"""Run: pip install chess==1.11.2 pytest && pytest chess/test_play.py"""
import chess
import pytest

import play


def fake_engine(board, move):
    b = board.copy()
    b.push(move)
    reply = None if b.is_game_over() else sorted(b.legal_moves, key=lambda m: m.uci())[0]
    return reply, 10, 20, "Stockfish"


def fake_coach(white_san, black_san, before, after):
    return f"Played {white_san}"


def run(title, user="alice", state=None, stats=None):
    state = state if state is not None else play.new_state()
    stats = stats if stats is not None else {}
    changed, msg = play.handle(title, user, state, stats, fake_engine, fake_coach)
    return changed, msg, state, stats


@pytest.mark.parametrize("title", ["chess: move e2e4", " chess: move e7e8q ", "chess: new"])
def test_regex_accepts(title):
    assert play.TITLE_RE.fullmatch(title.strip())


@pytest.mark.parametrize("title", ["chess: move e2e9", "chess: move E2E4", "chess:move e2e4", "chess: move e2e4 && rm",
                                   "chess: move e7e8k", "chess: new game", "chess: move e2e4\nchess: move d2d4", ""])
def test_regex_rejects(title):
    assert not play.TITLE_RE.fullmatch(title.strip())
    changed, msg, state, _ = run(title)
    assert not changed and msg is None and state["moves"] == []  # ignored: no comment at all


def test_reply_ignores_non_protocol_titles(monkeypatch):
    calls = []
    monkeypatch.setattr(play, "api", lambda *a, **k: calls.append(a))
    monkeypatch.setenv("ISSUE_TITLE", "chess: hello")
    play.main("reply")
    assert calls == []


def test_threefold_repetition_ends_game():
    state = play.new_state()
    state["moves"] = ["g1f3", "g8f6", "f3g1", "f6g8", "g1f3", "g8f6", "f3g1", "f6g8"]  # start position x3
    board = play.board_of(state)
    assert board.is_game_over(claim_draw=True) and "repetition" in play.result_text(board)
    changed, msg, _, _ = run("chess: move e2e4", state=state)
    assert not changed and "already over" in msg


def test_legal_move_plays_black_and_updates_stats():
    changed, msg, state, stats = run("chess: move e2e4")
    assert changed and state["moves"][0] == "e2e4" and len(state["moves"]) == 2
    assert stats == {"alice": 1}
    assert state["last"]["white"] == "e4" and state["last"]["en"] == "Played e4"
    assert "board-2.svg" in msg and play.board_of(state).turn == chess.WHITE


@pytest.mark.parametrize("title", ["chess: move e2e5", "chess: move a1a1"])
def test_illegal_move_rejected(title):
    changed, msg, state, stats = run(title)
    assert not changed and "isn't a legal move" in msg and stats == {}


def test_new_game_only_when_over_or_owner():
    state = play.new_state()
    run("chess: move e2e4", state=state)
    changed, msg, _, _ = run("chess: new", state=state)
    assert not changed and "still running" in msg
    changed, _, state, _ = run("chess: new", user="Sepehr071", state=state)
    assert changed and state["game"] == 2 and state["moves"] == []


def test_mate_by_white_ends_game_and_allows_new():
    state = play.new_state()
    state["moves"] = ["f2f3", "e7e5", "g2g4", "d8h4"]  # fool's mate: black already won
    changed, msg, _, _ = run("chess: move a2a3", state=state)
    assert not changed and "already over" in msg
    state = play.new_state()
    state["moves"] = ["e2e4", "e7e5", "f1c4", "b8c6", "d1h5", "g8f6"]  # scholar's mate next
    changed, msg, state, _ = run("chess: move h5f7", state=state)
    assert changed and state["last"]["black"] is None and "White wins" in msg
    changed, _, state, _ = run("chess: new", user="bob", state=state)
    assert changed and state["game"] == 2


