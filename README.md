<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4F46E5,100:06B6D4&height=170&section=header&text=Sepehr%20Radmard&fontColor=ffffff&fontSize=46&fontAlignY=36&desc=AI%20Engineer%20%C2%B7%20RAG%20%2B%20Retrieval%20%C2%B7%20AI%20Agents%20%C2%B7%20Evals&descAlignY=58&descSize=16" alt="Sepehr Radmard, AI Engineer: RAG and retrieval, AI agents, evals" width="100%">
</p>

<p align="center">
  <b>I build AI that finds the right source, acts on it and gets checked.</b><br>
  Hybrid RAG & reranking · approval-gated MCP agents · LLM-as-judge evals · realtime voice agents
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/LlamaIndex_%C2%B7_LlamaCloud-8B5CF6?style=flat-square" alt="LlamaIndex / LlamaCloud">
  <img src="https://img.shields.io/badge/Cohere_Rerank-39594D?style=flat-square" alt="Cohere Rerank">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/MCP-6E56CF?style=flat-square" alt="MCP">
  <img src="https://img.shields.io/badge/LiveKit_Agents-1F2937?style=flat-square&logo=webrtc&logoColor=white" alt="LiveKit Agents">
  <img src="https://img.shields.io/badge/Vercel_AI_SDK-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel AI SDK">
  <img src="https://img.shields.io/badge/OpenRouter-6566F1?style=flat-square" alt="OpenRouter">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL">
</p>

<!-- TERMINAL:START -->
<p align="center">
  <img src="docs/terminal.gif" width="900" alt="Animated retro terminal demo session: a Persian voice agent answers a question using a search_knowledge tool, a PM assistant pauses a jira.create_issue tool call for approval, an eval run passes 12/12 demo scenarios, then a neofetch-style card for Sepehr Radmard, AI Engineer." />
</p>
<!-- TERMINAL:END -->

---

## What I build

- **RAG and retrieval.** Hybrid dense + sparse vector search across several indexes, multi-query expansion with reciprocal rank fusion, one global Cohere rerank, and answers grounded only in retrieved passages. Scored with a RAG evaluator, not eyeballed.
- **Agents with a human in the loop.** MCP and native tool calling, default-deny tool policies, hard step and dollar caps. Reads run, writes wait for a click. Plus a terminal coding agent.
- **Evals, not vibes.** LLM-as-judge scoring, generated test suites for voice agents, human expert scoring side by side.
- **Voice, in real time.** Speech-to-speech agents on LiveKit and OpenAI Realtime that call retrieval tools mid-conversation, plus a phone receptionist on a real Asterisk line.
- **The model drafts, code does the math.** Structured outputs, deterministic parsers, every value traced back to its source. Multilingual, including Persian (RTL) support.

<details>
<summary><b>Capabilities, and the repos that prove them</b></summary>
<br>

