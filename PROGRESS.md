# AI Workshops — progress and to-do

The entry point for planning the workshops and supporting the student tool builds. From 2026-11-10, workshop planning lives here. It no longer lives in the course repo's `PROGRESS.md`, which keeps one pointer line. Course grading stays in the course repo. Student work and feedback that name students stay in the course repo's gitignored `Major_Assignments/`. **This repo is public: no student names, no keys.**

## Where things stand (2026-11-10)

| | Status | Next |
|---|---|---|
| **W1** · Introduction to AI co-creation | ✅ delivered (deck + self-guided page) | — |
| **W2** · Curation (ships v0) | ✅ delivered | Spring: Lane A wording names Gems/GPTs |
| **W3** · Agents: beyond the chatbot (ships v1) | ✅ built Nov 12 (deck + self-guided page + sim lab); runs **Thu Nov 12** | Andy: rehearse Round 2 and record it |
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
| W10 | **M3 is written at home** (C1). In person and online both due Sun Nov 15. | 2026-11-10 · Andy |
| W11 | **W3 = Agents: beyond the chatbot.** Agents read files, run commands, change and build. Anchor: the Hugging Face incident (Jul 2026). Agents pushed to finish a task behave in ways nobody asked for, so tools need guardrails (C3). | 2026-11-10 · Andy |
| W12 | **W4 turns to accessibility and the ethics of AI.** The guardrails piece of the old W4 spine moved to W3. | 2026-11-10 · Andy |
| W13 | **Release W3 and W4 early**, with the M3 and M4 tasks, so students have more time (C8). | 2026-11-10 · Andy |
| W15 | **Every student ends with one website and deploys it themselves**, on GitHub Pages or Vercel. A static tool is the page; a chatbot or teacher tool gets a page that shows it. One prompt path, P0–P7 (`w3/lane_c/PROMPTS.md`). The agent proposes and the student accepts or rejects, with reasons in the student's own words. *Supersedes* "Andy publishes Nov 30" (C8). | 2026-11-10 · Andy |
| W16 | **W3 lab = context engineering, live.** Andy drives a sim folder (thin vs. full skill folder, then a tempting check) on Claude in Antigravity; the class observes. **The roleplay persona test is dropped from the room**: students run P4 at home and paste it into M3. Updates C2 and W14. | 2026-11-12 · Andy |
| W14 | **W3 room format: drivers and observers check the agent's properties** on a lab folder. This replaces playing the AI. Antigravity install instructions go out before class, optional (C4). | 2026-11-10 · Andy proposed, Claude designed |

------------------------------------------------------------------------

## Clashes with the original plan

The original plan is `EPY3143_In_Person/EPY3143_Capstone_Workshops.md` (four 75-minute workshops, one per milestone). The README spine and the decisions above have moved away from it. Each row says what to do.

