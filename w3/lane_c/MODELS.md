# Models for Lane C builds (OpenRouter)

Checked against OpenRouter's live model list on **2026-11-10**. Prices are per million tokens, input / output. All of them support tool calling, which a coding agent needs. Prices and names change, so check again before each cohort.

| Use | Model ID | In / Out | Why |
|---|---|---|---|
| **Default** | `deepseek/deepseek-v4.1-flash-1017` | $0.01 / $0.50 | cheapest strong option; a pinned snapshot, so it won't change mid-build |
| **Can see screenshots** | `qwen/qwen3.8-flash` | $0.15 / $0.47 | multimodal: paste a screenshot of what looks wrong |
| **Lowest cost** | `z-ai/glm-5.3-flash` | $0.04 / $0.08 | built for coding agents; try it first on small changes |
| **When stuck** | `qwen/qwen3-coder-next` | $0.12 / $0.80 | coding-specialised; switch for one hard fix, then switch back |

**Avoid:**
- IDs that start with `~` or end in `-latest`. They point at whatever is newest, so the model changes under you.
- IDs that end in `:batch`. Those are for offline jobs, not a live agent.
- Anything priced over $1 input or $5 output, unless the instructor says so.

**What a build costs (estimate).** A coding agent re-sends the project with every step, so input tokens dominate. A full build of one page is roughly 1–3 million input tokens: well under $1 on the default model. A $5 cap per student leaves room for mistakes.

**Data.** Some of these models are served by their makers. Put no student names or real student work in the folder. In OpenRouter's privacy settings, turn off providers that may train on your inputs.

**Instructor:** confirm the default on one real build (the keyboard or the cell simulation) before handing this out. The prices are verified. Quality on our tasks is not yet.
