# AI Workshops — progress and to-do

The entry point for planning the workshops and supporting the student tool builds. From 2026-11-10, workshop planning lives here. It no longer lives in the course repo's `PROGRESS.md`, which keeps one pointer line. Course grading stays in the course repo. Student work and feedback that name students stay in the course repo's gitignored `Major_Assignments/`. **This repo is public: no student names, no keys.**

## Where things stand (2026-11-10)

| | Status | Next |
|---|---|---|
| **W1** · Introduction to AI co-creation | ✅ delivered (deck + self-guided page) | — |
| **W2** · Curation (ships v0) | ✅ delivered | Spring: Lane A wording names Gems/GPTs |
| **W3** · Agents / motivation (ships v1) | ⚠ **not built**; runs **Thu Nov 12** | design inputs ready: `w3/design_inputs.md` |
| **W4** · Alignment & production line (ships v2) | ☐ not started; runs **Tue Nov 24** (single session) | depends on the survey and on the Nov 17 discussion |
| **Tool deployment** | planned: `w3/deployment_lanes.md` · Lane C kit `w3/lane_c/` | Thursday survey decides the lanes |

**Where the students are (M2, both sections, 34):** 7 ready to add M3, 15 need one fix, 12 have no working v0. Shapes: 17 chatbots · 10 static pages · 7 teacher tools. Per-student detail: course repo, `Major_Assignments/Milestones/` (gitignored).

------------------------------------------------------------------------

## Decisions

A logged decision is not reopened. W-numbers are this repo's. Decisions inherited from the course repo keep their date and source.

| # | Decision | Date · source |
|---|---|---|
| W1 | Workshops are a separate product. This repo is the only source; the class links and never copies. Stand-alone course from Spring 2027. | 2026-09-17 · Andy (course PROGRESS) |
| W2 | Production line: v0 (W2) → v1 (W3) → v2 (W4). W2 = curation, W3 = agents + feedback rules in C.A.R.E. language, persona-tested. W4 = alignment, adaptability, ship. | 2026-09-17 · Andy |
| W3 | A workshop is 60 min of workshop ending on an exit card. **The milestone is written at home**, after the workshop. Self-guided pages carry no dates. | 2026-09-17 · Andy (W1, kept for W2) |
| W4 | **Skills-first.** Gems and Custom GPTs close (Nov 17 / Dec 2026). Every tool is one skill folder (`SKILL.md` + `knowledge.md`), the single source for every output. | 2026-11-08 · Andy |
| W5 | **Grant: tools hosted in a repo / GitHub Pages where possible.** Build credits on OpenRouter. **No key in any public page.** | 2026-11-08 · Andy |
| W6 | **The lane follows the tool's shape**: chatbot → own account (A) or shared runtime (B); static page → built once, runs free on Pages; teacher tool → own account only. *Replaces* the README rule "no v0 by W2 → Lane A for the semester." | 2026-11-10 · Andy approved the sort |
| W7 | **Lane C = Antigravity + Zoo Code**, one self-contained project folder. Antigravity's agent sets up; Zoo Code builds on a capped OpenRouter key kept in its settings. Kit: `w3/lane_c/`. | 2026-11-10 · Andy |
| W8 | **bolt.diy is a backup builder only**, never a chatbot runtime (one app + one key per student is unsafe and unmaintainable). | 2026-11-10 · Andy considered; recorded |
| W9 | **Lanes are not fixed until the Thursday survey.** | 2026-11-10 · Andy |

------------------------------------------------------------------------

## Clashes with the original plan

The original plan is `EPY3143_In_Person/EPY3143_Capstone_Workshops.md` (four 75-minute workshops, one per milestone). The README spine and the decisions above have moved away from it. Each row says what to do.

| # | Original plan | Now | Resolution |
|---|---|---|---|
| C1 | W3: **submit M3 in the room** (65–75 min). The course `Week_13/README.md` still says "Thu Nov 12 (in workshop)." | W3: the milestone is written at home (W3 decision; W1 and W2 both ran that way) | **Andy decides by Wed Nov 11.** Recommended: at home, due with online (Nov 15). Then fix the Week 13 README and `_sections/*.yml` (`milestone: "day of the capstone workshop"`, open since Sep 17). |
| C2 | W3 guided practice **is** the M3 peer feedback: a partner tests the W2 prototype against a short rubric (informational or evaluative? autonomy-supportive?) | Spine: persona triads (agent · learner · observer). M2 lesson: tests must script a wrong answer, an off-topic turn and a refusal | **Merge.** The persona test is the peer feedback. The partner plays the learner with the three scripted moves, then scores the replies with the original two questions. No separate activity is needed. |
| C3 | W3 title: *Designing for Motivation: Feedback, Autonomy, and Scaffolded Growth* | README: *Agents: teaching the tool how to talk* | Compatible content. The motivation is what goes in the HOW YOU TALK block, and the agent loop is the LLM idea. **Andy picks one title**; the Week 13 README and the README table then match it. |
| C4 | W3 hook + demo: rewrite a blunt AI reply into an autonomy-supportive one | Room format proposed: human agent first (triads, the agent may only use the printed milestones), then the template as take-home and online | **Andy confirms the format.** Both fit in 75 minutes if the demo is 5 minutes: the rewrite *is* the agent's first move. |
| C5 | Lane A = provider builders (Gem, Custom GPT, Claude Project) | Gems/GPTs close (W4) | Lane A = **the student's own account: a project with `SKILL.md` + `knowledge.md`**. Rewrite the README Lanes section after the survey. W2 materials are fixed for Spring. |
| C6 | README: "every lane ships v0 at W2 or it is not a lane; no v0 → Lane A for the semester" | 12 students have no working v0; lanes now follow shape (W6) | Rule retired by W6. Students with no v0 start from the template in whatever lane their shape needs. |
| C7 | README Lane B = "issued key, pointed at a chosen front end" | Lane B = shared runtime for chatbot students with no account: **Open WebUI** (needs MSU ITS) or **proxy + Pages chat template** | Decided by the survey (Q1–Q2) and the ITS answer. Students never hold a key for running a chatbot. Keys are for Lane C builds only. |
| C8 | W4 (Nov 24, single session): accessibility audit, 2+ changes, **submit M4**, executive summary for the **Dec 1 Showcase** | Spine: be the rulebook → red-team + audit → combine → **deploy**. Deployment adds Pages publishing, a catalog and consent | **The deploy can't happen in the room or over Thanksgiving week.** Recommended: static HTML and skill folders are due with M4 (Nov 24). Andy publishes Nov 30. The Showcase uses own-account links for chatbots, Pages links for static tools. |
| C9 | Course `Week_13/` and `Week_15/` list `04_workshop.qmd` as a course file | W1: the class links and never copies | Fixed 2026-11-10: both READMEs now point here. |

