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
5. The website is a page that shows the tool, with the share link and one real transcript (`lane_c/PROMPTS.md`, P2 and P7). Submit the address and the folder.

### 2 · Static page
1. Fill in the skill folder.
2. Write a half-page spec: what is on screen, the items (from `knowledge.md`), what a right answer and a wrong answer each trigger (from HOW YOU TALK), and when it ends (STOP).
3. **Simple (Lane A):** paste the spec into any assistant that writes a page (Claude artifact, ChatGPT canvas, Gemini canvas). Ask for **one self-contained HTML file with no API key**, and download it.
   **Hard (Lane C): Google Antigravity** for the most advanced students. It is easier to use than VS Code, and its agent can install Python and set up the environment for the student. The agent reads the folder and builds the page. Fallback: a coding agent with a capped OpenRouter key (Cline, Kilo Code, OpenCode).
4. Open it in a browser and run the persona test against it.
5. Deploy it yourself on GitHub Pages or Vercel (`lane_c/PROMPTS.md`, P7), then submit the live address and the zipped folder in Canvas.

### 3 · Teacher tool
1. Fill in the skill folder. LEARNER is the teacher. HOW YOU TALK covers the student who receives the output.
2. Load it in your own account (same as Chatbot, Lane A).
3. Test with three real inputs. Check the length against your LIMIT and **verify every fact**.
4. The website is a page that shows the tool: what it does, how to use it, three sample outputs (`lane_c/PROMPTS.md`, P2 and P7). Submit the address and the folder.

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
3. Did Antigravity install and run on your laptop on Thursday? Yes · Tried, it failed · Didn't try.
4. May your finished tool appear in a public catalog? With my name · Without my name · No.
5. Do you have a GitHub account? Yes · No · I'll make one.

**Reading the result.** Q2 = "No" or "none" on Q1, among chatbot students → proxy needed, with that many seats. Q3 = "Yes" → Lane C on Antigravity is possible. Q3 = "No" among hard-static students → those builds move to an office-hours clinic, or fall back to a chatbot. Q4 sets the catalog.

## Option to weigh after the survey: OpenRouter + Open WebUI

Open WebUI is a self-hosted chat interface, similar to ChatGPT, that connects to OpenRouter. Each student's tool would be a "model" inside it: `SKILL.md` as the system prompt, `knowledge.md` as its knowledge file. The key stays on the server.

| For | Against |
|---|---|
| Replaces Gems/GPTs for the whole class, with no code to write; the proxy + chat template would not be needed for class use | Needs a server that stays on (a small paid VM, or a free tier that sleeps or wipes storage), plus updates |
| One place for every chatbot; students need no AI account | Students get logins and their chats are stored: student data on a server. **Check with MSU ITS before using it with students** |
| You can read the transcripts, which is the prompt log and the persona test in one place | Login-only, so it is a weak fit for a public catalog or for K–12 learners |
| Model allowlist and one capped key | It runs on the server, not on Pages; the grant record is the folders in the repo |

**Fit:** a class sandbox for Lane B chatbots during the build. The public showcase stays static pages + the proxy. Decide after Q1–Q2: if many chatbot students have no usable account, Open WebUI beats building the proxy.

## Considered: bolt.diy (2026-11-10)

An open-source app builder in the browser that runs on an OpenRouter key.

- **As a builder for static pages:** it works. Ask for Vite + React or plain HTML, and the built files go to Pages. It is the OpenRouter-funded equivalent of Antigravity. Costs: someone installs and hosts it (Node or Docker), and a build re-sends the whole project to the model, so it burns tokens.
- **As the route for chatbots: no.** The suggested design (Next.js API routes + a key in `.env.local`, deployed to Vercel or Netlify) gives every student their own server app holding a key, on a public URL anyone can use to spend credits. It can't run on Pages. A `.env.local` committed by mistake leaks the key. Supabase adds student data on another service. That makes 17 apps to maintain where the plan has one shared runtime (proxy or Open WebUI).
- **Use only if** the survey shows Antigravity won't work for the Lane C students.
- **Video reviewed** (bolt.diy + DeepSeek V3 + Gemini 2.0, early 2025). Setup is a terminal install (`pnpm install`, `pnpm run dev`), so Andy or an office-hours clinic does it, not students alone. It fixes its own errors, pushes to GitHub, and takes voice prompts. Its demo is a **playable synth keyboard**, the closest match to the hardest music tool. The models and the "free" costs are dated.

The free-tier limits named here change often. Check them the week the lanes are fixed.
