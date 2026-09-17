# AI Workshops

Four workshops on building learning tools with AI — what a language model is, how it
reasons, what an agent is, and how a tool is aligned, adapted and shipped. Each one is
delivered two ways from the same content: a slide deck for a live session and a
self-guided page for working alone. Both are hosted here on GitHub Pages.

The workshops currently carry the capstone of EPY 3143, *Human Development and Learning*
(Mississippi State University, Fall 2026), and the milestone references below are that
course's. From Spring 2027 they run as a stand-alone course. **This repo is the only
source for the workshops; the class links here and keeps no copy.**

| | In-person deck | Self-guided page | Status |
|---|---|---|---|
| **Workshop 1 — Introduction to AI co-creation** | [`w1/slides.html`](w1/slides.html) | [`w1/`](w1/) | ✅ |
| Workshop 2 — Reasoning structure | `w2/slides.html` | `w2/` | planned |
| Workshop 3 — Agents | `w3/slides.html` | `w3/` | planned |
| Workshop 4 — Alignment, adaptability, and the production line | `w4/slides.html` | `w4/` | planned |

The workshops are **detached from the milestones**: a milestone is written at home, after its
workshop, and the workshop gives the technical piece the milestone needs. The self-guided
pages carry no dates; deadlines live in Canvas.

## The spine

Each workshop teaches one idea about language models and pairs it with one idea about
learners. The four milestones are stations on a production line; Workshop 4 is where the
belt runs end to end.

| | Workshop 1 | Workshop 2 | Workshop 3 | Workshop 4 |
|---|---|---|---|---|
| Milestone | **M1** who / what | **M2** how it teaches | **M3** how it motivates | **M4** who it leaves out → **ship** |
| The LLM idea | prediction, not knowledge | chain-of-thought is a worked example; the context window is working memory; decomposition is chunking | an agent is a perceive → decide → act loop with memory — a self-regulation loop, and a feedback loop | system prompts, RLHF, guardrails: rules the tool is made to follow — and every rule set has a default learner it was written for |
| The learner idea | developmentally appropriate ≠ simpler-sounding | schema, not pattern; cognitive load lived | contingent, informational feedback; scaffolds that fade | aligned *to whom* — reading level, language, modality, attention |
| "Be the ___" | be the model | be the reasoner · overload me | be the agent (agent · learner · observer) | be the rulebook (write five rules; the next group breaks them) |
| Build block | the tool types | the system prompt as a worked example + a knowledge file | conditional feedback rules, persona-tested by a partner | red-team + accessibility audit → combine → deploy |
| Ships | — | **v0** — system prompt in a builder, one test question | **v1** — feedback rules added | **v2** — final, deployed |
| UnBlooms emphasis | the whole cycle | Generate & Verify | Critique & Judge | Refine & Decide → Create or Resist |

Every deck keeps the same seven blocks — the deal · watch · be the ___ · what this changes
for your tool · prompts, tested · staying the agent · exit card — so a new workshop is a
change of video, activity and prompts, not a new design.

## Lanes

Students build in one of three lanes. The default costs the instructor nothing.

| Lane | Who | Builds in | Overhead |
|---|---|---|---|
| **A · Provider account** (default) | anyone with a paid or student plan | the provider's own builder — Custom GPT, Gem, Claude Project — and its artifacts | none |
| **B · OpenRouter** | no account, or won't make one | an issued key with a spending cap, pointed at a chosen front end | credits + key handout, at a setup clinic in office hours |
| **C · Antigravity / Zoocode** | advanced, code track | agentic IDE → HTML or app → GitHub Pages | setup page, then none |

**The rule:** every lane ships v0 at Workshop 2 or it is not a lane. A student without a
running v0 by the end of Workshop 2 works in lane A for the semester. Lane B and C setup
is mechanical work — a self-guided setup page plus one office-hours clinic, never workshop time.

## Repository layout

```
w1/                 Workshop 1
  index.html        self-guided page — generated, runs in the browser
  build_index.py    the generator; edit it, run it, commit both
  slides.qmd        deck source (Quarto revealjs), speaker notes included
  slides.html       rendered deck
shared/             MSU theme and the reveal.js accessibility patch
index.html          landing page
```

Render a deck with `quarto render wN/slides.qmd`. Self-guided pages are single files built
by `wN/build_index.py`; everything a student types stays in their browser.

## Credits

- 3Blue1Brown, *Large Language Models explained briefly* — embedded in Workshop 1.
- Tina Austin, *UnBlooms™ — The Reflective Checkpoint Process* ([tinaaustin.com](https://tinaaustin.com/)); Austin, Gulya et al., *Metacognition as Disciplinary Infrastructure in AI-Mediated Learning*, IJEDIE 4(1). The cycle is redrawn in the course palette.
- Epistemic-friction design moves (Compare · Predict → Verify · Revise · Rubric) follow Li et al. (2026).
- Workshop design: Andy Parra-Martinez, Ph.D. Pages drafted with Claude (Anthropic) and reviewed by the instructor.