| Capability | Proof |
|---|---|
| RAG, retrieval & vector search (hybrid dense + sparse over LlamaCloud vector indexes, `text-embedding-3-large`, multi-query fusion, Cohere rerank, grounded answers, RAG evaluation) | [rag-service](https://github.com/sepehr071/rag-service) · [rag-evaluator](https://github.com/sepehr071/rag-evaluator) · [livekit-fa-agent](https://github.com/sepehr071/livekit-fa-agent) · [product-assistant](https://github.com/sepehr071/product-assistant) |
| Realtime voice agents (LiveKit, speech-to-speech) | [livekit-fa-agent](https://github.com/sepehr071/livekit-fa-agent) · [voice-chess-coach](https://github.com/sepehr071/voice-chess-coach) · [product-assistant](https://github.com/sepehr071/product-assistant) |
| Telephony voice AI (Asterisk, Android dialer) | [phone-agent](https://github.com/sepehr071/phone-agent) |
| Tool-calling / MCP agents (approval gates in pm-assistant, pr-agent, dongeto) | [pm-assistant](https://github.com/sepehr071/pm-assistant) · [agent-studio](https://github.com/sepehr071/agent-studio) · [pr-agent](https://github.com/sepehr071/pr-agent) · [dongeto](https://github.com/sepehr071/dongeto) |
| MCP servers (14 on PyPI, Iranian services) | [snapp-mcp](https://github.com/sepehr071/snapp-mcp) · [digikala-mcp](https://github.com/sepehr071/digikala-mcp) · [mrbilit-mcp](https://github.com/sepehr071/mrbilit-mcp) · [bale-mcp](https://github.com/sepehr071/bale-mcp) · [payping-mcp](https://github.com/sepehr071/payping-mcp) · [and 9 more](#mcp-servers-for-iranian-services) |
| Coding agents | [sepicode](https://github.com/sepehr071/sepicode) · [pr-agent](https://github.com/sepehr071/pr-agent) |
| LLM evals (LLM-as-judge, test generation, human scoring) | [voice-agent-testgen](https://github.com/sepehr071/voice-agent-testgen) · [rag-evaluator](https://github.com/sepehr071/rag-evaluator) · [polymind](https://github.com/sepehr071/polymind) |
| Structured output and document AI (OCR, diarization, vision) | [invoice-extractor](https://github.com/sepehr071/invoice-extractor) · [meeting-assistant](https://github.com/sepehr071/meeting-assistant) · [feedo](https://github.com/sepehr071/feedo) · [ai-explain](https://github.com/sepehr071/ai-explain) · [steel-market-analyst](https://github.com/sepehr071/steel-market-analyst) |
| Text-to-SQL with guardrails | [erp-sql-agent](https://github.com/sepehr071/erp-sql-agent) |
| AI safety (DLP, sandboxing, prompt-injection guards, step and spend caps) | [polymind](https://github.com/sepehr071/polymind) · [invoice-extractor](https://github.com/sepehr071/invoice-extractor) · [ai-explain](https://github.com/sepehr071/ai-explain) · [sepicode](https://github.com/sepehr071/sepicode) |

</details>

---

## Featured projects

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/rag-service"><img src="https://raw.githubusercontent.com/sepehr071/rag-service/main/docs/images/hero.png" alt="rag-service architecture: query, multi-query expansion, hybrid retrieval, fusion, Cohere rerank, top-k passages" width="100%"></a>
<h3><a href="https://github.com/sepehr071/rag-service">rag-service</a></h3>
A hybrid retrieval API: one HTTP call turns a question into a short, reranked list of source passages that any LLM agent can use as a retrieval tool.
<br><br>
<sub>Hybrid dense + sparse search over several LlamaCloud vector indexes (<code>text-embedding-3-large</code>) · 3 LLM paraphrases + reciprocal rank fusion · one global Cohere rerank, falls back to fusion order on failure</sub><br>
<sub><b>Python · FastAPI · LlamaIndex · LlamaCloud · Cohere Rerank</b></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/pm-assistant"><img src="https://raw.githubusercontent.com/sepehr071/pm-assistant/main/docs/images/hero.png" alt="PM Assistant: chat with tool calls and the approval gate (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/pm-assistant">PM Assistant · pm-assistant</a></h3>
A local-first AI copilot for project managers: reads and acts across Jira, GitHub, Slack and more, and every write waits for your click.
<br><br>
<sub>Default-deny tool policy · approve/reject mid-stream (browser or Telegram) · plain-English rules compiled once, polled with zero LLM calls</sub><br>
<sub><b>Python · FastAPI · React 19 · SQLite · MCP</b></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/polymind"><img src="https://raw.githubusercontent.com/sepehr071/polymind/main/docs/images/hero.png" alt="Polymind: model arena comparing three models side by side (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/polymind">Polymind · polymind</a></h3>
A self-hosted, multi-model AI workspace with a DLP gate, sandboxed code execution and first-class Persian (RTL) support.
<br><br>
<sub>Side-by-side arena + judged debates between 2-5 models · DLP scan before any provider · LLM-written pandas runs under bubblewrap, no network</sub><br>
<sub><b>Python · FastAPI · PostgreSQL · React · OpenRouter</b></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/livekit-fa-agent"><img src="https://raw.githubusercontent.com/sepehr071/livekit-fa-agent/main/docs/images/hero.png" alt="Rahnama: Persian speech-to-speech voice agent (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/livekit-fa-agent">Rahnama · livekit-fa-agent</a></h3>
A Persian voice agent that talks back in real time and answers only from retrieved passages, built to work on filtered networks.
<br><br>
<sub>RAG via a <code>search_knowledge</code> tool call · turn-taking tuned for Farsi pauses · UDP → ICE/TCP fallback</sub><br>
<sub><b>Python · LiveKit Agents · OpenAI Realtime · nginx</b></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/sepicode"><img src="https://raw.githubusercontent.com/sepehr071/sepicode/main/docs/images/hero.png" alt="sepicode editing a file in the terminal (scripted demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/sepicode">sepicode</a></h3>
A full-screen terminal coding agent that reads, edits, searches and runs your code, with hard step and dollar caps on every turn.
<br><br>
<sub>Streaming Markdown, live tool-call timeline, inline diffs · nine zod-typed tools · read-only sub-agent capped at 8 steps / $0.25</sub><br>
<sub><b>Bun · TypeScript · React · OpenTUI · OpenRouter</b></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/sepehr071/meeting-assistant"><img src="https://raw.githubusercontent.com/sepehr071/meeting-assistant/main/docs/images/meeting-minutes-dark.png" alt="Speaker-attributed minutes of a fictional Persian meeting (demo data)" width="100%"></a>
<h3><a href="https://github.com/sepehr071/meeting-assistant">Meeting Assistant · meeting-assistant</a></h3>
Drop in a Persian meeting recording; get back who said what, the decisions, the action items and a follow-up email.
<br><br>
<sub>Parallel chunked transcription with speaker stitching across seams · minutes from diarized words, summaries via strict JSON schema</sub><br>
<sub><b>Python · FastAPI · Next.js · ElevenLabs Scribe v2</b></sub>
</td>
</tr>
</table>

---

## MCP servers for Iranian services

Plug Iran's everyday apps into Claude, Cursor, VS Code or any MCP client. Each one is a small Python stdio server on PyPI: `uvx <name>` and go.

| Server | What your agent can do | |
|---|---|---|
| **Shopping** | | |
| [snapp-mcp](https://github.com/sepehr071/snapp-mcp) | Search Snappfood and SnappMarket food and groceries, compare prices, find deals | ![stars](https://img.shields.io/github/stars/sepehr071/snapp-mcp?style=flat-square&label=%E2%98%85) |
| [digikala-mcp](https://github.com/sepehr071/digikala-mcp) | Search Digikala with feature filters, best picks for a budget, sellers, price history, reviews | ![stars](https://img.shields.io/github/stars/sepehr071/digikala-mcp?style=flat-square&label=%E2%98%85) |
| [technolife-mcp](https://github.com/sepehr071/technolife-mcp) | Electronics on Technolife: compare sellers and installment prices | ![stars](https://img.shields.io/github/stars/sepehr071/technolife-mcp?style=flat-square&label=%E2%98%85) |
| [masterkala-mcp](https://github.com/sepehr071/masterkala-mcp) | Gadgets and accessories on MasterKala: prices, specs, deals | ![stars](https://img.shields.io/github/stars/sepehr071/masterkala-mcp?style=flat-square&label=%E2%98%85) |
| [shopino-mcp](https://github.com/sepehr071/shopino-mcp) | Fashion from thousands of Iranian shops: prices, sizes, stock, shop ratings | ![stars](https://img.shields.io/github/stars/sepehr071/shopino-mcp?style=flat-square&label=%E2%98%85) |
| [khanoumi-mcp](https://github.com/sepehr071/khanoumi-mcp) | Cosmetics, skin care and perfume on Khanoumi: prices, shades, reviews | ![stars](https://img.shields.io/github/stars/sepehr071/khanoumi-mcp?style=flat-square&label=%E2%98%85) |
| [asalbanoo-mcp](https://github.com/sepehr071/asalbanoo-mcp) | Cosmetics, skin and hair care on Asal Banoo: prices, variants, deals | ![stars](https://img.shields.io/github/stars/sepehr071/asalbanoo-mcp?style=flat-square&label=%E2%98%85) |
| **Travel** | | |
| [mrbilit-mcp](https://github.com/sepehr071/mrbilit-mcp) | Cheapest flights, trains, buses and hotels in Iran, with seats and refund rules | ![stars](https://img.shields.io/github/stars/sepehr071/mrbilit-mcp?style=flat-square&label=%E2%98%85) |
| [jabama-mcp](https://github.com/sepehr071/jabama-mcp) | Villas and stays with exact prices, group tours, events and theater tickets | ![stars](https://img.shields.io/github/stars/sepehr071/jabama-mcp?style=flat-square&label=%E2%98%85) |
| [otaghak-mcp](https://github.com/sepehr071/otaghak-mcp) | Villas and cottages on Otaghak: availability, exact prices, reviews | ![stars](https://img.shields.io/github/stars/sepehr071/otaghak-mcp?style=flat-square&label=%E2%98%85) |
| **Health** | | |
| [doctoreto-mcp](https://github.com/sepehr071/doctoreto-mcp) | Find doctors on Doctoreto: visit fees, free slots, reviews, clinics, labs | ![stars](https://img.shields.io/github/stars/sepehr071/doctoreto-mcp?style=flat-square&label=%E2%98%85) |
| [paziresh24-mcp](https://github.com/sepehr071/paziresh24-mcp) | Find doctors on Paziresh24: profiles, prices, reviews, free slots | ![stars](https://img.shields.io/github/stars/sepehr071/paziresh24-mcp?style=flat-square&label=%E2%98%85) |
| **Your own account** | | |
| [bale-mcp](https://github.com/sepehr071/bale-mcp) | Bale bots: read, search and answer messages, ask and wait for replies, send files | ![stars](https://img.shields.io/github/stars/sepehr071/bale-mcp?style=flat-square&label=%E2%98%85) |
| [payping-mcp](https://github.com/sepehr071/payping-mcp) | PayPing merchants: balance, sales, customers; create payment links, coupons, invoices | ![stars](https://img.shields.io/github/stars/sepehr071/payping-mcp?style=flat-square&label=%E2%98%85) |

<sub>Store, travel and health servers are unofficial and read-only. Bale and PayPing run locally with your own token.</sub>

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
<b><a href="https://github.com/sepehr071/dongeto">dongeto</a></b><br>
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
<tr>
<td width="33%" valign="top">
<a href="https://github.com/sepehr071/voice-chess-coach"><img src="https://raw.githubusercontent.com/sepehr071/voice-chess-coach/main/docs/images/hero.png" alt="Voice chess coach with a live board and bilingual transcript (demo data)" width="100%"></a><br>
<b><a href="https://github.com/sepehr071/voice-chess-coach">voice-chess-coach</a></b><br>
<sub>Play White by voice against a coach on a live board. <code>tool_choice="required"</code> + python-chess own the rules.</sub>
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

### 🕹️ Commit arcade

<!-- ARCADE:START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sepehr071/sepehr071/output/breakout-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sepehr071/sepehr071/output/breakout-contribution-graph.svg">
  <img alt="Breakout game animated over Sepehr's GitHub contribution graph: a ball bounces around breaking contribution-day bricks" src="https://raw.githubusercontent.com/sepehr071/sepehr071/output/breakout-contribution-graph.svg">
</picture>
<p><sub>My last year of commits as Breakout bricks, regenerated daily. <a href="https://abozanona.github.io/pacman-contribution-graph/">Play it yourself</a> · made with <a href="https://github.com/abozanona/pacman-contribution-graph">pacman-contribution-graph</a></sub></p>
<!-- ARCADE:END -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:06B6D4,100:4F46E5&height=90&section=footer" alt="" width="100%">
</p>
