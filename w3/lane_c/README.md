# The build kit: from M2 to a live website

Every student ends with **one website** for their tool, deployed by the student on GitHub Pages or Vercel. A static tool *is* the page. A chatbot or teacher tool gets a page that shows it: what it does, how to use it, a real test transcript.

Everything lives in one project folder. The folder is your tool, your record and your submission.

```
my-tool/
  skill/        SKILL.md · knowledge.md     ← your M2 → M3 → M4
  assets/       optional: pictures, icons, links · CREDITS.md
  docs/         index.html                  ← the website
  SETUP_LOG.md  what the agent did · what you decided, and why
  card.md       what it is, where it lives
  .gitignore    keeps keys and clutter out
```

**You are in charge.** The agent proposes and you accept or reject. Every prompt in `PROMPTS.md` makes it wait for your OK. Your accept/reject reasons go in `SETUP_LOG.md`, in your own words. That log is what you defend in December.

## Steps

1. **Copy `template/`** and rename it after your tool. Open it in Antigravity (File → Open Folder).
2. **P0 · Gather.** Turn your M1 and M2 into `skill/` (works in any AI chat). Answer its questions yourself.
3. **P1 · Set up.** Antigravity's agent. Read each command before you approve it.
4. **Zoo Code** (to build static tools on an OpenRouter key). Extensions panel → search **Zoo Code** → Install. Choose **OpenRouter**, paste your key into its settings box, pick a model from `MODELS.md`. The key stays in Zoo Code's settings, never in your folder.
5. **P2 · Plan the page → P3 · Build → P4 · Test → P5 · Fix one thing.** Repeat P4–P5 until the three persona moves work.
6. **P6 · Accessibility and ethics** (Workshop 4).
7. **P7 · Deploy** on GitHub Pages or Vercel. The safety check runs first.
8. **Submit** the live address + the zipped folder in Canvas.

## If something goes wrong

- The agent wants to install something system-wide, or asks for a password: say no, and ask in office hours.
- The agent proposes a server, an API route or an environment variable: say no. A static site needs none.
- Your credit runs out: you asked for too much in one prompt. Ask for one change at a time.
- You find your key in any file, or in a commit: delete it, tell your instructor, and get a new key.
