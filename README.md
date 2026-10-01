<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,100:06B6D4&height=170&section=header&text=Sepehr%20Radmard&fontColor=ffffff&fontSize=46&fontAlignY=36&desc=AI%20Engineer%20%C2%B7%20Voice%20Agents%20%C2%B7%20Tool-Calling%20Agents%20%C2%B7%20Evals&descAlignY=58&descSize=16" alt="Sepehr Radmard, AI Engineer: voice agents, tool-calling agents, evals" width="100%">
</p>

<p align="center">
  <b>I build AI that talks, acts and gets checked, most of it Persian-first.</b><br>
  Realtime voice agents · approval-gated MCP agents · LLM-as-judge evals · grounded LLM apps
</p>

<p align="center" dir="rtl">سلام! من سپهرم. دستیارهای هوشمند فارسی می&zwnj;سازم، از صدا تا ابزار.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/LiveKit_Agents-1F2937?style=flat-square&logo=webrtc&logoColor=white" alt="LiveKit Agents">
  <img src="https://img.shields.io/badge/OpenAI_Realtime-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Realtime">
  <img src="https://img.shields.io/badge/MCP-6E56CF?style=flat-square" alt="MCP">
  <img src="https://img.shields.io/badge/Vercel_AI_SDK-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel AI SDK">
  <img src="https://img.shields.io/badge/OpenRouter-6566F1?style=flat-square" alt="OpenRouter">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Asterisk-F68F1E?style=flat-square&logo=asterisk&logoColor=white" alt="Asterisk">
</p>

---

## What I build

- **Voice, in real time.** Speech-to-speech agents on LiveKit and OpenAI Realtime, plus a Persian phone receptionist on a real Asterisk line.
- **Agents with a human in the loop.** MCP and native tool calling, default-deny tool policies, hard step and dollar caps. Reads run, writes wait for a click.
- **Evals, not vibes.** LLM-as-judge scoring, generated test suites for voice agents, human expert scoring side by side.
- **The model drafts, code does the math.** Structured outputs, deterministic parsers, every value traced back to its source.
- **Persian-first.** RTL interfaces, Farsi speech in and out, turn-taking tuned for Farsi pauses.

<details>
<summary><b>Capabilities, and the repos that prove them</b></summary>
<br>

