# Setup demos: one video per tool

Drop screenshots into `<tool>/screenshots/`. Claude turns each folder into a short video.

## Taking the screenshots

- One screenshot per step, in order: from download to the first answer.
- Name each file with its number and the action: `01_download.png`, `02_open-settings.png`, `03_paste-key.png`.
- If a step happens off screen (a keyboard shortcut, a wait), say it in the file name.
- Capture the whole window, at the same window size every time.
- Last screenshot: the tool answering a test prompt. That is the proof it works.
- A key or email on screen is fine. Claude blurs it before anything is published.

The raw screenshots stay out of git (see `.gitignore`). Only the finished videos are tracked.
