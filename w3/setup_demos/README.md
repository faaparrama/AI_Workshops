# Setup demos: one video per tool

Drop screenshots into `<folder>/screenshots/`. Claude turns each folder into a short video.

## The order students follow

1. **`00_desktop-folder/`** (every student watches this one): download `my-tool-demo.zip`, unzip it, and move the `my-tool-demo` folder to the Desktop. It ends with the folder sitting on the Desktop.
2. **`01_md-editor/`** (every student watches this one): install a Markdown editor, open the `my-tool-demo` folder from the Desktop, and edit `knowledge.md` with their own material. Students never open a `.md` file in Word or TextEdit.
3. **One tool video** (`codex/`, `antigravity/`, `claude-code/`, `opencode/`): open the app, then open the `my-tool-demo` folder from the Desktop.

## Taking the screenshots

- `00_desktop-folder`: from the download link to the folder on the Desktop.
- `01_md-editor`: from the download page to `knowledge.md` open, with a line of new text typed and saved.
- Each tool: from opening the app to its first answer about the folder. Test prompt: "Read SKILL.md and tell me what this tool does."
- Name each file with its number and the action: `01_download.png`, `02_open-settings.png`, `03_paste-key.png`.
- If a step happens off screen (a keyboard shortcut, a wait), say it in the file name.
- Capture the whole window, at the same window size every time.
- Last screenshot: the tool answering a test prompt. That is the proof it works.
- A key or email on screen is fine. Claude blurs it before anything is published.

The raw screenshots stay out of git (see `.gitignore`). Only the finished videos are tracked.
