# Lane C — build your tool in Antigravity

For the hard static tools: a simulation, a keyboard, a drag-and-drop diagram. Everything lives in one project folder. The folder is your tool, your record and your submission.

**Two agents, two jobs.** Antigravity's own agent **sets up** the folder. Zoo Code, running on your OpenRouter key, **builds** the tool. Don't mix them up.

## Steps

1. **Get your key.** Your instructor gives you an OpenRouter key with a credit limit. Keep it private. Don't email it, paste it into a document or put it in your folder.
2. **Install Google Antigravity** and sign in with a Google account.
3. **Make the folder.** Copy `template/` and rename it after your tool, e.g. `staff-reader/`. Open that folder in Antigravity (File → Open Folder).
4. **Fill in `skill/`.** Paste your SKILL.md (LEARNER · TASK · HOW YOU TALK) and your knowledge.md.
5. **Set up.** Open Antigravity's agent panel. Paste everything in `SETUP_PROMPT.md`. Read each command before you approve it. When it finishes, open `SETUP_LOG.md` and check it.
6. **Install Zoo Code.** Extensions panel → search **Zoo Code** → Install. Open it, choose **OpenRouter** as the provider, paste your key into its settings box, and pick a model from `MODELS.md`. The key stays in Zoo Code's settings, outside your folder.
7. **Build.** In Zoo Code, paste `BUILD_PROMPT.md`. Fill in the blanks first.
8. **Test.** Open `site/index.html` in your browser. Run the persona test: one wrong answer, one off-topic move, one quit. Tell Zoo Code what broke, one thing at a time.
9. **Submit.** Zip the folder and upload it to Canvas. Your instructor publishes `site/` to GitHub Pages.

## If something goes wrong

- The agent wants to install something "system-wide" or asks for your password: stop and ask in office hours.
- Your credit runs out: you've built too much in one prompt. Ask for one change at a time.
- You see your key in any file: delete it, tell your instructor, and get a new key.
