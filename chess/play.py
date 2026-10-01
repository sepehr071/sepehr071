"""Community chess for the profile README: visitors play White, Stockfish plays Black,
an LLM coach comments in English + Persian.

Idea inspired by marcizhu/readme-chess (MIT); this is independent code.

Usage:
  python chess/play.py init    # reset to the starting position, print the README block
  python chess/play.py play    # handle one issue (env: ISSUE_TITLE, ISSUE_AUTHOR, REPLY_FILE, GITHUB_TOKEN)
  python chess/play.py reply   # post REPLY_FILE as a comment and close the issue (env: ISSUE_NUMBER, GITHUB_TOKEN)
"""
import json
import os
import re
import shutil
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import chess
import chess.engine
import chess.svg

REPO = "sepehr071/sepehr071"
OWNER = "sepehr071"
ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "chess"
README = ROOT / "README.md"
START, END = "<!-- CHESS:START -->", "<!-- CHESS:END -->"
TITLE_RE = re.compile(r"chess: (?:move ([a-h][1-8][a-h][1-8][qrbn]?)|(new))")
MODEL_URL = "https://models.github.ai/inference/chat/completions"
MOVE_URL = (f"https://github.com/{REPO}/issues/new?title=chess%3A+move+{{uci}}"
            "&body=Just+press+Submit+%E2%80%94+the+bot+plays+Black+within+a+minute.")
NEW_URL = (f"https://github.com/{REPO}/issues/new?title=chess%3A+new"
           "&body=Just+press+Submit+%E2%80%94+a+fresh+board+appears+within+a+minute.")
VALUES = {chess.PAWN: 100, chess.KNIGHT: 300, chess.BISHOP: 320, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0}
PIECES = [(chess.KING, "King"), (chess.QUEEN, "Queen"), (chess.ROOK, "Rook"),
          (chess.BISHOP, "Bishop"), (chess.KNIGHT, "Knight"), (chess.PAWN, "Pawn")]
BAD_WORDS = ("fuck", "shit", "bitch", "cunt", "dick", "asshole", "nigg", "fag", "whore", "slut")


# ---------- state ----------

def new_state(game=1):
    return {"game": game, "moves": [], "history": [], "last": None}


def board_of(state):
    board = chess.Board()
    for uci in state["moves"]:
        board.push_uci(uci)
    return board