def test_promotion_defaults_to_queen():
    state = play.new_state()
    state["moves"] = ["a2a4", "b7b5", "a4b5", "a7a6", "b5a6", "c8b7", "a6b7", "h7h6"]
    changed, _, state, _ = run("chess: move b7a8", state=state)
    assert changed and state["moves"][8] == "b7a8q"


def test_fallback_engine_takes_free_queen_and_mates():
    board = chess.Board("4k3/8/8/3q4/4P3/8/8/4K3 w - - 0 1")
    assert play.fallback_move(board) == chess.Move.from_uci("e4d5")
    board = chess.Board("6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1")
    assert play.fallback_move(board) == chess.Move.from_uci("a1a8")


def test_engine_turn_without_stockfish(monkeypatch):
    monkeypatch.setattr(play, "stockfish_path", lambda: None)
    reply, before, after, name = play.engine_turn(chess.Board(), chess.Move.from_uci("e2e4"))
    assert reply is not None and before == 0 and "fallback" in name


def test_clean_and_coach_fallback():
    assert play.clean("<b>Nice</b> [link](https://x.y) **move**\x07") == "Nice link move"
    assert play.clean("hi @octocat see www.evil.com now") == "hi octocat see now"
    assert len(play.clean("a" * 300)) == 140
    assert play.coach("e4", "e5", 0, 20, token="") == play.template_coach(0, 20)  # no token -> template


def test_coach_uses_llm_json_and_rejects_bad(monkeypatch):
    import io, json
    def fake_urlopen(content):
        body = json.dumps({"choices": [{"message": {"content": content}}]}).encode()
        class R(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *a): pass
        return lambda req, timeout: R(body)
    monkeypatch.setattr(play.urllib.request, "urlopen", fake_urlopen('{"en": "Good <i>e4</i>!"}'))
    assert play.coach("e4", "e5", 0, 20, token="t") == "Good e4!"
    monkeypatch.setattr(play.urllib.request, "urlopen", fake_urlopen('{"en": "shit move"}'))
    assert play.coach("e4", "e5", 0, 20, token="t") == play.template_coach(0, 20)
    monkeypatch.setattr(play.urllib.request, "urlopen", fake_urlopen("not json"))
    assert play.coach("e4", "e5", 0, 20, token="t") == play.template_coach(0, 20)


def test_render_and_update_readme(tmp_path, monkeypatch):
    state, stats = play.new_state(), {}
    play.handle("chess: move e2e4", "alice", state, stats, fake_engine, fake_coach)
    play.handle("chess: move d2d4", "bob", state, stats, fake_engine, fake_coach)
    play.handle("chess: move g1f3", "bob", state, stats, fake_engine, fake_coach)
    block = play.render_block(state, stats)
    assert block.startswith(play.START) and block.endswith(play.END)
    assert "board-6.svg" in block and 'dir="rtl"' not in block and "Coach:</i> Played Nf3" in block
    assert "issues/new?title=chess%3A+move+b1c3&body=Just+press+Submit" in block
    assert block.index("@bob](") < block.index("@alice](https://github.com/alice) | 1")  # top players sorted
    readme = tmp_path / "README.md"
    readme.write_text(f"intro\n{play.START}\nold\n{play.END}\noutro\n", encoding="utf-8")
    play.update_readme(block, readme)
    text = readme.read_text(encoding="utf-8")
    assert text.startswith("intro\n") and text.endswith("\noutro\n") and "old" not in text

    monkeypatch.setattr(play, "DIR", tmp_path)
    (tmp_path / "board-2.svg").write_text("x")
    assert play.write_board(play.board_of(state)) == "board-6.svg"
    assert [p.name for p in tmp_path.glob("board-*.svg")] == ["board-6.svg"]


def test_game_over_render_has_new_game_link():
    state = play.new_state()
    state["moves"] = ["f2f3", "e7e5", "g2g4", "d8h4"]
    block = play.render_block(state, {})
    assert "chess%3A+new" in block and "Your move" not in block
