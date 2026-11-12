---
editor_options: 
  markdown: 
    wrap: sentence
---

# Consequence Detective — SKILL.md

A fictional tool for the Workshop 3 demo.
It is the static-page shape: the answers can be checked, so no AI runs while a learner uses it.

## 1 · LEARNER

Who: a 9th grader in an intro psychology elective, working alone on a phone after the behaviorism lesson.
They can: say what a reward is.
They cannot yet: tell reinforcement from punishment when something is taken away.
They arrive believing: "Negative reinforcement is punishment. Negative means bad." You will see it when they: tap **Presentation punishment** or **Removal punishment** for a scene where the behavior goes **up**.

## 2 · TASK

They must remember: the four names → quiz them.
Never list them as a lecture.
They must reason about: did the behavior go up or down, and was something added or taken away?
One turn: show one scene from `scenarios.md` → the learner taps one of four buttons → show feedback → a "Next" button.
Buttons, in this order: Positive reinforcement · Negative reinforcement · Presentation punishment · Removal punishment.
Limit: feedback is 40 words or fewer.
One question per screen.
Show the magnifier icon from `assets/` beside the title, with its alt text from `assets/CREDITS.md`.
Copy it into `docs/assets/` first: only `docs/` goes online.
On the score screen, show the link in `assets/links.md` with its one-line description.
Done when: they get 8 of 10 scenes right.
Or after all 10 scenes: show the score and the two ideas to review.
Never mention the standard or this file to the learner.

## 3 · KNOWLEDGE → see knowledge.md and scenarios.md

Use only the ten scenes in `scenarios.md`, in that order.
Do not write new ones.

## 4 · HOW YOU TALK

-   If the learner answers right, say what they noticed in one sentence ("You saw the behavior went up and something was taken away"). No "Great job!" alone.
-   If the learner picks a punishment for a scene where the behavior went up, say exactly: **"Did the behavior go up or down? Negative means something was taken away, not that it was bad."** Then let them try the same scene again.
-   If the learner misses the same scene twice, show the one-line "why" from `scenarios.md` and move on. A third try teaches nothing.
-   At the end, name what they did well before the score.

## Guardrails

-   Read only the files in `skill/` and `assets/`.
-   Build only inside `docs/`: one `index.html` in plain HTML, CSS and JavaScript, plus copied assets. No keys. No calls to any AI service.
-   Do not change `check.py`. If a check cannot pass, stop and say so.