def load(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ---------- engine ----------

def material(board):
    return sum(VALUES[p.piece_type] * (1 if p.color else -1) for p in board.piece_map().values())


def terminal(board):
    """White-POV centipawns for a finished game."""
    if board.is_checkmate():
        return -10000 if board.turn == chess.WHITE else 10000
    return 0


def fallback_move(board):
    """2-ply material search: no engine needed. ponytail: naive, Stockfish is the real opponent."""
    sign = 1 if board.turn == chess.WHITE else -1
    best, best_score = None, None
    for move in board.legal_moves:
        board.push(move)
        if board.is_checkmate():
            board.pop()
            return move
        replies = []
        for r in board.legal_moves:
            board.push(r)
            replies.append(sign * (terminal(board) if board.is_checkmate() else material(board)))
            board.pop()
        score = min(replies) if replies else 0
        board.pop()
        key = (score, board.is_capture(move), move.uci())
        if best is None or key > best_score:
            best, best_score = move, key
    return best


def stockfish_path():
    return shutil.which("stockfish") or ("/usr/games/stockfish" if os.path.exists("/usr/games/stockfish") else None)


def engine_turn(board, move):
    """Evaluate, apply White's `move` and pick Black's reply on a copy.
    Returns (reply or None, eval_before, eval_after, engine_name); evals are White-POV centipawns."""
    path = stockfish_path()
    if path:
        try:
            with chess.engine.SimpleEngine.popen_uci(path) as eng:
                lim = chess.engine.Limit(time=0.3)
                ev = lambda b: terminal(b) if b.is_game_over(claim_draw=True) else eng.analyse(b, lim)["score"].white().score(mate_score=10000)
                b = board.copy()
                before = ev(b)
                b.push(move)
                reply = None
                if not b.is_game_over(claim_draw=True):
                    reply = eng.play(b, chess.engine.Limit(time=0.5)).move
                    b.push(reply)
                return reply, before, ev(b), "Stockfish"
        except Exception as e:  # engine crash -> fall through to the built-in mover
            print(f"stockfish failed: {e}", file=sys.stderr)
    b = board.copy()
    before = material(b)
    b.push(move)
    reply = None if b.is_game_over(claim_draw=True) else fallback_move(b)
    if reply:
        b.push(reply)
    return reply, before, terminal(b) if b.is_game_over(claim_draw=True) else material(b), "fallback engine (Stockfish unavailable)"


# ---------- coach ----------

def clean(text, limit=140):
    """Plain text only: no HTML, markdown, links or control chars."""
    s = re.sub(r"<[^>]*>", "", str(text))
    s = re.sub(r"(?:https?://|www\.)\S+", " ", s)
    s = re.sub(r"[`*_#\[\]()<>|\\~{}@]", "", s)  # @ too: no mention pings from the LLM
    s = "".join(c for c in s if c.isprintable() or c == "\u200c")
    s = " ".join(s.split())
    return s if len(s) <= limit else s[:limit - 1].rstrip() + "…"


def pawns(cp):
    if abs(cp) >= 9000:
        return "mate" if cp > 0 else "-mate"
    return f"{cp / 100:+.1f}"


def template_coach(before, after):
    if after >= 9000:
        return "Checkmate is in sight for White - finish it!", "مات سفید نزدیک است؛ کار را تمام کن!"
    if after <= -9000:
        return "Black has a mating attack - defend the king!", "سیاه حملهٔ مات دارد؛ از شاه دفاع کن!"
    if after - before <= -150:
        return "That one cost White material - check what Black is attacking.", "این حرکت برای سفید گران تمام شد؛ ببین سیاه به چه حمله می\u200cکند."
    if after - before >= 100:
        return "Nice move - White just improved the position.", "حرکت خوبی بود؛ سفید وضعیت را بهتر کرد."
    return "Solid play - keep developing pieces and fight for the center.", "بازی محکمی است؛ مهره\u200cها را توسعه بده و برای مرکز بجنگ."


def coach(white_san, black_san, before, after, token=None, timeout=20):
    """One-line coach comment {en, fa} from GitHub Models; templated fallback on any failure."""
    token = token if token is not None else os.environ.get("GITHUB_TOKEN")
    if token:
        prompt = (f"White played {white_san}. Black replied {black_san or 'nothing (the game ended)'}. "
                  f"Engine eval from White's view, in pawns: before {pawns(before)}, after {pawns(after)}.")
        body = {"model": "openai/gpt-4.1-mini", "temperature": 0.7, "max_tokens": 200,
                "response_format": {"type": "json_object"},
                "messages": [
                    {"role": "system", "content": "You are a friendly chess coach. Reply ONLY with JSON "
                     '{"en": "...", "fa": "..."}: one short sentence each (max 120 characters) about '
                     "White's move and Black's reply. en in English, fa in Persian. Chess only, "
                     "no profanity, no markdown, no links, no emoji."},
                    {"role": "user", "content": prompt}]}
        req = urllib.request.Request(MODEL_URL, json.dumps(body).encode(), {
            "Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                content = json.load(r)["choices"][0]["message"]["content"]
            data = json.loads(content.strip().strip("`").removeprefix("json"))
            en, fa = clean(data["en"]), clean(data["fa"])
            if en and fa and not any(w in (en + fa).lower() for w in BAD_WORDS):
                return en, fa
        except Exception as e:
            print(f"coach fallback: {e}", file=sys.stderr)
    return template_coach(before, after)


# ---------- game logic ----------

def handle(title, user, state, stats, engine_fn=engine_turn, coach_fn=coach):
    """Apply one issue to state/stats in place. Returns (changed, reply_markdown); reply is None
    for titles outside the protocol, which the bot ignores entirely (no comment, no close)."""
    m = TITLE_RE.fullmatch(title.strip())
    if not m:
        return False, None
    board = board_of(state)
    if m.group(2):
        if not board.is_game_over(claim_draw=True) and user.lower() != OWNER:
            return False, "The current game is still running, so it can't be reset yet. Jump in with a move from the README instead!"
        game = state["game"] + 1
        state.clear()
        state.update(new_state(game))
        return True, f"Thanks @{user}! Game #{game} has started. You're White - pick the first move in the README."
    if board.is_game_over(claim_draw=True):
        return False, f"This game is already over ({result_text(board)}). Start a new one: [chess: new]({NEW_URL})"
    if board.turn != chess.WHITE:
        return False, "It's not White's turn right now - give the bot a minute and try again."
    try:
        move = chess.Move.from_uci(m.group(1))
    except ValueError:  # e.g. a1a1
        move = chess.Move.null()
    if move not in board.legal_moves:
        queen = chess.Move(move.from_square, move.to_square, chess.QUEEN)
        if not move.promotion and queen in board.legal_moves:
            move = queen
        else:
            return False, f"`{m.group(1)}` isn't a legal move in this position. Pick one of the links in the README."

    reply, before, after, engine_name = engine_fn(board, move)
    white_san = board.san(move)
    board.push(move)
    black_san = None
    if reply:
        black_san = board.san(reply)
        board.push(reply)
    en, fa = coach_fn(white_san, black_san, before, after)

    state["moves"] += [move.uci()] + ([reply.uci()] if reply else [])
    number = (len(state["moves"]) + 1) // 2
    state["history"] = (state["history"] + [{"n": number, "player": user, "white": white_san, "black": black_san}])[-5:]
    state["last"] = {"player": user, "white": white_san, "black": black_san, "en": en, "fa": fa,
                     "eval": after, "engine": engine_name}
    stats[user] = stats.get(user, 0) + 1

    lines = [f"Thanks @{user}! You played **{white_san}**"
             + (f", {engine_name} answered **{black_san}**" if black_san else "")
             + f" (eval {pawns(after)}).", "", f"> **Coach:** {en}", ">", f"> {fa}", "",
             f"[See the new board](https://github.com/{REPO}/blob/main/chess/board-{len(board.move_stack)}.svg)"
             f" - or the [README](https://github.com/{REPO}) to play the next move."]
    if board.is_game_over(claim_draw=True):
        lines += ["", f"**Game over: {result_text(board)}** Start a new one: [chess: new]({NEW_URL})"]
    return True, "\n".join(lines)


def result_text(board):
    """Draws by threefold repetition / 50-move rule are claimed automatically (claim_draw=True everywhere)."""
    outcome = board.outcome(claim_draw=True)
    if outcome.winner is not None:
        return "checkmate, " + ("White wins!" if outcome.winner == chess.WHITE else "Black wins.")
    return outcome.termination.name.lower().replace("_", " ") + ", it's a draw."


# ---------- output ----------

def write_board(board):
    """Write chess/board-<ply>.svg (unique name so caches never show a stale board), delete older ones."""
    name = f"board-{len(board.move_stack)}.svg"
    for old in DIR.glob("board-*.svg"):
        if old.name != name:
            old.unlink()
    check = board.king(board.turn) if board.is_check() else None
    svg = chess.svg.board(board, size=360, lastmove=board.peek() if board.move_stack else None, check=check)
    (DIR / name).write_text(svg, encoding="utf-8")
    return name


def render_block(state, stats):
    board = board_of(state)
    ply = len(board.move_stack)
    out = [START, '<h3 align="center">Chess vs. the AI Coach</h3>', "",
           f'<p align="center">Game #{state["game"]} &middot; you play <b>White</b>: click a move below, '
           "Stockfish answers as Black and an LLM coach comments.</p>", "",
           f'<p align="center"><img src="chess/board-{ply}.svg" width="360" alt="Chess board, move {ply // 2 + 1}"></p>', ""]
    last = state.get("last")
    if board.is_game_over(claim_draw=True):
        out.append(f'<p align="center"><b>Game over: {result_text(board)}</b> &middot; <a href="{NEW_URL}">Start a new game</a></p>')
    else:
        out.append(f'<p align="center"><b>{"White" if board.turn else "Black"} to move</b>'
                   + (f' &middot; last: {last["white"]}' + (f' / {last["black"]}' if last["black"] else "")
                      + f' by <a href="https://github.com/{last["player"]}">@{last["player"]}</a>' if last else "")
                   + "</p>")
    if last:
        out += ["", f'<p align="center"><i>Coach:</i> {html(last["en"])}</p>',
                f'<p align="center" dir="rtl">{html(last["fa"])}</p>']
        if "Stockfish" not in last.get("engine", "Stockfish"):
            out.append(f'<p align="center"><sub>Black played with the {last["engine"]}.</sub></p>')
    out.append("")
    if not board.is_game_over(claim_draw=True) and board.turn == chess.WHITE:
        out += ["<details open><summary><b>Your move</b> (legal moves for White)</summary>", "",
                "| Piece | Moves |", "| :-- | :-- |"]
        for ptype, label in PIECES:
            moves = sorted((board.san(mv), mv.uci()) for mv in board.legal_moves
                           if board.piece_type_at(mv.from_square) == ptype)
            if moves:
                out.append(f"| {label} | " + " &middot; ".join(f"[{san}]({MOVE_URL.format(uci=uci)})" for san, uci in moves) + " |")
        out += ["", "</details>", ""]
    if state["history"]:
        out += ["**Last moves**", "", "| # | Player | White | Black |", "| --: | :-- | :-- | :-- |"]
        out += [f'| {h["n"]} | [@{h["player"]}](https://github.com/{h["player"]}) | {h["white"]} | {h["black"] or "-"} |'
                for h in reversed(state["history"])]
        out.append("")
    if stats:
        top = sorted(stats.items(), key=lambda kv: (-kv[1], kv[0].lower()))[:5]
        out += ["**Top players**", "", "| Player | Moves |", "| :-- | --: |"]
        out += [f"| [@{u}](https://github.com/{u}) | {n} |" for u, n in top]
        out.append("")
    out.append(END)
    return "\n".join(out)


def html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def update_readme(block, path=None):
    path = path or README
    text = path.read_text(encoding="utf-8")
    i, j = text.find(START), text.find(END)
    if i < 0 or j < i:
        raise SystemExit("README is missing the CHESS:START/END markers")
    path.write_text(text[:i] + block + text[j + len(END):], encoding="utf-8")


def api(method, url, token, body=None):
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/{url}", method=method,
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status


def main(mode):
    state_path, stats_path = DIR / "state.json", DIR / "stats.json"
    if mode == "init":
        state, stats = new_state(1), load(stats_path, {})
        save(state_path, state)
        save(stats_path, stats)
        write_board(board_of(state))
        print(render_block(state, stats))
    elif mode == "play":
        state, stats = load(state_path, new_state(1)), load(stats_path, {})
        changed, msg = handle(os.environ.get("ISSUE_TITLE", ""), os.environ.get("ISSUE_AUTHOR", "someone"), state, stats)
        if changed:
            save(state_path, state)
            save(stats_path, stats)
            write_board(board_of(state))
            if os.environ.get("GITHUB_ACTIONS") == "true":
                update_readme(render_block(state, stats))
        if msg is not None:
            Path(os.environ["REPLY_FILE"]).write_text(msg, encoding="utf-8")
    elif mode == "reply":
        if not TITLE_RE.fullmatch(os.environ.get("ISSUE_TITLE", "").strip()):
            return  # not our protocol: stay silent, never comment (no spam loops)
        token, number = os.environ["GITHUB_TOKEN"], int(os.environ["ISSUE_NUMBER"])
        reply = Path(os.environ.get("REPLY_FILE", "-"))
        ok = os.environ.get("JOB_STATUS", "success") == "success"
        msg = reply.read_text(encoding="utf-8") if ok and reply.is_file() else \
            "Sorry, something went wrong while processing this move (nothing was saved). Please try again in a minute."
        try:
            api("POST", f"issues/{number}/comments", token, {"body": msg})
        finally:
            api("PATCH", f"issues/{number}", token, {"state": "closed"})
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