| Capability | Proof |
|---|---|
| Realtime voice agents (LiveKit, speech-to-speech) | [livekit-fa-agent](https://github.com/sepehr071/livekit-fa-agent) · [voice-chess-coach](https://github.com/sepehr071/voice-chess-coach) · [product-assistant](https://github.com/sepehr071/product-assistant) |
| Telephony voice AI (Asterisk, Android dialer) | [phone-agent](https://github.com/sepehr071/phone-agent) |
| Tool-calling / MCP agents (approval gates in pm-assistant, pr-agent, dongeto) | [pm-assistant](https://github.com/sepehr071/pm-assistant) · [agent-studio](https://github.com/sepehr071/agent-studio) · [pr-agent](https://github.com/sepehr071/pr-agent) · [dongeto](https://github.com/sepehr071/dongeto) |
| Coding agents | [sepicode](https://github.com/sepehr071/sepicode) · [pr-agent](https://github.com/sepehr071/pr-agent) |
| LLM evals (LLM-as-judge, test generation, human scoring) | [voice-agent-testgen](https://github.com/sepehr071/voice-agent-testgen) · [rag-evaluator](https://github.com/sepehr071/rag-evaluator) · [polymind](https://github.com/sepehr071/polymind) |
| RAG and grounded answers | [livekit-fa-agent](https://github.com/sepehr071/livekit-fa-agent) · [product-assistant](https://github.com/sepehr071/product-assistant) · [steel-market-analyst](https://github.com/sepehr071/steel-market-analyst) |
| Structured output and document AI (OCR, diarization, vision) | [invoice-extractor](https://github.com/sepehr071/invoice-extractor) · [meeting-assistant](https://github.com/sepehr071/meeting-assistant) · [feedo](https://github.com/sepehr071/feedo) · [ai-explain](https://github.com/sepehr071/ai-explain) |
| Text-to-SQL with guardrails | [erp-sql-agent](https://github.com/sepehr071/erp-sql-agent) |
| AI safety (DLP, sandboxing, prompt-injection guards, step and spend caps) | [polymind](https://github.com/sepehr071/polymind) · [invoice-extractor](https://github.com/sepehr071/invoice-extractor) · [ai-explain](https://github.com/sepehr071/ai-explain) · [sepicode](https://github.com/sepehr071/sepicode) |

</details>

---

## Featured projects

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/livekit-fa-agent"><img src="https://raw.githubusercontent.com/sepehr071/livekit-fa-agent/main/docs/images/hero.png" alt="Rahnama: Persian speech-to-speech voice agent (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/livekit-fa-agent">Rahnama · livekit-fa-agent</a></h3>
A Persian voice agent that talks back in real time and answers only from retrieved passages, built to work on filtered networks.
<br><br>
<sub>RAG via a <code>search_knowledge</code> tool call · turn-taking tuned for Farsi pauses · UDP → ICE/TCP fallback</sub><br>
<sub><b>Python · LiveKit Agents · OpenAI Realtime · nginx</b></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/voice-chess-coach"><img src="https://raw.githubusercontent.com/sepehr071/voice-chess-coach/main/docs/images/hero.png" alt="Voice chess coach with a live board and bilingual transcript (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/voice-chess-coach">Chess Live · voice-chess-coach</a></h3>
Talk to a chess coach, play White by voice, and watch it answer as Black on a live board, in Persian or English.
<br><br>
<sub>The voice model can't fake a move: <code>tool_choice="required"</code> + python-chess owns the rules · board sync over LiveKit RPC</sub><br>
<sub><b>React 19 · TypeScript · LiveKit · Python</b></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/pm-assistant"><img src="https://raw.githubusercontent.com/sepehr071/pm-assistant/main/docs/images/hero.png" alt="PM Assistant: chat with tool calls and the approval gate (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/pm-assistant">PM Assistant · pm-assistant</a></h3>
A local-first AI copilot for project managers: reads and acts across Jira, GitHub, Slack and more, and every write waits for your click.
<br><br>
<sub>Default-deny tool policy · approve/reject mid-stream (browser or Telegram) · plain-English rules compiled once, polled with zero LLM calls</sub><br>
<sub><b>Python · FastAPI · React 19 · SQLite · MCP</b></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/sepicode"><img src="https://raw.githubusercontent.com/sepehr071/sepicode/main/docs/images/hero.png" alt="sepicode editing a file in the terminal (scripted demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/sepicode">sepicode</a></h3>
A full-screen terminal coding agent that reads, edits, searches and runs your code, with hard step and dollar caps on every turn.
<br><br>
<sub>Streaming Markdown, live tool-call timeline, inline diffs · nine zod-typed tools · read-only sub-agent capped at 8 steps / $0.25</sub><br>
<sub><b>Bun · TypeScript · React · OpenTUI · OpenRouter</b></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/meeting-assistant"><img src="https://raw.githubusercontent.com/sepehr071/meeting-assistant/main/docs/images/meeting-minutes-dark.png" alt="Speaker-attributed minutes of a fictional Persian meeting (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/meeting-assistant">Meeting Assistant · meeting-assistant</a></h3>
Drop in a Persian meeting recording; get back who said what, the decisions, the action items and a follow-up email.
<br><br>
<sub>Parallel chunked transcription with speaker stitching across seams · minutes from diarized words, summaries via strict JSON schema</sub><br>
<sub><b>Python · FastAPI · Next.js · ElevenLabs Scribe v2</b></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/polymind"><img src="https://raw.githubusercontent.com/sepehr071/polymind/main/docs/images/hero.png" alt="Polymind: model arena comparing three models side by side (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/polymind">Polymind · polymind</a></h3>
A self-hosted, multi-model AI workspace with a DLP gate, sandboxed code execution and first-class Persian (RTL) support.
<br><br>
<sub>Side-by-side arena + judged debates between 2-5 models · DLP scan before any provider · LLM-written pandas runs under bubblewrap, no network</sub><br>
<sub><b>Python · FastAPI · PostgreSQL · React · OpenRouter</b></sub>
</td>
</tr>
</table>

---

## More projects

<table>
<tr>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/product-assistant"><img src="https://raw.githubusercontent.com/sepehr071/product-assistant/main/docs/images/hero.png" alt="Product Talk kiosk mid-conversation (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/product-assistant">product-assistant</a></b><br>
<sub>Scan a product, ask it out loud about sugar or allergens. Realtime voice grounded in pack facts.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/phone-agent"><img src="https://raw.githubusercontent.com/sepehr071/phone-agent/main/docs/images/hero.png" alt="phone-agent architecture diagram" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/phone-agent">phone-agent</a></b><br>
<sub>Persian AI phone receptionist on a real line: Asterisk AudioSocket, 8 kHz PCM, plus an Android dialer app.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/voice-agent-testgen"><img src="https://raw.githubusercontent.com/sepehr071/voice-agent-testgen/main/docs/images/hero.png" alt="Voice Agent TestKit: a judged test run (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/voice-agent-testgen">voice-agent-testgen</a></b><br>
<sub>Paste a voice agent's prompt, get a judged test suite back. Runs the real agent via LiveKit's <code>AgentSession</code>.</sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/agent-studio"><img src="https://raw.githubusercontent.com/sepehr071/agent-studio/main/docs/images/hero.png" alt="Agent Studio: an agent turn with an MCP tool call (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/agent-studio">agent-studio</a></b><br>
<sub>Persian-first AI workbench: native tools and MCP servers (stdio, HTTP, SSE), every step visible in the chat.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/pr-agent"><img src="https://raw.githubusercontent.com/sepehr071/pr-agent/main/docs/images/hero.png" alt="PR Agent: dashboard reviewing a merge request (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/pr-agent">pr-agent</a></b><br>
<sub>Seven AI reviewers on every GitLab merge request, one human who decides what gets posted.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/erp-sql-agent"><img src="https://raw.githubusercontent.com/sepehr071/erp-sql-agent/main/docs/images/hero.png" alt="Accounting dashboard with audit flags (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/erp-sql-agent">erp-sql-agent</a></b><br>
<sub>Ask your ledger in Persian, get audited numbers. SELECT-only SQL tool with a forced <code>LIMIT</code>.</sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/rag-evaluator"><img src="https://raw.githubusercontent.com/sepehr071/rag-evaluator/main/docs/images/hero.png" alt="RAG Evaluator: aggregate judge scores dashboard (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/rag-evaluator">rag-evaluator</a></b><br>
<sub>LLM-as-judge on four criteria, plus human experts scoring the same answers with AI scores hidden.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/steel-market-analyst"><img src="https://raw.githubusercontent.com/sepehr071/steel-market-analyst/main/docs/images/hero.png" alt="METAP: AI analysis screen (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/steel-market-analyst">steel-market-analyst</a></b><br>
<sub>Price PDFs in, grounded market read out. 13 named hallucination failure modes in the prompt pack.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/invoice-extractor"><img src="https://raw.githubusercontent.com/sepehr071/invoice-extractor/main/docs/images/hero.png" alt="invoice-ai review UI on a synthetic invoice" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/invoice-extractor">invoice-extractor</a></b><br>
<sub>OCR + LLM extraction, every value linked to its box on the page. Injection-guarded, runs fully local.</sub>
</td>
</tr>
<tr>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/dongeto"><img src="https://raw.githubusercontent.com/sepehr071/dongeto/main/docs/images/hero.png" alt="Dongeto: Farsi chat, draft card and settlement slip (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/dongeto">dongeto · دنگتو</a></b><br>
<sub>Type the expense in Farsi. The LLM drafts it, unit-tested code does the money math.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/feedo"><img src="https://raw.githubusercontent.com/sepehr071/feedo/main/docs/images/hero.png" alt="Feedo: reports dashboard and mobile intake form (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/feedo">feedo</a></b><br>
<sub>Plain-Persian bug reports plus screenshots in, structured drafts out. The model never picks IDs.</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/ai-explain"><img src="https://raw.githubusercontent.com/sepehr071/ai-explain/main/docs/images/hero.png" alt="AI Explain: landing page next to a generated canvas" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/ai-explain">ai-explain</a></b><br>
<sub>Ask anything, get an interactive HTML/SVG explainer, planned and streamed into a sandboxed iframe.</sub>
</td>
</tr>
</table>

<details>
<summary><b>Off the clock: True Anomaly, a WebGPU space sim</b></summary>
<br>
<a href="https://github.com/sepehr071/true-anomaly"><img src="https://raw.githubusercontent.com/sepehr071/true-anomaly/main/docs/images/hero.png" alt="True Anomaly: chase view near Jupiter with the live HUD" width="520"></a>
<br>
Fly a 6DOF probe through a real-scale solar system in the browser, every planet placed from NASA/JPL Horizons data. Physics in true kilometres with a Newton-iteration Kepler solver, rendered on Three.js <code>WebGPURenderer</code> with a WebGL fallback.
</details>

<p align="center"><sub>All screenshots use demo or synthetic data. Open any repo for architecture notes, setup and more screenshots.</sub></p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,100:4F46E5&height=90&section=footer" alt="" width="100%">
</p>
