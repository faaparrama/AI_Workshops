# Prompts: from your M2 to a live website

Eight prompts, in order. Each one does one job. Paste one, read what comes back, decide, then move on.

## You are in charge

The agent suggests. You decide. Every prompt below makes the agent **show you its plan and wait**. These rules hold for all eight:

- **Read before you approve.** If you can't explain a command or a change, ask the agent to explain it in one sentence. Approve only after that.
- **Say no out loud.** "No, keep my wording." "No, don't install that." A no is a decision, and decisions are what you defend in December.
- **Log your decisions yourself.** `SETUP_LOG.md` has two parts. The agent writes *what it did*. **You** write *what you accepted or rejected, and why*. A reason the agent wrote for you is a reason you didn't make.
- **Never paste a password, token or key into the chat.** When something needs a login, you log in yourself, in the browser.
- **Keep the agent on "ask before running commands."**

**Where each prompt runs.** P0 works in any AI chat (ChatGPT, Gemini, Claude). P1–P7 need an agent that can open your folder: Antigravity's own agent, or Zoo Code.

------------------------------------------------------------------------

## P0 · Gather: turn your M1 and M2 into the skill folder

*Any AI chat. Paste the prompt, then paste your M1 and M2 text below it.*

```
Below are my M1 and M2 for a teaching tool. Sort my own words into
four blocks. Do not invent anything.

1 LEARNER: who · they can / cannot yet · what they arrive believing ·
  what I will see when they hold that belief
2 TASK: what they must remember (quiz it) · what they must reason
  about (question, hint, one step) · one turn in order · word limit ·
  done when (one observable thing) · number of turns
3 KNOWLEDGE: the standard, quoted with its source · 4–6 ideas in order,
  each written as a sentence a learner could get wrong · sources ·
  off limits
4 HOW YOU TALK: leave empty (that is M3)

Rules:
- Quote or lightly trim my words. Never add content I did not write.
- Where something is missing, write [MISSING: what is needed].
- If an "idea" is a heading or a tool action, flag it: [REWRITE AS AN IDEA].
- If my misconception is about value or effort ("this is boring",
  "we don't need this"), move it to block 4 and say so.
- Then ask me up to five questions, one per gap, most important first.
Do not write my answers for me.
```

Then answer the questions yourself. Copy blocks 1, 2 and 4 into `skill/SKILL.md` and block 3 into `skill/knowledge.md`.

------------------------------------------------------------------------

## P1 · Set up the folder

*Antigravity's agent. Open your project folder first (File → Open Folder).*

```
Set up this folder for a student's teaching tool. I am a future
teacher, not a programmer. Keep everything inside this folder.

First, show me your plan as a numbered list and wait for my OK.
Then:
1. Check for skill/, docs/, SETUP_LOG.md, card.md and .gitignore.
   Create any that are missing. Do not change anything in skill/.
2. Check whether git is installed. If it is, run git init and make a
   first commit. If git asks for my name and email, ask me and set
   them for this folder only.
3. Check for Python 3 (python3, or python / py on Windows). If it is
   there, make a virtual environment in .venv/ inside this folder.
   If it is not, tell me in two sentences how to install it, and wait.
4. Give me one command that previews docs/ in my browser. Run it once,
   show me it works, then stop it.
5. In SETUP_LOG.md under "What the agent did", write each command
   you ran and why, one line each, in plain words.

Rules: ask before installing anything outside this folder. Never use
sudo or ask for an admin password without explaining first. Never write
a key, password or token into any file. Do not build the tool.
Finish with what is installed and my next step, in five lines or fewer.
```

------------------------------------------------------------------------

## P2 · Plan the page

*Antigravity's agent or Zoo Code.* Every tool ends as **one website**. What the page holds depends on your tool's shape:

- **Static tool** (practice, simulation, quiz): the tool itself, then *About this tool* below it.
- **Chatbot or teacher tool:** a page that shows the tool. It has what the tool does, who it is for, how to use it (your share link, or "load this skill folder into your own AI"), one **real** test transcript, and *About this tool*.

