# Capstone tools — shape, lane, build steps

Sorted from the Fall 2026 M2 submissions (34 tools, both sections), 2026-11-10. No students are named here because this repo is public. The per-student assignment lives in the course repo's gitignored `Major_Assignments/`.

Every tool starts from the same **skill folder**: `SKILL.md` (LEARNER · TASK · HOW YOU TALK) and `knowledge.md`. The shape decides what gets built from that folder. Gems and Custom GPTs close in Nov–Dec 2026, so neither one is a lane.

## The sorting question

**Who uses the tool, and do they type open answers?**

| Shape | This term | What it looks like | Lane | Who pays to run it |
|---|---:|---|---|---|
| **1 · Chatbot** | 17 | the learner types open answers; the tool asks, hints, judges | **A** if the student has an account · **B** (proxy) if not | the user's account (A) · grant credits (B) |
| **2 · Static page** | 10 | a fixed item set, checked answers, feedback messages written from the M3 block | build in **A** (simple) or **B/C** (hard) · runs on GitHub Pages | nobody, ever: AI is used once, at build |
| **3 · Teacher tool** | 7 | the teacher or professional uses it to generate handouts, activities, sorted posts, questions | **A** only | the teacher's own account |

**Steer toward static whenever answers can be checked.** It costs no tokens at run time, needs no account and lives on Pages permanently. That fits the grant record best.

## Build steps

### 1 · Chatbot
1. Fill in the skill folder (W3 adds HOW YOU TALK).
2. **Lane A:** in your own account, make a project and paste `SKILL.md` as its instructions. Upload `knowledge.md`.
3. Persona test, pasted as a transcript: one wrong answer, one off-topic turn, one refusal.
4. **Lane B (no account):** submit the folder. It runs through the course chat template + proxy on a capped cheap model.
5. Submit the folder plus a share link (A) or nothing extra (B).

### 2 · Static page
1. Fill in the skill folder.
2. Write a half-page spec: what is on screen, the items (from `knowledge.md`), what a right answer and a wrong answer each trigger (from HOW YOU TALK), and when it ends (STOP).
3. **Simple (Lane A):** paste the spec into any assistant that writes a page (Claude artifact, ChatGPT canvas, Gemini canvas). Ask for **one self-contained HTML file with no API key**, and download it.
   **Hard (Lane B/C):** a coding agent (Cline, Kilo Code, OpenCode, Aider, or Antigravity) with a capped OpenRouter key reads the folder and builds the page.
4. Open it in a browser and run the persona test against it.
5. Submit the HTML file in Canvas. Pages publishing is done by the instructor. Students need no GitHub account.

### 3 · Teacher tool
1. Fill in the skill folder. LEARNER is the teacher. HOW YOU TALK covers the student who receives the output.
2. Load it in your own account (same as Chatbot, Lane A).
3. Test with three real inputs. Check the length against your LIMIT and **verify every fact**.
4. Submit the folder plus three sample outputs. No deployment.

## What the instructor builds, by survey result

| Needed | When | Size |
|---|---|---|
| **Tools repo**: one folder per tool (`skill/`, `site/`, `card.md`) + a catalog page | always | small; a build script like `build_index.py` |
| **Pages upload of static HTML** | always (10 now) | mechanical; office-hours work |
| **Chat template + proxy** (holds the key, spend cap, model allowlist) | only if the survey shows chatbot students with no usable account | about a day, once |
| **OpenRouter keys, one per student, capped** | hard static builds (≈3) + any Lane B chatbot | setup clinic, office hours |
| **Opt-in consent** for the public catalog | before anything is listed with a name | one survey question |

## Thursday survey: the questions that decide the lane

1. Which AI accounts do you have? ChatGPT (free / paid) · Gemini (free / paid) · Claude (free / paid) · Copilot via MSU · none.
2. In that account, can you make a project and upload a file to it? Yes · No · Don't know. *(Ask them to check live, in the room.)*
3. Would you install VS Code and one extension to build your tool? Yes · No · Already use one.
4. May your finished tool appear in a public catalog? With my name · Without my name · No.

**Reading the result.** Q2 = "No" or "none" on Q1, among chatbot students → proxy needed, with that many seats. Q3 = "No" among hard-static students → those builds move to an office-hours clinic, or fall back to a chatbot. Q4 sets the catalog.

The free-tier limits named here change often. Check them the week the lanes are fixed.