------------------------------------------------------------------------

## To-do

Dated and concrete. Three a day at most. When an item is done, mark it ✅.

### Before Workshop 3 (Thu Nov 12)
- [ ] **Tue Nov 10 · Andy:** send MSU ITS one line: *"Can a self-hosted Open WebUI with student logins be used for EPY 3143 coursework?"*
- [ ] **Wed Nov 11 · Andy:** decide C1 (M3 at home?), C3 (title) and C4 (room format). Each is a one-word answer.
- [ ] **Wed Nov 11 · Claude, after those answers:** build W3: `w3/slides.qmd` + `w3/build_index.py` (self-guided online page) from `w3/design_inputs.md`, with the four-block template as a downloadable `SKILL.md` and the survey link. Seven blocks as always.
- [ ] **Wed Nov 11 · Andy:** paste the four survey questions (`w3/deployment_lanes.md`) into a Canvas quiz, for both sections.
- [ ] **Wed Nov 11 · Andy:** Canvas message to the 8 online "not yet" students (M2 has no prompt; online M3 due Nov 15).
- [ ] **Wed Nov 11 · Andy:** ask the two in-person students whose M2 looks like the wrong file.

### After the survey (Nov 13–17)
- [ ] Count chatbot students with no usable account → **Open WebUI vs proxy vs neither** (with the ITS answer).
- [ ] **Andy, office hours:** run the Lane C setup prompt once on his Mac. Confirm Zoo Code installs in Antigravity and the default model builds one page.
- [ ] Issue capped OpenRouter keys (≈$5) to Lane C students only. Run the setup clinic in office hours, never in workshop time.
- [ ] Rewrite the README Lanes section (C5–C7) to match the survey.
- [ ] Decide where student tools live: a new public repo (`skill/` · `site/` · `card.md` per tool + catalog page) or a folder here. Consent from survey Q4 applies.

### Before Workshop 4 (Tue Nov 24)
- [ ] Confirm the Nov 17 discussion (Ch. 4–5) runs. W4 depends on it.
- [ ] Build W4: the accessibility audit (original plan) + "be the rulebook" (spine) + the M4 block in `SKILL.md` ("who it leaves out"). Hand-in = skill folder + HTML (static) or share link (chatbot).
- [ ] Decide C8 (deploy timing) and tell students on Nov 24 what is due, and when.

### Showcase (Dec 1)
- [ ] **Nov 30 · Andy:** publish the static tools to Pages and the catalog (consenting students only).
- [ ] Defense material: the prompt log + `SETUP_LOG.md` + the before/after rewrites from W3.

### Spring 2027 (stand-alone course)
- [ ] W2 materials: Lane A wording, the template as a file from day one, a real test transcript required.
- [ ] **Build two weeks ahead**: W3 was built two days out this term.

------------------------------------------------------------------------

## Log

**2026-11-10 — M2 read for build readiness; deployment planned (Andy + Claude).**
- **Read:** both sections' M2 (34). Andy asked about prompt quality and readiness to build, not scores.
- **Main finding:** students tested only the easy path. The persona test must script a wrong answer, an off-topic turn and a refusal.
- **Online:** the template didn't reach most students, two tests were imagined, and four students resubmitted M1.
- **Saved:** design inputs → `w3/design_inputs.md`; shape/lane/build steps + survey → `w3/deployment_lanes.md`; Lane C kit with the model shortlist (checked live on OpenRouter) → `w3/lane_c/`.
- **Weighed:**
  - Open WebUI: good for the class, poor for a public catalog; needs MSU ITS approval.
  - bolt.diy: a builder only (W8).
  - The bolt.diy video: dated early 2025; its synth-keyboard demo is the closest match to the hardest music tool.
- **What nearly shipped** (course repo): 17 student .docx files sat in an unignored folder. They are gitignored now.
- **What broke:** W3 is being built two days out, against the build-two-weeks-ahead rule.