```
Read skill/SKILL.md and skill/knowledge.md. My tool's shape is
[static tool / chatbot / teacher tool].

Propose the plan for one web page, docs/index.html. Do not build yet.
- Static tool: what the learner sees first; each item, taken only from
  knowledge.md; what a right answer does and what a wrong answer does
  (from HOW YOU TALK); when it ends (the "done when" line).
- Chatbot or teacher tool: the sections of a page that presents the
  tool, as described above.
- Every page ends with "About this tool": who it is for, the standard,
  what it teaches, how it talks, its guardrails, who it may leave out,
  "Built with AI: [model]", and the author (or "withheld").

Show the plan as a short outline. List anything SKILL.md does not
answer as a question for me. Wait for my changes.
```

------------------------------------------------------------------------

## P3 · Build

*Zoo Code, on your OpenRouter key.*

```
Build docs/index.html from the plan we agreed. Rules:
- One file: plain HTML, CSS and JavaScript. No build step. A library
  from a CDN is fine.
- No API keys, no environment variables, no calls to any AI service.
  The page must work with no AI behind it.
- Use only content from skill/knowledge.md and skill/SKILL.md.
- Readable on a phone. Text large enough for the learner in LEARNER.
- Before you write, tell me in three lines what you will create.
  After you write, tell me how to open it, and stop.
- Add one line per change to SETUP_LOG.md under "What the agent did".
```

------------------------------------------------------------------------

## P4 · Test: the persona test

*Agent with a browser, or do it yourself and paste what happened.*

```
Open docs/index.html as my learner (see LEARNER in SKILL.md). Try
three moves:
1. a wrong answer, the one my misconception predicts
2. something off topic
3. "just tell me the answer" (or quitting halfway)
For each move, report what the page did, word for word, and whether
it followed SKILL.md. Do not fix anything. Just report.
```

Chatbot or teacher tool: run the three moves in your own tool and paste the real transcript into the page. Don't use an imagined one.

------------------------------------------------------------------------

## P5 · Fix one thing

```
Fix only this: [one problem from the test, in my words].
Show me the change before you make it. Change nothing else.
Then tell me how to check that it worked.
```

Repeat P4 → P5 until the three moves work. **One fix per prompt** keeps the cost down and keeps you in charge.

------------------------------------------------------------------------

## P6 · Accessibility and ethics check (Workshop 4)

```
Check docs/index.html and report. Don't fix anything yet. List each
problem with the line it is on:
- reading level and plain language for my learner
- alt text on every image; captions or a transcript for any video
- works with a keyboard only; visible focus
- colour contrast; nothing that relies on colour alone
- the page says it was built with AI and never claims to be a teacher
- no student names, no real student work, no personal data
- no key, token or password anywhere in the folder
Then I will choose what to fix, one item at a time (P5).
```

------------------------------------------------------------------------

## P7 · Deploy: GitHub Pages or Vercel

*Antigravity's agent. You need a free GitHub account; Vercel signs in with it.*

```
Help me publish docs/ as a public website. Show me each step and wait
for my OK before running anything.

Before anything else, a safety check. Search the whole folder and its
git history for:
- any API key, token or password (including in .env files)
- student names or real student work
- anything I marked private
If you find one, STOP and tell me. Do not publish.
Also confirm the author line in card.md and "About this tool" matches
what I agreed to share. Ask me.

Then I choose ONE route:

A) GitHub Pages
1. I log in to GitHub myself in the browser (never paste a token here).
2. Create a public repository named [tool-name] and push this folder.
3. Tell me where to click: Settings → Pages → Deploy from a branch →
   main → /docs → Save.
4. Give me the address (https://USERNAME.github.io/tool-name/) and
   check it loads.

B) Vercel
1. Push the folder to GitHub as in A, steps 1–2.
2. Tell me where to click on vercel.com: Add New → Project → import
   the repository → Framework: Other → Root Directory: docs → no build
   command → Deploy.
3. Give me the address and check it loads.

Rules: this is a static site. Do not add a server, serverless function,
API route, environment variable or key. If anything seems to need one,
stop and tell me to ask my instructor.
Finally, write the live address into card.md and SETUP_LOG.md.
```

**Submit in Canvas:** the live address and the zipped folder. The folder is the grant record. The address is what goes in the catalog.