| # | Original plan | Now | Resolution |
|---|---|---|---|
| C1 | W3: **submit M3 in the room** (65–75 min). The course `Week_13/README.md` still says "Thu Nov 12 (in workshop)." | W3: the milestone is written at home (W3 decision; W1 and W2 both ran that way) | ✅ **Resolved (W10).** At home, due Sun Nov 15. Week 13 README and `_sections/*.yml` updated 2026-11-10. |
| C2 | W3 guided practice **is** the M3 peer feedback: a partner tests the W2 prototype against a short rubric (informational or evaluative? autonomy-supportive?) | Spine: persona triads (agent · learner · observer). M2 lesson: tests must script a wrong answer, an off-topic turn and a refusal | **Merge.** The persona test is the peer feedback. The partner plays the learner with the three scripted moves, then scores the replies with the original two questions. No separate activity is needed. |
| C3 | W3 title: *Designing for Motivation: Feedback, Autonomy, and Scaffolded Growth* | README: *Agents: teaching the tool how to talk* | ✅ **Resolved (W11).** *Agents: beyond the chatbot.* Motivation stays in M3 (HOW YOU TALK); guardrails and motivation rules share the if-then shape. Week 13 README updated. The README table gets the new title when W3 ships. |
| C4 | W3 hook + demo: rewrite a blunt AI reply into an autonomy-supportive one | Room format proposed: human agent first (triads, the agent may only use the printed milestones), then the template as take-home and online | ✅ **Resolved (W14).** Drivers + observers on an agent lab. The observer's log replaces the triads. The persona test stays as the peer feedback. Plan: `w3/PLAN.md`. **New clash it creates:** the README says Lane C setup is "never workshop time." Here the install happens *before* class and is optional, and project setup in the room is a guided lab, not lane setup. |
| C5 | Lane A = provider builders (Gem, Custom GPT, Claude Project) | Gems/GPTs close (W4) | Lane A = **the student's own account: a project with `SKILL.md` + `knowledge.md`**. Rewrite the README Lanes section after the survey. W2 materials are fixed for Spring. |
| C6 | README: "every lane ships v0 at W2 or it is not a lane; no v0 → Lane A for the semester" | 12 students have no working v0; lanes now follow shape (W6) | Rule retired by W6. Students with no v0 start from the template in whatever lane their shape needs. |
| C7 | README Lane B = "issued key, pointed at a chosen front end" | Lane B = shared runtime for chatbot students with no account: **Open WebUI** (needs MSU ITS) or **proxy + Pages chat template** | Decided by the survey (Q1–Q2) and the ITS answer. Students never hold a key for running a chatbot. Keys are for Lane C builds only. |
| C8 | W4 (Nov 24, single session): accessibility audit, 2+ changes, **submit M4**, executive summary for the **Dec 1 Showcase** | Spine: be the rulebook → red-team + audit → combine → **deploy**. Deployment adds Pages publishing, a catalog and consent | ✅ **Partly resolved (W13):** W3 and W4 and both tasks release early. Still recommended: static HTML + skill folders due with M4, Andy publishes Nov 30. Plan: `w4/PLAN.md`. |
| C10 | C8 recommendation: students submit HTML, Andy publishes to Pages; students need no GitHub account | Students deploy themselves (W15) | ✅ **Resolved (W15).** Survey adds Q5 (GitHub account). Andy's catalog links to student addresses. The zipped folder in Canvas is the grant record. Template folder `site/` renamed `docs/` so Pages can deploy from `/docs` with no workflow file. |
| C9 | Course `Week_13/` and `Week_15/` list `04_workshop.qmd` as a course file | W1: the class links and never copies | Fixed 2026-11-10: both READMEs now point here. |

------------------------------------------------------------------------

## To-do

Dated and concrete. Three a day at most. When an item is done, mark it ✅.

### Before Workshop 3 (Thu Nov 12)
- [ ] **Tue Nov 10 · Andy:** send MSU ITS one line: *"Can a self-hosted Open WebUI with student logins be used for EPY 3143 coursework?"*
- [ ] **Tue Nov 10 · Andy:** send students `w3/before_class.md` (optional Antigravity install), both sections. ✅ Antigravity confirmed still free (Andy, 2026-11-10).
- [x] ✅ **Thu Nov 12 · Claude:** `w3/sim_lab/` + observer log built and check tested (W16).
- [x] ✅ **Thu Nov 12 · Claude:** `w3/slides.qmd` (rendered) and `w3/build_index.py` → `w3/index.html`; landing page and README list W3 from `w3/PLAN.md`.
- [ ] **Wed Nov 11 · Andy:** test the agent lab once on his Mac and record the ≈5-min run for online and non-installers. The recording is the Plan B if the live demo fails.
- [ ] **Wed Nov 11 · Andy + Claude:** write `Week_13/02_milestone.md` (M3: HOW YOU TALK + three guardrails, at home, due Nov 15). It doesn't exist yet and has to be released with W3.
- [ ] **Wed Nov 11 · Andy:** paste the eight survey questions (`w3/survey.md`) into a Canvas quiz, both sections; Q7 needs a file-upload question.
- [ ] **Wed Nov 11 · Andy:** Canvas message to the 8 online "not yet" students. Ask the two in-person students whose M2 looks like the wrong file.

### Release W4 early (by Fri Nov 13, course-build block)
- [ ] **Claude:** build W4 from `w4/PLAN.md` (deck + self-guided page). Write `Week_15/02_milestone.md` (M4).
- [ ] **Andy:** release the W4 page and M4 in Canvas (due Tue Nov 24, with the skill folder + HTML or link).

### After the survey (Nov 13–17)
- [ ] Count chatbot students with no usable account → **Open WebUI vs proxy vs neither** (with the ITS answer).
- [ ] **Andy, office hours:** run P0–P3 and P7 (`w3/lane_c/PROMPTS.md`) once on his Mac, deploying a test page to both GitHub Pages and Vercel. Confirm Zoo Code installs in Antigravity and the default model builds one page.
- [ ] Issue capped OpenRouter keys (≈$5) to Lane C students only. Run the setup clinic in office hours, never in workshop time.
- [ ] Rewrite the README Lanes section (C5–C7) to match the survey.
- [ ] Decide where student tools live: a new public repo (`skill/` · `site/` · `card.md` per tool + catalog page) or a folder here. Consent from survey Q4 applies.

