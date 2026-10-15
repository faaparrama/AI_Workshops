#!/usr/bin/env python3
"""Assemble w2/index.html — the self-guided Workshop 2. Edit here, run, commit both."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

# ---------- serial-position curve, same shape as the deck ----------
UCURVE = '''<svg viewBox="0 0 470 300" role="img" aria-label="Two U-shaped curves of recall by position, one for people and one for language models. Both are higher at the start and the end of a list than in the middle; the model's curve dips lower in the middle.">
  <line x1="50" y1="240" x2="450" y2="240" class="uc-axis" stroke-width="2"/>
  <line x1="50" y1="240" x2="50" y2="30" class="uc-axis" stroke-width="2"/>
  <text x="50" y="270" font-size="17" class="uc-ink">start</text>
  <text x="250" y="270" font-size="17" class="uc-ink" text-anchor="middle">middle</text>
  <text x="450" y="270" font-size="17" class="uc-ink" text-anchor="end">end</text>
  <text x="250" y="294" font-size="15" class="uc-muted" text-anchor="middle">position in the list · in the window</text>
  <text x="38" y="135" font-size="15" class="uc-muted" text-anchor="middle" transform="rotate(-90 38 135)">recalled · used</text>
  <rect x="200" y="185" width="100" height="40" rx="6" class="uc-lost"/>
  <text x="250" y="210" font-size="15" class="uc-ink" text-anchor="middle">lost here</text>
  <path d="M60,70 C150,215 330,215 440,48" fill="none" class="uc-you" stroke-width="5"/>
  <path d="M60,52 C160,235 330,235 440,95" fill="none" class="uc-model" stroke-width="4" stroke-dasharray="10 7"/>
  <line x1="170" y1="40" x2="200" y2="40" class="uc-you" stroke-width="5"/><text x="208" y="46" font-size="17" font-weight="600" class="uc-you-t">you · Week 6</text>
  <line x1="170" y1="68" x2="200" y2="68" class="uc-model" stroke-width="4" stroke-dasharray="10 7"/><text x="208" y="74" font-size="17" font-weight="600" class="uc-model-t">the model · Liu 2024</text>
</svg>'''

RULES = [
    "Be encouraging.",
    "Use real examples from Mississippi history.",
    "Never explain a document; ask a question instead.",
    "Keep every reply under 60 words.",
    'Say "evidence," never "proof."',
    "Always end with a question.",
    "Avoid the word \"bias\" until the student has named the author's purpose.",
    "Mention that primary sources can disagree.",
    "Don't use bullet points.",
    "Do not ask more than one question per turn.",
    "Refer to the student by name if they give one.",
    "Do not explain what you were not asked.",
]
RULE_ROWS = "\n".join(
    f'<li><label class="chk"><input type="checkbox" id="r{i+1}" data-save> {r.replace("&", "&amp;")}</label></li>'
    for i, r in enumerate(RULES))
OVERLOAD_PROMPT = ("You are a tutor for 10th graders learning to source historical documents. "
                   + " ".join(RULES)
                   + "\n\nStudent: my name is Lee. This newspaper article is a primary source, so it's true, right?")

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Curation: teaching the tool</title>
<meta name="description" content="EPY 3143 Workshop 2, self-guided: how a language model reads and reasons, and how to curate the knowledge file and the v0 prompt your tool runs on.">
<style>
:root{
  --maroon:#5D1725; --maroon-deep:#40101A; --maroon-soft:#F2E9EB;
  --ground:#FFFFFF; --surface:#FAF8F8; --ink:#241E20; --muted:#6E6E6E;
  --rule:#E4DDDE; --rule-strong:#C1C6C8;
  --gold:#C99700; --gold-text:#8A6600; --gold-bg:#FBF6E9;
  --teal:#00A3AD; --teal-text:#01717A; --teal-bg:#E8F6F7;
  --ok:#2F6B4F; --ok-bg:#EDF5F1; --no:#9B2C2C; --no-bg:#FBEDED;
  --box:#FFFFFF;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --maroon:#E9A7B2; --maroon-deep:#F3C3CB; --maroon-soft:#2E2126;
  --ground:#171215; --surface:#1F181B; --ink:#EFE8EA; --muted:#A79DA0;
  --rule:#382C31; --rule-strong:#4C3C42;
  --gold:#FFB81C; --gold-text:#FFC94D; --gold-bg:#2A2118;
  --teal:#5FD3DA; --teal-text:#7FE0E6; --teal-bg:#152628;
  --ok:#7FCBA4; --ok-bg:#18251F; --no:#F09B9B; --no-bg:#2A1A1A;
  --box:#1F181B;
}}
:root[data-theme="dark"]{
  --maroon:#E9A7B2; --maroon-deep:#F3C3CB; --maroon-soft:#2E2126;
  --ground:#171215; --surface:#1F181B; --ink:#EFE8EA; --muted:#A79DA0;
  --rule:#382C31; --rule-strong:#4C3C42;
  --gold:#FFB81C; --gold-text:#FFC94D; --gold-bg:#2A2118;
  --teal:#5FD3DA; --teal-text:#7FE0E6; --teal-bg:#152628;
  --ok:#7FCBA4; --ok-bg:#18251F; --no:#F09B9B; --no-bg:#2A1A1A;
  --box:#1F181B;
}
*{box-sizing:border-box}
body{background:var(--ground);color:var(--ink);
  font-family:"Source Sans 3","Segoe UI",-apple-system,BlinkMacSystemFont,sans-serif;
  font-size:17px;line-height:1.62;margin:0 auto;padding:1.5rem 16px 5rem;max-width:44rem;
  -webkit-font-smoothing:antialiased}
h1{font-family:Georgia,"Iowan Old Style","Times New Roman",serif;font-size:2rem;line-height:1.1;color:var(--maroon);margin:0 0 .2em;text-wrap:balance}
h2{font-family:Georgia,"Iowan Old Style","Times New Roman",serif;font-size:1.45rem;line-height:1.2;color:var(--ink);margin:2.8rem 0 .7rem;padding-bottom:.22em;border-bottom:3px solid var(--maroon);text-wrap:balance}
h2 .t{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.62em;color:var(--muted);font-weight:400;letter-spacing:.05em;margin-left:.6em;white-space:nowrap}
h3{font-size:1.05rem;margin:1.8rem 0 .5rem;color:var(--maroon)}
p{margin:0 0 1rem}
strong{color:var(--maroon-deep)}
a{color:var(--maroon)}
code{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.88em;background:var(--maroon-soft);color:var(--maroon-deep);padding:.06em .3em;border-radius:2px}
pre{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.8em;line-height:1.45;background:var(--surface);border:1px solid var(--rule);border-radius:6px;padding:.8rem 1rem;white-space:pre-wrap;overflow-wrap:anywhere;margin:.6rem 0}
table{border-collapse:collapse;width:100%;font-size:.92em;margin:0 0 1.2rem}
th{text-align:left;color:var(--maroon);border-bottom:2px solid var(--maroon);padding:.35em .6em;font-size:.8em;letter-spacing:.05em;text-transform:uppercase}
td{border-bottom:1px solid var(--rule);padding:.4em .6em;vertical-align:top}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
figure{margin:1.5rem 0}
figure svg{max-width:100%;height:auto;display:block}
figcaption{font-size:.82em;color:var(--muted);margin-top:.5rem}
.head{border-top:4px solid var(--maroon);padding-top:1rem;margin-bottom:1.5rem}
.head .moment{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 .5rem}
.head .sub{color:var(--muted);font-size:1rem;margin:.3rem 0 0}
.keyline{border-left:5px solid var(--maroon);background:var(--maroon-soft);padding:.7rem 1rem;margin:1.2rem 0;border-radius:0 3px 3px 0}
.keyline p{margin:0 0 .5rem}.keyline p:last-child{margin:0}
.gotcha{border-left:5px solid var(--gold);background:var(--gold-bg);padding:.7rem 1rem;margin:1.2rem 0;font-size:.94em;border-radius:0 3px 3px 0}
.gotcha p{margin:0 0 .5rem}.gotcha p:last-child{margin:0}
.do{border-left:5px solid var(--teal);background:var(--teal-bg);padding:.8rem 1rem;margin:1.2rem 0;border-radius:0 3px 3px 0}
.do p{margin:0 0 .5rem}.do p:last-child{margin:0}
.do .tag,.keyline .tag{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--teal-text);display:block;margin-bottom:.3rem}
.keyline .tag{color:var(--maroon)}
label{display:block;font-weight:600;margin:.9rem 0 .3rem;font-size:.95em}
label.chk{display:flex;gap:.5em;align-items:flex-start;font-weight:400;margin:.25rem 0}
label.chk input{margin-top:.35em;flex:none}
textarea,input[type=text],input[type=number],select{width:100%;font:inherit;font-size:.95em;color:var(--ink);background:var(--box);border:1px solid var(--rule-strong);border-radius:4px;padding:.5em .6em}
textarea{min-height:5.5em;resize:vertical}
textarea.short{min-height:3em}
input[type=number]{width:5.5em;text-align:right}
button{font:inherit;font-size:.92em;font-weight:700;border-radius:5px;padding:.5em 1em;cursor:pointer;border:2px solid var(--maroon);background:var(--maroon);color:#fff}
button.ghost{background:transparent;color:var(--maroon)}
button.copy{font-size:.78em;padding:.25em .7em;margin-top:.4rem}
a:focus-visible,button:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid var(--maroon);outline-offset:2px}
@media (pointer:coarse){button{min-height:2.75rem}}
.video{position:relative;width:100%;aspect-ratio:16/9;background:#000;border-radius:6px;overflow:hidden;margin:1rem 0}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.prompt{background:var(--surface);border:1px solid var(--rule);border-radius:6px;padding:.8rem 1rem;margin:.6rem 0;font-family:Georgia,"Times New Roman",serif;font-size:.97em}
.prompt em{color:var(--maroon-deep)}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
@media (max-width:640px){.cols{grid-template-columns:1fr}}
.card{background:var(--surface);border:1px solid var(--rule);border-radius:6px;padding:.9rem 1rem}
.card h4{margin:0 0 .5rem;color:var(--maroon);font-size:1rem}
details{border:1px solid var(--rule);border-radius:6px;padding:.5rem .9rem;margin:1rem 0;background:var(--surface)}
summary{cursor:pointer;font-weight:700;color:var(--maroon)}
details[open] summary{margin-bottom:.5rem}
.rules{margin:.4rem 0 .8rem;padding-left:1.6em}
.rules li{margin:0}
.score{border-left:4px solid var(--gold);background:var(--gold-bg);padding:.5rem .8rem;margin:.5rem 0;font-size:.95em;border-radius:0 3px 3px 0}
.score b{color:var(--maroon-deep)}
.status{font-size:.85em;color:var(--muted);margin-left:.6em}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:0 1rem}
@media (max-width:640px){.grid2{grid-template-columns:1fr}}
.uc-axis{stroke:var(--muted)}.uc-ink{fill:var(--ink)}.uc-muted{fill:var(--muted)}
.uc-you{stroke:var(--maroon)}.uc-you-t{fill:var(--maroon)}
.uc-model{stroke:var(--muted)}.uc-model-t{fill:var(--muted)}
.uc-lost{fill:var(--gold);opacity:.22}
.footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--rule);font-size:.88em;color:var(--muted)}
.footer ul{padding-left:1.2em}
.toc{font-size:.9em;columns:2;column-gap:2rem;margin:0 0 1rem;padding-left:1.2em}
@media (max-width:640px){.toc{columns:1}}
@media print{button,.video,.no-print{display:none!important}textarea{min-height:3em}}
</style>
</head>
<body>

<header class="head">
  <p class="moment">EPY 3143 · Week 9 · Workshop 2 · Online</p>
  <h1>Curation: teaching the tool what to teach</h1>
  <p class="sub">About ninety minutes, self-guided: how the model reads and reasons, then what you give it to read. You leave with your <strong>v0</strong>, a knowledge file and a system prompt, tested once.</p>
</header>

<div class="keyline">
  <span class="tag">How this page works</span>
  <p>Work in order, with <strong>the AI tool you build in</strong> open in another tab. Have your <strong>M1</strong>, your <strong>standard</strong> (the actual line, with its source) and your <strong>Readiness Checks from Weeks 6–8</strong> nearby.</p>
  <p>Your answers save in this browser and go nowhere else. At the end, one button copies them for the <strong>Week 9 Engagement Check</strong>.</p>
  <p><span id="saveStatus" role="status" aria-live="polite" class="status"></span></p>
</div>

<ol class="toc">
  <li><a href="#map">The map</a> <span class="status">3 min</span></li>
  <li><a href="#inside">Inside the model</a> <span class="status">40 min</span></li>
  <li><a href="#overload">Overload me</a> <span class="status">5 min</span></li>
  <li><a href="#curate">Curate: your file and your v0</a> <span class="status">30 min</span></li>
  <li><a href="#agent">Staying the agent</a> <span class="status">8 min</span></li>
  <li><a href="#exit">Exit card, then Milestone 2</a> <span class="status">4 min</span></li>
</ol>

<!-- ============================================================ -->
<h2 id="map">1 · The map <span class="t">3 min</span></h2>

<p>Workshop 1 had one idea: <strong>the tool produces the most likely text, not the truth.</strong> Today we explore how models reason and solve problems. First, how a model processes the information you give it. Then, what information you actually give it. Every LLM idea below connects to a theory you already know from Unit 2.</p>

<div class="scroll"><table>
<tr><th>Unit 2</th><th>LLM idea</th><th>Cognitive theory</th><th>What it means</th></tr>
<tr><td rowspan="5"><strong>Memory</strong><br>Week 6</td><td>context window</td><td>working memory (Baddeley)</td><td>limited active capacity, in both</td></tr>
<tr><td>attention</td><td>selective attention</td><td>focus on what is relevant</td></tr>
<tr><td>RAG</td><td>long-term memory retrieval</td><td>pulled from a store when cued</td></tr>
<tr><td>hallucination</td><td>constructive memory (Bartlett)</td><td>recall rebuilds the gist</td></tr>
<tr><td>embeddings</td><td>semantic memory</td><td>meaning lives in relationships</td></tr>
<tr><td rowspan="2"><strong>Knowledge construction</strong><br>Week 7</td><td>training</td><td>schema theory</td><td>structure built from repeated patterns</td></tr>
<tr><td>chain-of-thought</td><td>worked examples, <em>not yet</em> metacognition</td><td>visible steps, without monitoring them</td></tr>
<tr><td rowspan="2"><strong>Complex processes</strong><br>Week 8</td><td>pattern-matching</td><td>heuristics vs. algorithms; the reworded problem</td><td>a heuristic; its steps imitate an algorithm</td></tr>
<tr><td>hallucination</td><td>critical evaluation</td><td>you verify; it does not</td></tr>
</table></div>

<p><strong>Then curation:</strong> your knowledge file is your fund of knowledge, and your system prompt is an advance organiser. The parallels are useful, not exact: read each row as "behaves like." <em>Fine-tuning, the model's version of conceptual change, comes in Workshop 4.</em></p>

<!-- ============================================================ -->
<h2 id="inside">2 · Inside the model <span class="t">40 min</span></h2>

<h3>Video: AI vs human thinking <span class="status">12 min</span></h3>
<p><strong>IBM Technology — Martin Keen.</strong> People and language models, compared on six things. During the memory segment (4:46), hold one question: <strong>what does each one do when it runs out of room?</strong></p>
<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/-ovM0daP6bw" title="AI vs Human Thinking: How Large Language Models Really Work — IBM Technology" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>
<p class="status">Not loading? <a href="https://www.youtube.com/watch?v=-ovM0daP6bw">Open it on YouTube.</a></p>

<div class="do">
  <span class="tag">Write</span>
  <label for="q_room">What does a person do when working memory runs out of room? What does the model do?</label>
  <textarea id="q_room" data-save class="short"></textarea>
</div>

<h3>1 · The context window is working memory <span class="status">4 min</span></h3>
<p>Everything the model "knows" during a chat sits in one window: <strong>your instructions, the file, the chat so far, its own answers.</strong> Most current models hold about <strong>1 million tokens</strong> (pieces of words), some 750,000 words; free tiers give less. Nothing from your chat goes into its training. Size is rarely the problem now. The middle is:</p>

<figure>
''' + UCURVE + r'''
<figcaption>Illustrative shape, not data. Models use the start and end of a long window better than the middle (Liu et al., 2024), like primacy and recency in Week 6.</figcaption>
</figure>

<div class="keyline"><p><strong>Design consequence:</strong> the rules that matter go first, the file stays short, and long chats drift. Matthew kept only the first of several instructions; a tool drops the rules buried in the middle of a long prompt.</p></div>

<h3>2 · Attention is selective attention <span class="status">3 min</span></h3>
<div class="prompt"><em>The trophy didn't fit in the suitcase because <strong>it</strong> was too big.</em></div>
<label for="q_it1">In this sentence, <em>it</em> is…</label>
<select id="q_it1" data-save><option value="">choose</option><option>the trophy</option><option>the suitcase</option></select>
<div class="prompt"><em>The trophy didn't fit in the suitcase because <strong>it</strong> was too small.</em></div>
<label for="q_it2">In this sentence, <em>it</em> is…</label>
<select id="q_it2" data-save><option value="">choose</option><option>the trophy</option><option>the suitcase</option></select>

<details>
  <summary>Check, then read</summary>
  <p>Big → the trophy. Small → the suitcase. One word, far from <em>it</em>, flips the meaning. The model does this for every word: it <strong>weighs which other words in the window matter</strong>.</p>
  <p><strong>Design consequence:</strong> everything in the window competes for attention. Paste a 200-page curriculum guide and all of it gets weighed. Curation decides what deserves attention.</p>
</details>

<h3>3 · Does it read the internet? <span class="status">6 min</span></h3>
<fieldset style="border:0;padding:0;margin:0">
  <legend style="font-weight:600">True or false: <em>when I ask a chatbot a question, it reads the internet and understands it.</em></legend>
  <label class="chk"><input type="radio" name="tf" id="tf_t" data-save> True</label>
  <label class="chk"><input type="radio" name="tf" id="tf_f" data-save> False</label>
</fieldset>

<div class="do">
  <span class="tag">Try it · 4 min</span>
  <p>Three asks in one <strong>fresh chat</strong>. Predict before each.</p>
  <p><strong>1 · Dense.</strong> <em>"Quote, word for word, [your standard's code]."</em></p>
  <label for="q_quote1">How close was it?</label>
  <textarea id="q_quote1" data-save class="short"></textarea>
  <p><strong>2 · Thin.</strong> Ask about something no search can reach: <em>"In EPY 3143's Case Study 2, why does Matthew stop halfway through his independent work?"</em> (or your own unit plan).</p>
  <label for="q_quote3">What did it do: say it could not find it, or answer anyway? If it answered, from what?</label>
  <textarea id="q_quote3" data-save class="short"></textarea>
  <p><strong>3 · Paste.</strong> Paste the real text and ask again.</p>
  <label for="q_quote2">What changed, and what changed about the model?</label>
  <textarea id="q_quote2" data-save class="short"></textarea>
</div>

<div class="scroll"><table>
<tr><th>Where the words come from</th><th>What actually happens</th></tr>
<tr><td><strong>Training</strong></td><td>Billions of pages read <strong>once</strong>, before release, and compressed into probabilities. No pages kept, no sources.</td></tr>
<tr><td><strong>Web search</strong> <span class="status" style="margin:0">always on</span></td><td>It searches, copies a few pages <strong>into the window</strong>, and answers from them.</td></tr>
<tr><td><strong>Your file</strong></td><td>Your text is copied <strong>into the window</strong>. A page or two fits whole.</td></tr>
</table></div>

<div class="keyline"><p><strong>False.</strong> It never reads anything outside the window; it <strong>predicts from what is in it.</strong> Your standard is on thousands of pages, so it came back exactly: copied from a search (look for "Searched the web" or source links) or rebuilt from training. Matthew is on none, so it stopped or rebuilt a probable student from the gist, as Bartlett's readers did. Pasting changed the window, and the model stayed the same.</p>
<p><strong>It is right where the internet is dense, and probable where it is thin. Your classroom is where it is thin.</strong> That is what Milestone 2 is for.</p></div>

<p class="status" style="margin:0 0 1rem">Huge collections, like a district's whole curriculum, are searched first and only the closest pieces copied in. That is <strong>RAG</strong>. Your file will not need it.</p>

<h3>Video: how AI learned to reason <span class="status">7 min</span></h3>
<p><strong>Engineering Visualized.</strong> From next-word prediction to reasoning models. Watch for one thing: <strong>where does the model keep its in-between steps?</strong></p>
<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/hoPF9QbeGdc" title="How AI Learned to Reason — From Next Token Prediction to Reasoning Models — Engineering Visualized" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>
<p class="status">Not loading? <a href="https://www.youtube.com/watch?v=hoPF9QbeGdc">Open it on YouTube.</a></p>

<h3>4 · It reasons by writing, and pattern-matches <span class="status">6 min</span></h3>
<p>Two asks in a <strong>fresh chat</strong>. Predict before each.</p>
<div class="prompt"><strong>1 · Dense:</strong> <em>A bat and a ball cost $1.10. The bat costs $1.00 more than the ball. How much is the ball?</em></div>
<label for="q_bb1">What did it answer? Why do you think it got there?</label><input type="text" id="q_bb1" data-save>
<div class="prompt"><strong>2 · Thin:</strong> <em>I'm a 10th grader. Help me work out whether a newspaper report of the 1963 Jackson sit-in is reliable. Don't tell me the answer.</em></div>
<label for="q_bb2">Count: how many questions did it ask you? How many things did it explain?</label><input type="text" id="q_bb2" data-save>

<details>
  <summary>Check, then read</summary>
  <p><strong>1 passes</strong> (5 cents; 10 cents is the System 1 answer from Week 8). It has seen this famous problem thousands of times. That says nothing about <em>your</em> learner's problem.</p>
  <p><strong>On 2</strong>, it usually gives a full sourcing checklist, each item explained, maybe one question at the end. Nothing in it is wrong, and it did the learner's sourcing for them. It answered <strong>the usual question</strong>, <em>how do you source a document?</em>, instead of <strong>this learner's</strong>, <em>help me do it</em>. HOLD BACK in your v0 is how you stop it.</p>
  <p><strong>How it reasons:</strong> each step it writes goes into the window, and the next step is predicted from it. That helps, like a worked example, but <strong>every step is still the probable next step</strong>, and the written steps do not always reflect what drove the answer (Turpin et al., 2023). Nothing monitors them, so it is <em>not yet</em> metacognition. That job is yours.</p>
  <p><strong>Algorithm or heuristic?</strong> Predicting the next word is a heuristic: fast, usually right. Its written steps imitate an algorithm and slip as a procedure gets longer (Dziri et al., 2023). When the tool writes and runs code ("Analyzing," "Ran code"), a real algorithm does the work.</p>
</details>

<div class="do">
  <span class="tag">Write</span>
  <label for="q_reason">Now the same move in your own subject: ask it to help one of your learners without giving the answer. What did it give away?</label>
  <textarea id="q_reason" data-save class="short"></textarea>
</div>

<div class="keyline"><p><strong>Design consequence:</strong> a tutor that shows every step does the learner's thinking. Decide which steps the tool shows and which it <strong>asks for</strong>. That is M2 Part 2: remember, or reason.</p></div>

<!-- ============================================================ -->
<h2 id="overload">3 · Overload me <span class="t">5 min</span></h2>

<p>A tutor prompt as a first-time builder writes it: one role, twelve rules, one paragraph. <strong>Predict which rules it will break.</strong></p>
<pre id="ovp">''' + OVERLOAD_PROMPT.replace("&", "&amp;").replace("<", "&lt;") + r'''</pre>
<button class="copy ghost" type="button" data-copy="ovp">Copy</button>

<p style="margin-top:1rem">Paste it into a fresh chat. Then tick every rule the reply <strong>kept</strong>.</p>
<ol class="rules">
''' + RULE_ROWS + r'''
</ol>
<div class="score" id="ovScore" aria-live="polite">Tick the rules it kept.</div>

<details>
  <summary>Read after you score it</summary>
  <p>Most tools keep the first and last few and drop some in the middle, usually the word limit and the "bias" rule. Lee's yes-or-no question also pulls against rule 3: did it simply answer?</p>
  <p>The fix is <strong>chunking</strong>, your Week 6 load budget: non-negotiables first, numbered, grouped, the rest cut. That is the shape of the v0 template below.</p>
</details>

<!-- ============================================================ -->
<h2 id="curate">4 · Curate: your file and your v0 <span class="t">30 min</span></h2>

<h3>Whatever you leave out, it fills in</h3>
<p>The model <strong>always answers</strong>. What you leave out, it fills with the <strong>probable</strong>: the textbook-average lesson. M2 replaces it with <strong>what you actually teach.</strong></p>

<div class="scroll"><table>
<tr><th>M2 part</th><th>Left out, the tool fills it with…</th><th>In your v0</th></tr>
<tr><td><strong>1 · Fund of knowledge</strong></td><td>the textbook-average topic, in chapter order, at an average level</td><td>KNOWLEDGE</td></tr>
<tr><td><strong>2 · Remember or reason</strong></td><td>explaining everything, so the learner reasons nothing</td><td>HOLD BACK</td></tr>
<tr><td><strong>3 · Load</strong></td><td>long replies, every detail at once</td><td>LIMIT</td></tr>
<tr><td><strong>4 · Misconception</strong></td><td>the right answer, delivered straight past the misconception</td><td>STEPS 3</td></tr>
<tr><td><strong>5 · Measure</strong></td><td>no endpoint: it praises and keeps going</td><td>STOP</td></tr>
</table></div>

<div class="keyline"><p><strong>The closer your file is to your classroom, the less it has to guess.</strong> M2 is the part of the tool you write.</p></div>

<h3>The knowledge file is your fund of knowledge <span class="status">12 min</span></h3>
<p><strong>M2 Part 1.</strong> Write it here; the button below copies it as one document.</p>

<details>
  <summary>See a worked one first: 10th-grade history</summary>
  <div class="scroll"><table>
  <tr><td><strong>Standard</strong></td><td>"Cite specific textual evidence to support analysis of primary and secondary sources, attending to such features as the date and origin of the information." Common Core RH.9-10.1</td></tr>
  <tr><td><strong>Topic list</strong></td><td>① A source's date and origin tell you what its author could know. ② A primary source is evidence of what its author saw and wanted, not proof of what happened. ③ Every author wrote for a purpose and an audience, which shapes what they put in and left out. ④ Two accounts of one event can disagree, and each can be accurate about what its author saw. ⑤ A claim is stronger when sources with different purposes agree.</td></tr>
  <tr><td><strong>Sequence</strong></td><td>① and ② first, on one document; ③ once they can source it without help; ④ and ⑤ need the second document.</td></tr>
  <tr><td><strong>Sources</strong></td><td>the standard above; the two documents; the textbook's civil rights chapter</td></tr>
  <tr><td><strong>Your example</strong></td><td>Two accounts of the May 1963 Woolworth's sit-in in Jackson: the <em>Jackson Daily News</em> report, and Anne Moody's memoir <em>Coming of Age in Mississippi</em> (1968).</td></tr>
  <tr><td><strong>Off limits</strong></td><td>writing their analysis; saying which account is "true"; documents not in this file</td></tr>
  </table></div>
</details>

<div class="do">
  <span class="tag">M2 Part 1 · your knowledge file</span>
  <label for="k_std">Standard — the actual line, quoted, with its source</label>
  <textarea id="k_std" data-save class="short"></textarea>
  <label for="k_topics">Topic list — 4–8 <em>ideas</em>, one per line, each a sentence a learner could get wrong</label>
  <textarea id="k_topics" data-save></textarea>
  <p class="status" style="margin:0">Heading: "The Civil Rights Movement." Idea: "A primary source is evidence of what its author saw and wanted, not proof of what happened." A heading gives the tool nothing to teach and the learner nothing to be wrong about.</p>
  <label for="k_seq">Sequence — the order, and why: what must be in place before the next idea makes sense</label>
  <textarea id="k_seq" data-save class="short"></textarea>
  <label for="k_src">Sources — where each idea comes from, something you can open and check</label>
  <textarea id="k_src" data-save class="short"></textarea>
  <label for="k_ex">Your example — one worked example from your own teaching: your names, your numbers, your documents</label>
  <textarea id="k_ex" data-save class="short"></textarea>
  <label for="k_off">Off limits — what the tool must not teach or answer</label>
  <textarea id="k_off" data-save class="short"></textarea>
  <p><button class="copy" type="button" id="copyKnow">Copy my knowledge file</button> <span id="knowStatus" class="status" role="status" aria-live="polite"></span></p>
</div>

<div class="gotcha"><p><strong>Sources</strong> are things you can open: a textbook chapter, a framework, a protocol, your own problems. A chatbot gives a reconstruction (part 3), so it cannot be one. <strong>Off limits</strong> is the row people skip; health, counselling and safety tools need it most.</p></div>

<h3>M2 in your lane <span class="status">2 min</span></h3>
<p>M2 becomes <strong>two files</strong>: the knowledge file (Part 1) and the v0 prompt (Parts 2–5). Read your own column.</p>
<div class="scroll"><table>
<tr><th>Sit-in tutor</th><th>A · Provider account</th><th>B · OpenRouter</th><th>C · Antigravity</th></tr>
<tr><td><strong>Knowledge file</strong></td><td>upload it as the GPT's, Gem's or Project's knowledge</td><td>paste its text into the system prompt, under the v0</td><td>save as <code>knowledge.md</code>; the page sends it with every message</td></tr>
<tr><td><strong>v0 prompt</strong></td><td>paste into the Instructions box</td><td>paste into the front end's system prompt</td><td>save as <code>prompt.md</code>; the page sends it as the system message</td></tr>
<tr><td><strong>LIMIT</strong></td><td>asked for in the prompt</td><td>the prompt, plus the front end's max-length setting</td><td>the prompt, plus a token cap in code</td></tr>
<tr><td><strong>STOP</strong></td><td>asked for in the prompt</td><td>asked for in the prompt</td><td>a turn counter in code can enforce it</td></tr>
<tr><td><strong>Test it</strong></td><td>the builder's preview chat</td><td>a fresh chat with that system prompt</td><td>open the page</td></tr>
</table></div>
<p>Further right, the build can <strong>enforce</strong> what lane A can only <strong>ask for</strong>. Lane C: never put an API key in a page published to GitHub Pages.</p>
<div class="gotcha"><p><strong>The lane rule:</strong> every lane ships v0 today. If lane B or C is not running yet, build v0 in lane A and move later.</p></div>

<h3>Is it using your file? <span class="status">8 min</span></h3>
<p>A fluent answer proves nothing. Put your file into your tool, add <em>"Teach only from the attached file. If the question is outside it, say so,"</em> and run three tests.</p>

<div class="scroll"><table>
<tr><th>Test</th><th>Do this</th><th>It used the file if…</th></tr>
<tr><td><strong>Tracer</strong></td><td>Ask a question that needs <strong>your example</strong>.</td><td>your example comes back, not a textbook one</td></tr>
<tr><td><strong>Edge</strong></td><td>Ask about something <strong>just outside</strong> the file, in the same subject.</td><td>it says so, instead of answering from training</td></tr>
<tr><td><strong>Quote</strong></td><td>Ask <em>"Which line of the file did you use?"</em> Then <strong>find that line</strong> yourself.</td><td>the line is really there</td></tr>
</table></div>

<div class="do">
  <span class="tag">Write</span>
  <label for="t_tracer">Tracer — did your example come back?</label>
  <textarea id="t_tracer" data-save class="short"></textarea>
  <label for="t_edge">Edge — what did it do with the question just outside the file?</label>
  <textarea id="t_edge" data-save class="short"></textarea>
  <label for="t_quote">Quote — was the line really there?</label>
  <textarea id="t_quote" data-save class="short"></textarea>
  <label for="t_without">Now the same question in a fresh chat <em>without</em> the file. What changed: the vocabulary, the order, the example, what it refused?</label>
  <textarea id="t_without" data-save class="short"></textarea>
</div>

<details>
  <summary>If the tests failed</summary>
  <p>The file is too long, the ideas are headings, or the file was never attached to this chat. All three are fixable now. If nothing changed without the file, it told the tool nothing the internet had not.</p>
</details>

<h3>v0: the system prompt as a worked example <span class="status">8 min</span></h3>
<p>The prompt shows the tool a good tutoring turn, step by step, like a worked example. Fill the blanks and it assembles below. <strong>Each line is an M2 part.</strong></p>

<details>
  <summary>See a worked one first: the sit-in tutor</summary>
<pre>ROLE      You are a Socratic tutor for 10th graders: they can summarise
          a document, cannot yet explain how its author shaped it.

KNOWLEDGE Teach only the ideas in the attached file, in its order.
          Outside the file: say so and send them to their teacher.

STEPS     1. Ask what they think the document says before you explain.
          2. One idea at a time. Check it against the second account.
          3. When they say a source is true because it is primary,
             ask what its author could and could not see.

HOLD BACK Never say which account is more reliable. Give a question,
          then a hint, then one modelled step. Ask them to retrieve
          "date, origin, purpose, audience" instead of reminding them.

LIMIT     At most 60 words per reply. One question per turn.

STOP      End when they explain on their own why the two sit-in
          accounts differ, or after 12 turns: summarise in two lines.</pre>
</details>

<div class="do">
  <span class="tag">Build your v0</span>
  <div class="grid2">
    <div><label for="v_type">Tool type</label><input type="text" id="v_type" data-save placeholder="Socratic tutor"></div>
    <div><label for="v_teacher">Who they go to for anything outside the file</label><input type="text" id="v_teacher" data-save placeholder="their teacher"></div>
    <div><label for="v_can">Your learners can…</label><input type="text" id="v_can" data-save></div>
    <div><label for="v_cannot">…but cannot yet</label><input type="text" id="v_cannot" data-save></div>
    <div><label for="v_mis">When you hear (the misconception, Part 4)</label><input type="text" id="v_mis" data-save></div>
    <div><label for="v_resp">respond by</label><input type="text" id="v_resp" data-save></div>
    <div><label for="v_reason">Never give (what they must reason, Part 2)</label><input type="text" id="v_reason" data-save></div>
    <div><label for="v_remember">Ask them to retrieve (what they must remember)</label><input type="text" id="v_remember" data-save></div>
    <div><label for="v_words">At most how many words per reply? (Part 3)</label><input type="number" id="v_words" data-save min="10" max="400"></div>
    <div><label for="v_turns">End after how many turns?</label><input type="number" id="v_turns" data-save min="2" max="60"></div>
  </div>
  <label for="v_measure">End when the learner… (your measure, Part 5)</label>
  <input type="text" id="v_measure" data-save>
  <pre id="v0out" aria-live="polite"></pre>
  <button class="copy" type="button" data-copy="v0out">Copy my v0</button>
</div>

<p>Now run <strong>one test question</strong> in your tool, with the prompt and the file. That run is your v0.</p>

<!-- ============================================================ -->
<h2 id="agent">5 · Staying the agent <span class="t">8 min</span></h2>

<p>Checkpoint 2, <strong>Generate &amp; Verify</strong>, on your v0. <strong>Change one detail</strong> of your test question (a number, a condition, a name) and ask again. Find the step where it answered <strong>the usual question</strong> instead of <strong>your learner's</strong>:</p>
<ul>
  <li>its step 2 is the textbook's next heading, not your learner's next need;</li>
  <li>it names the misconception, then explains the right idea instead of asking;</li>
  <li>it praises and moves on without checking.</li>
</ul>
<p>Then, quickly:</p>
<label class="chk"><input type="checkbox" id="c_know" data-save> Every claim came from the file. (If not: does the file say it at all, or only as a heading?)</label>
<label class="chk"><input type="checkbox" id="c_hold" data-save> It held back what the learner must reason.</label>
<label class="chk"><input type="checkbox" id="c_limit" data-save> It stayed under my word limit. (Count.)</label>

<div class="gotcha"><p><strong>Your documentation log starts with M2.</strong> At each checkpoint, the decision and the reason, in your own words. A reason pasted from the tool is a reason you did not make.</p></div>

<!-- ============================================================ -->
<h2 id="exit">6 · Exit card, then Milestone 2 <span class="t">4 min</span></h2>

<p>The week's Engagement Check, and the first draft of M2 Part 5's last paragraph.</p>

<div class="do">
  <span class="tag">Exit card</span>
  <label for="x_test">1 · Your test question, and the first two lines of the tool's answer</label>
  <textarea id="x_test" data-save></textarea>
  <label for="x_step">2 · The step where its reasoning pattern-matched</label>
  <textarea id="x_step" data-save class="short"></textarea>
  <label for="x_fix">3 · The one line you will change in the prompt or the file before M3</label>
  <textarea id="x_fix" data-save class="short"></textarea>
</div>

<p class="no-print">
  <button id="copyAll" type="button">Copy all my answers</button>
  <button class="ghost" type="button" onclick="window.print()">Print / save as PDF</button>
  <span id="copyStatus" role="status" aria-live="polite" class="status"></span>
</p>
<p>Paste it into the <strong>Week 9 Engagement Check</strong>. Only the exit card is scored; the rest, including your knowledge file and v0, is your record.</p>

<h3>Then: Milestone 2, in the Week 9 module</h3>
<p>One page, plus your knowledge file and v0; instructions and rubric are in the module. Three of the five parts are already in your Readiness Checks.</p>
<ol>
  <li><strong>The fund of knowledge</strong> — the table you just wrote</li>
  <li><strong>Remember, or reason?</strong> — your HOLD BACK line</li>
  <li><strong>How the tool manages load</strong> — Week 6's load budget, and your LIMIT line</li>
  <li><strong>The misconception</strong> — Week 7's exemplar rule, and STEPS line 3</li>
  <li><strong>The measure, and v0</strong> — Week 8's wild item, and this exit card</li>
</ol>
<p><strong>Peer feedback:</strong> run your partner's v0, and tell them what a learner would have to know already for it to work.</p>

<!-- ============================================================ -->
<footer class="footer">
  <p><strong>Sources and credits</strong></p>
  <ul>
    <li>IBM Technology (Keen, M.). <em>AI vs Human Thinking: How Large Language Models Really Work.</em> YouTube. <a href="https://www.youtube.com/watch?v=-ovM0daP6bw">youtube.com/watch?v=-ovM0daP6bw</a>. Embedded under YouTube's standard embed terms.</li>
    <li>Engineering Visualized. <em>How AI Learned to Reason — From Next Token Prediction to Reasoning Models.</em> YouTube. <a href="https://www.youtube.com/watch?v=hoPF9QbeGdc">youtube.com/watch?v=hoPF9QbeGdc</a>. Embedded under YouTube's standard embed terms.</li>
    <li>Liu, N. F., et al. (2024). Lost in the middle: How language models use long contexts. <em>Transactions of the ACL, 12</em>, 157–173. The curve on this page is an illustrative redrawing, not their data.</li>
    <li>Levesque, H., Davis, E., &amp; Morgenstern, L. (2012). The Winograd schema challenge. <em>KR.</em> (The trophy and the suitcase.)</li>
    <li>Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. <em>NeurIPS.</em></li>
    <li>Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. <em>NeurIPS.</em> · Turpin, M., et al. (2023). Language models don't always say what they think. <em>NeurIPS.</em> · McCoy, R. T., et al. (2024). Embers of autoregression. <em>PNAS, 121</em>(41). · Dziri, N., et al. (2023). Faith and fate: Limits of transformers on compositionality. <em>NeurIPS.</em></li>
    <li>Austin, T. <em>UnBlooms™ — The Reflective Checkpoint Process.</em> <a href="https://tinaaustin.com/">tinaaustin.com</a>. Checkpoint 2, Generate &amp; Verify, is hers.</li>
    <li>Workshop design: Andy Parra-Martinez, EPY 3143, Mississippi State University. This page was drafted with Claude (Anthropic) from the in-person workshop deck and reviewed by the instructor. It runs entirely in your browser; nothing you type leaves this device.</li>
  </ul>
</footer>

<script>
(function(){
  var KEY='epy3143-w9-workshop2-online';
  var fields=Array.prototype.slice.call(document.querySelectorAll('[data-save]'));
  var saveStatus=document.getElementById('saveStatus');
  function getv(f){ return (f.type==='checkbox'||f.type==='radio') ? f.checked : f.value; }
  function setv(f,v){ if(f.type==='checkbox'||f.type==='radio') f.checked=!!v; else f.value=v; }
  function load(){
    var data={};
    try{data=JSON.parse(localStorage.getItem(KEY)||'{}')||{};}catch(e){data={};}
    fields.forEach(function(f){ if(data[f.id]!==undefined) setv(f,data[f.id]); });
    if(saveStatus) saveStatus.textContent = Object.keys(data).length ? 'Restored your saved answers from this browser.' : 'Saves in this browser as you type.';
  }
  var t;
  function save(){
    var data={};
    fields.forEach(function(f){ data[f.id]=getv(f); });
    try{localStorage.setItem(KEY,JSON.stringify(data)); if(saveStatus) saveStatus.textContent='Saved in this browser.';}
    catch(e){ if(saveStatus) saveStatus.textContent='Could not save in this browser — copy your answers before you leave.'; }
  }
  function changed(){ clearTimeout(t); t=setTimeout(save,300); score(); buildV0(); }
  fields.forEach(function(f){ f.addEventListener('input',changed); f.addEventListener('change',function(){save();score();buildV0();}); });

  var v=function(id){ var e=document.getElementById(id); return (e&&e.value||'').trim(); };

  // --- overload me: kept by position ---
  function score(){
    var kept=function(a,b){ var n=0; for(var i=a;i<=b;i++){ if(document.getElementById('r'+i).checked) n++; } return n; };
    var f=kept(1,3), m=kept(4,9), l=kept(10,12), any=f+m+l;
    var el=document.getElementById('ovScore');
    el.innerHTML = any ? 'Kept — first three: <b>'+f+'/3</b> · middle six: <b>'+m+'/6</b> · last three: <b>'+l+'/3</b>' : 'Tick the rules it kept.';
  }

  // --- v0 builder ---
  function slot(id,ph){ return v(id)||'['+ph+']'; }
  function buildV0(){
    var out=
'ROLE      You are a '+slot('v_type','tool type')+' for learners who can '+slot('v_can','___')+',\n'+
'          but cannot yet '+slot('v_cannot','___')+'.\n\n'+
'KNOWLEDGE Teach only the ideas in the attached file, in its order.\n'+
'          Outside the file: say so and send them to '+slot('v_teacher','the teacher')+'.\n\n'+
'STEPS     1. Ask what the learner already thinks before you explain.\n'+
'          2. One idea at a time. Check it before moving on.\n'+
'          3. When you hear '+slot('v_mis','the misconception')+', respond by '+slot('v_resp','___')+'.\n\n'+
'HOLD BACK Never give '+slot('v_reason','what they must reason')+'. Give a question,\n'+
'          then a hint, then one worked step. Ask them to retrieve\n'+
'          '+slot('v_remember','what they must remember')+' instead of reminding them.\n\n'+
'LIMIT     At most '+slot('v_words','N')+' words per reply. One question per turn.\n\n'+
'STOP      End when the learner '+slot('v_measure','does the measure')+', or after\n'+
'          '+slot('v_turns','N')+' turns: summarise in two lines and send them back.';
    document.getElementById('v0out').textContent=out;
    return out;
  }

  function knowFile(){
    return ['KNOWLEDGE FILE','','STANDARD',v('k_std')||'—','','TOPIC LIST (ideas, in order)',v('k_topics')||'—','',
      'SEQUENCE',v('k_seq')||'—','','SOURCES',v('k_src')||'—','','EXAMPLE',v('k_ex')||'—','','OFF LIMITS',v('k_off')||'—'].join('\n');
  }

  // --- copy ---
  function copyText(txt,status){
    var done=function(ok){ if(status) status.textContent= ok?'Copied.':'Could not copy — select the text and copy it by hand.'; };
    if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(function(){done(true)},function(){done(false)}); }
    else{ try{ var ta=document.createElement('textarea'); ta.value=txt; document.body.appendChild(ta); ta.select(); var ok=document.execCommand('copy'); document.body.removeChild(ta); done(ok);}catch(e){done(false);} }
  }
  Array.prototype.forEach.call(document.querySelectorAll('[data-copy]'),function(b){
    b.addEventListener('click',function(){ var src=document.getElementById(b.getAttribute('data-copy')); copyText(src.textContent, null); var old=b.textContent; b.textContent='Copied'; setTimeout(function(){b.textContent=old;},1500); });
  });
  document.getElementById('copyKnow').addEventListener('click',function(){ copyText(knowFile(), document.getElementById('knowStatus')); });
  document.getElementById('copyAll').addEventListener('click',function(){
    var d=function(id){ return v(id)||'—'; };
    var kept=[]; for(var i=1;i<=12;i++){ if(document.getElementById('r'+i).checked) kept.push(i); }
    var tf=document.getElementById('tf_t').checked?'true':(document.getElementById('tf_f').checked?'false':'—');
    var checks=[['c_know','claims from the file'],['c_hold','held back'],['c_limit','under the limit']].map(function(c){ return c[1]+': '+(document.getElementById(c[0]).checked?'yes':'no'); }).join(' · ');
    var out=['EPY 3143 · Week 9 · Workshop 2 (online) — my answers','',
      'EXIT CARD','Test question and first two lines: '+d('x_test'),'Where it pattern-matched: '+d('x_step'),'The one change before M3: '+d('x_fix'),'',
      'Running out of room: '+d('q_room'),
      'Trophy/suitcase: '+d('q_it1')+' / '+d('q_it2'),
      'Reads the internet? I said '+tf,'Dense, my standard: '+d('q_quote1'),'Thin, classroom only: '+d('q_quote3'),'After pasting: '+d('q_quote2'),
      'Bat and ball: '+d('q_bb1'),'Sit-in ask — questions vs explanations: '+d('q_bb2'),'My own subject, help without the answer: '+d('q_reason'),
      'Overload me — rules kept: '+(kept.join(', ')||'—'),'',
      'Is it using my file?','Tracer: '+d('t_tracer'),'Edge: '+d('t_edge'),'Quote: '+d('t_quote'),'Without the file: '+d('t_without'),'',
      'Staying the agent — '+checks,'',
      knowFile(),'','V0 PROMPT',buildV0()].join('\n');
    copyText(out, document.getElementById('copyStatus'));
  });

  load(); score(); buildV0();
})();
</script>
</body>
</html>
'''

open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, len(HTML)//1024, "KB")
