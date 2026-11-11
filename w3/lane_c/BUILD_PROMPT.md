# Build prompt — paste into Zoo Code (fill in the blanks first)

Read `skill/SKILL.md` and `skill/knowledge.md`. They are the rules and the content for a teaching tool. Build that tool as a web page.

**What it is:** [one sentence, e.g. "a treble staff that shows one note; the learner taps its name"]

**On screen:** [what the learner sees first]

**A right answer does:** [from HOW YOU TALK]
**A wrong answer does:** [from HOW YOU TALK: a hint first, then one worked step]
**It ends when:** [the STOP line]

Rules for the build:
- Write the tool into `site/index.html`. One file, plain HTML, CSS and JavaScript. No build step. A library from a CDN is fine.
- **No API keys and no calls to an AI service.** The page must work with no internet AI.
- Use only the content in `knowledge.md`. Do not add facts.
- Readable on a phone. Text large enough for the learner in LEARNER.
- After you build, tell me how to open it, and stop. Wait for my test before changing anything.
- Add one line to `SETUP_LOG.md` for each change you make.