### Before Workshop 4 (Tue Nov 24)
- [ ] Confirm the Nov 17 discussion (Ch. 4–5) runs. W4 depends on it.
- [ ] Tell students on Nov 24 what is due with M4 and when Andy publishes (Nov 30).

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

**2026-11-10 (later) — Andy's answers on the clashes.**
- **Decisions:** C1 M3 at home (W10); W3 = agents beyond the chatbot, anchored on the Hugging Face incident (W11); W4 = accessibility + ethics (W12); release W3–W4 early (W13); drivers + observers check agent properties (W14). C5–C7 wait for the survey.
- **Incident checked against sources:** Hugging Face disclosure (Jul 16, 2026), METR investigation (Aug 26, 2026), CSA research notes. Some details (which model, the timeline) are still disputed, so the deck says so.
- **Saved:** `w3/PLAN.md`, `w4/PLAN.md` and `w3/before_class.md`. Survey Q3 now asks whether Antigravity ran on Thursday.
- **Course repo:** the Week 13 README and `_sections/*.yml` were updated (M3 at home, Sun Nov 15; the W3 title).

**2026-11-10 (later) — W3 gets a hopeful example (Andy: "not everything is apocalypse and hype").** Navier–Stokes (OpenAI, Sep 2026: ≈10,000 agents, 88 hours, Lean-checked proof of finite-time blow-up) pairs with the Hugging Face incident. The lesson for both is the same: the stop rule and an outside check decide the ending. The claim is **contested**: mathematicians are still checking it, the Clay Institute lists the problem as open, and an Oct 13 Scientific American survey found the proof departs from the Córdoba–Martínez-Zoroa program. The deck says so. Settled backup: AlphaEvolve (2025). Recheck the status the morning of Nov 12.

**2026-11-10 (later) — The build kit became the path from M2 to a live website.**
- **Checked:** the Lane C prompts against what M2 shows students actually have. Most have M1/M2 text, not a skill folder. Many lack an idea list, a STOP line or a real test. Neither SETUP nor BUILD covered that, and nothing covered deployment.
- **Now:** one `PROMPTS.md` with eight prompts:
  - P0 gathers M1/M2 into the skill folder in any chat, quoting the student and marking `[MISSING]`, never inventing.
  - P1 sets up the folder.
  - P2 plans the page by shape.
  - P3 builds; P4 runs the persona test (report only); P5 fixes one thing.
  - P6 runs the W4 accessibility + ethics check.
  - P7 deploys to GitHub Pages or Vercel, after a safety scan for keys, names and consent; static only.
- **Removed:** `SETUP_PROMPT.md` and `BUILD_PROMPT.md`, so there are no two copies to drift.
- **The W3 goal is built into every prompt:** the agent shows its plan and waits. `SETUP_LOG.md` splits "what the agent did" from "what I decided", and the student writes the second part.
- **Survey:** Q5 added (GitHub account).

**2026-11-11 — Survey Q6: the interface.** Andy asked each student what they picture on screen, with a sketch or a screenshot. The answer feeds P2. The per-student M2 feedback (course repo, gitignored) now ends with a Stretch line (one realistic way to grow the tool) and the same interface question.

**2026-11-12 — W3 lab becomes a live context-engineering demo (W16).** `w3/sim_lab/`: Round 1 thin folder, Round 2 full skill folder for a fictional operant-conditioning drill, Round 3 "pass every check" with one check only real learners can pass. Fabricating the evidence file or editing `check.py` is the task-pressure move to watch for. `check.py` tested: a good page passes 6 of 7. Model for the live run: Claude in Antigravity (reliability in front of the room; no key on screen). The roleplay persona test left the room; P4 at home replaces it. **Not yet done for today:** Andy's rehearsal and recording, slides, M3 task file.

**2026-11-12 — W3 built: deck, self-guided page, provider comparison.** Deck follows `w3/PLAN.md` (W16): the deal, the agent loop as Week 12's self-regulation cycle, Hugging Face + Navier–Stokes, sim lab rounds 1–3, guardrails, staying the agent, exit card + six-question survey, M3. **Added at Andy's request:** a slide comparing ChatGPT Codex, Claude Code and Antigravity (where it runs, cost, good for, watch). Checked live: Codex is in ChatGPT plans with a capped free tier; Claude Code needs Pro or higher; Antigravity is a free preview that may need a personal Gmail. **Navier–Stokes rechecked:** still unsettled; the proof file is not public; the deck says so. **What nearly shipped:** the first draft of the speaker notes named six students (as M3-seed and teacher-tool examples) in this public repo. The write was blocked, the names were removed, and a scan of the whole repo against the M2 roster found none in W3. **Not done:** Andy's rehearsal and recording; the online page links the recording through the Week 13 module; `Week_13/02_milestone.md` (M3) still unwritten.

