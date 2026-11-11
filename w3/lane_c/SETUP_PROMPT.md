# Setup prompt — paste into Antigravity's agent

You are setting up a project folder for a student's teaching tool. The student is a future teacher, not a programmer. Keep everything inside this folder.

Do these, in order:

1. Check that this folder has `skill/`, `site/`, `SETUP_LOG.md`, `card.md` and `.gitignore`. Create any that are missing. Do not change files inside `skill/`.
2. Check whether `git` is installed. If it is, run `git init` here and make a first commit. If it is not, say so and stop this step.
3. Check whether Python 3 is installed. If it is, create a virtual environment in `.venv/` inside this folder. If it is not, explain in two sentences how the student installs it, and wait.
4. Give the student one command that previews `site/` in the browser (for example `python3 -m http.server 8000 --directory site`). Run it once to show it works, then stop it.
5. Write `SETUP_LOG.md`: every command you ran, one line each, and why, in plain words.

Rules:
- Install inside this folder whenever you can. **Ask before installing anything system-wide**, and say why it is needed.
- Never use `sudo` or ask for an administrator password without explaining first and waiting for a yes.
- **Never write an API key, password or token into any file.** If the student pastes one, tell them to delete it.
- Do not build the tool. Building is the next step, in a different agent.
- When you finish, list what is installed and what the student does next, in five lines or fewer.