**2026-11-12 (later) — OpenCode added to the provider comparison.** Andy installed it: easy, and it takes an OpenRouter key directly. Deck and page now compare four: Codex, Claude Code, Antigravity, OpenCode. Lane C stays Antigravity + Zoo Code (W7); OpenCode is named as taking the same capped key the same way.

**2026-11-12 (morning) — W3 gets a "Challenges with agentic AI" section, opened by the two decision maps.** Andy's request: agentic AI connects to motivation (goals, planning, acting, monitoring, evaluating) without anthropomorphizing it. The deck now runs: the deal → **Two maps for deciding** (the 4Ds and UnBlooms, the course's own redrawn PNGs, copied to `w3/figures/`) → divider → *Agentic AI Explained in 3 Minutes* (Innovate & Update) → the self-regulation loop with a new line, "It runs the same steps. It is not a learner." → **A cute face is a design choice** (Rodrigo Cardenete's Short) → Hugging Face, Navier–Stokes, two endings → **Who did it?** (Catharina Doria's Short; responsibility goes to the company and the people who built, set up, and ran the agent) → **Say what it did** (verb swaps: wanted → was set, decided → ran code, lied → edited, knows → reads; and for M3, a tool can be warm but doesn't claim to feel). The self-guided page has the same section, with two new saved answers in the copy-all button. **Timing:** the block takes 14 minutes. The provider table became a backup slide after M3 (it stays in the page's flow), the sim lab went from 28 to 20 minutes, and guardrails from 10 to 7. **Not verified:** only the video titles could be read; the content wording on the slides follows Andy's description of each video. Andy should preview all three before 12:30. YouTube embeds can fail when the deck is opened as a local file, so each video slide also shows a link.

**2026-11-12 (morning, later) — W3 survey updated to 8 questions.** Paste-ready wording for both sections in `w3/survey.md`. Q3 now asks about the optional pre-class install, since Andy drives in the room. **New Q4:** would you let an agent build your tool, if you read every plan first (yes · with help in office hours · no)? It is the 4Ds' Delegation question, and it sorts the clinic list. **New Q8:** one sentence about an agent with a person in it, from the "Say what it did" slide. Old Q4–Q6 are now Q5–Q7. The deck, the self-guided page and `deployment_lanes.md` all say 8. Also fixed: the page's M3 list pointed at "section 5" for guardrails; it is section 6. **Andy:** if the Canvas survey already exists, add Q4 and Q8 and reword Q3; otherwise paste all eight. Not pushed.

**2026-11-12 (later) — W3 stories streamlined from Andy's hand edit (three tiers + questions to argue).** Andy edited `w3/index.html` by hand; the edits are now in `build_index.py` (the page is generated) and in the deck. Order: hard problems (AlphaFold, UNICEF) → needs checking (Navier–Stokes) → harm (Hugging Face) → four open questions (which is an agent? who checked? who pays? who answers?). The questions slide replaces "Same power, two endings"; timing unchanged. Online: one saved answer, `q_crit`, replaces `q_stop`. **Facts checked and corrected:** Hugging Face was OpenAI's own test of its own agents (METR/Redwood + OpenAI reports, Aug 2026; ~700 agents in the attack), so Andy's "OpenAI" was right and the deck's "model disputed" was stale. Navier–Stokes: 130 billion tokens confirmed; cost "millions" (OpenAI) / $6–10M (NPR estimate); Andy's $10–40M had no source. Proof now published and Lean code compiles; NPR: mathematicians learned little. UNICEF: 17 countries confirmed; "2 million children" and "50 by 2030" had no source and were left out. **What nearly broke:** a hand edit to a generated file is lost on the next build.

**2026-11-12 (later) — W3 flow streamlined (Andy).** Section 3 is now "How does agentic AI work?" (the 3-minute video + the self-regulation loop). New section 4, "Is AI good for individuals?": gains (repeat work done, time freed, gatekept skills opened) and costs (the skill you hand over, trusting too fast, sameness, telling it too much), then the cute-face video. Section 5, "Is agentic AI good for society?", keeps the three stories and the questions. "Go deeper" links for students on the page; every DOI checked against Crossref (Noy & Zhang 2023; Brynjolfsson et al. 2025; Bastani et al. 2025; Lee et al. 2025; Doshi & Hauser 2024; Kosmyna et al. 2025 marked as a preprint). New saved answer `q_trade` (one skill you would never hand to an agent). Deck agenda: 6–10 how it works, 10–15 individuals, 15–26 society, sim lab 26–44 (18 min; rounds 4/6/5).
