#!/usr/bin/env python3
"""Assemble w4/index.html — the self-guided Workshop 4. Edit here, run, commit both.

The stylesheet is taken from w2/build_index.py so the pages stay one design.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "index.html")
W2 = open(os.path.join(HERE, "..", "w2", "build_index.py"), encoding="utf-8").read()
CSS = re.search(r"<style>(.*?)</style>", W2, re.S).group(1)

# id, name, how to test a page, the line for SKILL.md when there is no page yet
ACCESS = [
    ("listen", "Reading aloud",
     "Open your page in Microsoft Edge and press Ctrl+Shift+U (Mac: Command+Shift+U). Close your eyes and listen. Can you answer the question using only what you hear?",
     "Every question, answer choice and reply can be read aloud."),
    ("keys", "Keyboard only",
     "Use only the Tab, Enter and Space keys. Can you reach every button? Can you see which button is selected?",
     "Everything works from the keyboard, and the selected button is easy to see."),
    ("zoom", "Zoom at 200%",
     "Press Ctrl and + (Mac: Command and +) until the browser shows 200%. Is any text cut off?",
     "The page still works at 200% zoom and on a phone."),
    ("color", "Color",
     "Take a screenshot and view it in black and white. Can you still tell correct answers from incorrect ones? Then check your text colors with the <a href='https://webaim.org/resources/contrastchecker/'>WebAIM contrast checker</a>. Normal text needs a contrast ratio of at least 4.5 to 1.",
     "Words tell the learner whether an answer is correct. Color only repeats the message."),
    ("pics", "Pictures and video",
     "Cover each picture. Does the text give the learner the information in the picture? Play each video without sound. Does it have captions?",
     "Every picture has a description. Every video has captions."),
    ("words", "Vocabulary",
     "List the difficult words. Keep the words that your lesson teaches. For the other words, can the learner find a short definition?",
     "Define any difficult word that the lesson does not teach. Keep every word that the lesson teaches."),
    ("load", "Amount of information",
     "Look at one screen or one reply. How many things does the learner have to do? Is there a timer? Can the learner go back?",
     "Show one question per screen or reply. Do not use a timer. Let the learner go back."),
]


def access_cards():
    out = []
    for k, name, test, rule in ACCESS:
        out.append(
            f'<fieldset class="check"><legend>{name}</legend>\n'
            f'<p><strong>If you have a page:</strong> {test}</p>\n'
            f'<p><strong>If you have only SKILL.md:</strong> does the file include a line like this one? <em>"{rule}"</em></p>\n'
            f'<label for="a_{k}">What you found</label>\n'
            f'<select id="a_{k}" data-save><option value="">Choose</option><option>Works</option>'
            f'<option>Excludes some learners</option><option>Does not apply to my tool</option></select>\n</fieldset>')
    return "\n".join(out)


EXTRA = """
.card,.cols{margin-bottom:1rem}
.cols .card{margin-bottom:0}
fieldset.check + label{margin-top:1.4rem}
fieldset.check{border:1px solid var(--rule);border-radius:6px;padding:.6rem 1rem .9rem;margin:1rem 0;background:var(--surface)}
fieldset.check legend{font-weight:700;color:var(--maroon);padding:0 .4em}
fieldset.check p{margin:0 0 .5rem;font-size:.95em}
fieldset.check label{margin:.4rem 0 .2rem}
.locked[hidden]{display:none}
.opts{display:flex;flex-wrap:wrap;gap:.5rem;margin:.6rem 0}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) button:not(.ghost){color:#171215}}
"""

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Who does your tool leave out?</title>
<meta name="description" content="EPY 3143 Workshop 4, self-guided: three learners, an access and challenge review, five ethics rules, and two changes to your tool.">
<style>__CSS__</style>
</head>
<body>

<header class="head">
  <p class="moment">EPY 3143 · Week 15 · Workshop 4 · Both sections</p>
  <h1>Who does your tool leave out?</h1>
  <p class="sub">This self-guided workshop takes about an hour. You will study three learners, review your tool for access and challenge, write five ethics rules, and make two changes.</p>
</header>

<div class="keyline">
  <span class="tag">How this page works</span>
  <p>Complete the sections in order. You need your <strong>SKILL.md</strong> from Milestone 3 and your access rule from the <strong>Week 14 workbench</strong> (Part 6). If your tool is already a page, open it too.</p>
  <p>You don't need to install anything or use AI. Your answers are saved only in this browser. At the end, copy them with one button and paste them into <strong>Self-guided Workshop 4</strong> in Canvas.</p>
  <p><span id="saveStatus" role="status" aria-live="polite" class="status"></span></p>
</div>

<ol class="toc">
  <li><a href="#deal">Purpose and key terms</a> <span class="status">4 min</span></li>
  <li><a href="#three">Three learners</a> <span class="status">12 min</span></li>
  <li><a href="#setting">How the setting matters</a> <span class="status">7 min</span></li>
  <li><a href="#traps">Two common mistakes</a> <span class="status">5 min</span></li>
  <li><a href="#access">Access review</a> <span class="status">12 min</span></li>
  <li><a href="#challenge">Challenge review</a> <span class="status">6 min</span></li>
  <li><a href="#ethics">Five ethics rules</a> <span class="status">6 min</span></li>
  <li><a href="#change">Two changes and a test</a> <span class="status">8 min</span></li>
  <li><a href="#exit">Exit card and Milestone 4</a> <span class="status">3 min</span></li>
</ol>

<!-- ============================================================ -->
<h2 id="deal">1 · Purpose and key terms <span class="t">4 min</span></h2>

<p>When we design a tool, we imagine a learner. We assume that this learner can read the text, type an answer, and benefit from the questions we wrote. Other learners will also use the tool, and some of those assumptions will be wrong for them. In this workshop, you identify those learners and revise your tool for them.</p>
<p>We will use three terms:</p>
<ul>
  <li><strong>Barrier:</strong> a feature of the tool that stops learners from showing what they can do. For example, a page that has only text is a barrier for a student with dyslexia.</li>
  <li><strong>Bar:</strong> the learning goal and the thinking it requires.</li>
  <li><strong>Ceiling:</strong> the most challenging work the tool offers. A low ceiling leaves advanced learners with nothing new to learn.</li>
</ul>
<p>In Week 14, you learned to <strong>lower the barrier and keep the bar</strong>. In this workshop, you also learn to <strong>raise the ceiling</strong>.</p>
<label for="q_default">Describe in one sentence the learner you imagined when you designed your tool. What does your tool assume this learner can already do?</label>
<textarea id="q_default" data-save class="short"></textarea>

<!-- ============================================================ -->
<h2 id="three">2 · Three learners <span class="t">12 min</span></h2>

<p>The three 8th graders below are fictional. All of them used the demo tool from Workshop 3, <em>Where Does Confidence Come From?</em> The tool presents eight short scenes. For each scene, the learner chooses one of four sources of self-efficacy.</p>

<div class="card">
  <h3 style="margin-top:0">Jonah</h3>
  <p><strong>School record:</strong> Jonah has dyslexia and an IEP. His accommodations are extra time and text-to-speech on tests.</p>
  <p><strong>Results with the tool:</strong> He answered 3 of 8 scenes correctly in 14 minutes.</p>
  <p><strong>Teacher's observation:</strong> When his teacher read a scene aloud, Jonah answered before she finished. Then he asked, "If you watch a video of yourself doing it, is that mastery or vicarious?"</p>
  <label for="c_jonah">What is the barrier for Jonah, and what is the bar? What would you add to the tool?</label>
  <textarea id="c_jonah" data-save class="short"></textarea>
</div>

<div class="card" style="margin-top:1rem">
  <h3 style="margin-top:0">Imani</h3>
  <p><strong>School record:</strong> Imani reads two grades above level and earns top scores on every test. She has no IEP, 504 plan or gifted services.</p>
  <p><strong>Results with the tool:</strong> She answered 8 of 8 scenes correctly in three minutes. Then she closed the page.</p>
  <p><strong>Teacher's observation:</strong> Students wrote a paragraph after using the tool, and Imani turned in one line. In the class discussion, she explained the same idea for two minutes and gave an original example.</p>
  <label for="c_imani">What did Imani learn from the tool? What would you add?</label>
  <textarea id="c_imani" data-save class="short"></textarea>
</div>

<div class="card" style="margin-top:1rem">
  <h3 style="margin-top:0">Rafa</h3>
  <p><strong>School record:</strong> Rafa's grades and test scores are average. He has never been referred for an evaluation.</p>
  <p><strong>Results with the tool:</strong> On Monday, he read silently in English class and answered 4 of 8 scenes correctly.</p>
  <p><strong>Coach's observation:</strong> On Thursday, the robotics coach read the same eight scenes aloud as a game. Rafa answered all eight correctly. He then invented a ninth scene in which two sources of self-efficacy conflict.</p>
  <label for="c_rafa">Rafa worked with the same eight scenes on both days. What was different in robotics club?</label>
  <textarea id="c_rafa" data-save class="short"></textarea>
</div>

<div class="do">
  <span class="tag">Write your answer first</span>
  <label for="c_both">Which of these learners might be twice-exceptional (2e)? Cite the evidence that supports your answer. Explain what the setting showed about that learner and what it hid.</label>
  <textarea id="c_both" data-save></textarea>
  <button type="button" id="showBoth">Show the explanation</button>
  <span id="bothStatus" role="status" aria-live="polite" class="status"></span>
</div>

<div id="bothAnswer" class="locked" hidden tabindex="-1">
  <p><strong>Any of the three learners could be twice-exceptional.</strong> Jonah has an identified disability, and he asks a question we would expect from an advanced learner. Imani is academically advanced, and her writing is much weaker than her speaking. Rafa has no identification. His strength and his difficulty may be hiding each other.</p>
  <p>You studied these three patterns in Week 14 (Baum et al., 2017). Their cases also show that <strong>the setting influences what teachers see</strong>. Work that depends on print can reveal a reading difficulty. Work that depends on oral reasoning can reveal a talent. When a student compensates for the difficulty and receives little challenge, teachers may see average performance.</p>
  <div class="scroll"><table>
  <tr><th scope="col">Learner</th><th scope="col">Setting that shows the difficulty</th><th scope="col">Setting that shows the strength</th></tr>
  <tr><td>Jonah</td><td>Reading eight scenes in print</td><td>Listening to a scene and asking questions</td></tr>
  <tr><td>Imani</td><td>Writing a paragraph alone</td><td>Discussing the idea in class</td></tr>
  <tr><td>Rafa</td><td>Reading silently in English class</td><td>Listening, speaking and inventing a scene in robotics club</td></tr>
  </table></div>
  <div class="gotcha"><p><strong>These observations are not diagnoses.</strong> They give a teacher a reason to talk with the family and consider a referral for evaluation. Your tool should never suggest a diagnosis.</p></div>
</div>

<!-- ============================================================ -->
<h2 id="setting">3 · How the setting matters <span class="t">7 min</span></h2>

<p>Your tool is also a setting. The way it asks learners to respond influences which strengths and difficulties it shows. The example below is one scene from the demo tool with two added options, <em>Read aloud</em> and <em>Go deeper</em>. Try both.</p>

<div class="card" id="demo">
  <h3 style="margin-top:0">Where does Rosa's confidence come from?</h3>
  <p id="scene">Rosa missed every free throw in October. She practiced each day after school. Now she makes six of ten, and she asks to shoot in the game.</p>
  <div class="opts">
    <button type="button" class="ghost" id="speak">Read aloud</button>
    <button type="button" class="ghost" id="deeperBtn" aria-expanded="false" aria-controls="deeper">Go deeper</button>
  </div>
  <p id="speakStatus" role="status" aria-live="polite" class="status"></p>
  <div class="opts" role="group" aria-label="Choose a source of confidence">
    <button type="button" class="ans" data-a="m">Mastery experience</button>
    <button type="button" class="ans" data-a="v">Vicarious experience</button>
    <button type="button" class="ans" data-a="p">Verbal persuasion</button>
    <button type="button" class="ans" data-a="e">Physiological and emotional state</button>
  </div>
  <p id="demoFb" role="status" aria-live="polite"></p>
  <div id="deeper" hidden>
    <p id="deeperText">On Friday, Rosa's coach says, "I knew you could do it." The scene now includes two sources of confidence. On Saturday, Rosa misses her first five shots. Which source is more likely to support her confidence now? Use evidence from the scene to explain your answer.</p>
    <button type="button" class="ghost" id="speak2">Read this aloud</button>
  </div>
</div>

<p><em>Read aloud</em> lowers the barrier, and <em>Go deeper</em> raises the ceiling. The learning goal stays the same because every learner still has to identify the source of confidence.</p>
<p>Both options are available to all learners, so nobody has to disclose a disability to use them. This design follows Universal Design for Learning, which keeps the goal firm and offers flexible ways to reach it (CAST, 2024).</p>
<p>The challenge also needs to be accessible. Rafa may choose <em>Go deeper</em> and still need to hear the question, so the more difficult question has its own read-aloud button.</p>
<label for="q_setting">What does your tool ask learners to do most often: read, type, speak, or reason? Which learners would have difficulty showing what they know in that setting?</label>
<textarea id="q_setting" data-save class="short"></textarea>

<!-- ============================================================ -->
<h2 id="traps">4 · Two common mistakes <span class="t">5 min</span></h2>

<p>AI tools can make two mistakes when we ask them to adapt a lesson. The replies below are examples written for this workshop.</p>

<div class="cols">
  <div class="card">
    <h3 style="margin-top:0">Mistake 1: Simplifying the thinking</h3>
    <p><strong>Request:</strong> Make Rosa's scene accessible for a student with dyslexia.</p>
    <p><strong>AI reply:</strong> "Rosa practiced and got better! (Mastery experience)"</p>
    <p>The reply removes the evidence and gives the answer. Jonah no longer has to reason about the scene.</p>
  </div>
  <div class="card">
    <h3 style="margin-top:0">Mistake 2: Adding more of the same work</h3>
    <p><strong>Request:</strong> Make this harder for an advanced student.</p>
    <p><strong>AI reply:</strong> "Here are 20 more scenes to sort!"</p>
    <p>Imani already showed that she can sort the scenes. The additional scenes give her more work without new learning.</p>
  </div>
</div>

<p><strong>To avoid the first mistake, keep the content and provide another way to access it.</strong> A meta-analysis of 22 studies found that text-to-speech and other read-aloud tools improved the reading comprehension of students with reading disabilities (<em>d</em> = 0.35; Wood et al., 2018).</p>
<p><strong>To avoid the second mistake, let students skip what they know and offer deeper work.</strong> In a national study of 336 high-ability students in grades 2 to 6, teachers eliminated content that students had already mastered. The achievement scores of these students did not differ significantly from the scores of students who completed all of the content (Reis et al., 1998).</p>
<p><strong>For a twice-exceptional learner, provide access and challenge together.</strong> If we only simplify the work, we remove the challenge. If we only add challenge, the barrier remains.</p>

<!-- ============================================================ -->
<h2 id="access">5 · Access review <span class="t">12 min</span></h2>

<p>Complete seven checks of your tool. Do each check yourself, because an AI tool may report that a page is accessible when it is not.</p>
<p>If your tool is a chatbot, check the chat window and one of its replies. If you have only a SKILL.md, check whether the file includes the rule.</p>
__ACCESS__
<label for="a_worst">Which of these problems would exclude the most learners? Describe one learner and explain what would happen to that learner.</label>
<textarea id="a_worst" data-save class="short"></textarea>

<!-- ============================================================ -->
<h2 id="challenge">6 · Challenge review <span class="t">6 min</span></h2>

<p>Use your tool as Imani would. Answer every question correctly and quickly. Then check each statement that is true of your tool.</p>
<label class="chk"><input type="checkbox" id="h_skip" data-save> The tool recognizes that I know the content and lets me skip ahead.</label>
<label class="chk"><input type="checkbox" id="h_deep" data-save> The more difficult questions ask me to think in a new way: compare, defend, find an exception, or create an example.</label>
<label class="chk"><input type="checkbox" id="h_more" data-save> The tool does not give me more of the same work when I answer correctly.</label>
<label class="chk"><input type="checkbox" id="h_fast" data-save> The tool does not reward speed.</label>
<label class="chk"><input type="checkbox" id="h_open" data-save> Any learner can choose the challenge.</label>
<label class="chk"><input type="checkbox" id="h_both" data-save> The access options also work in the challenge questions.</label>

<p>Each statement you left unchecked is something you can improve. Complete the sentence below to write a challenge rule for your tool.</p>
<div class="prompt"><em>When the learner</em> ____ (something the tool can observe)<em>, the tool skips</em> ____ <em>and asks</em> ____. <em>It never</em> ____.</div>
<label for="h_rule">Your challenge rule</label>
<p class="status" id="h_ex">Example: "When the learner gets the first three scenes right, the tool skips to the two-source scenes and asks which source would last. It never adds more one-source scenes."</p>
<textarea id="h_rule" data-save class="short" aria-describedby="h_ex"></textarea>

<!-- ============================================================ -->
<h2 id="ethics">7 · Five ethics rules <span class="t">6 min</span></h2>

<p>Ethics rules protect the people who use your tool. Write one rule for each area below as an <strong>if-then</strong> sentence, and add the rules to the guardrails in your SKILL.md. The disclosure rule can be a statement.</p>

<label for="e_label">1 · Label: What does the tool do when a learner mentions a diagnosis? It should never ask for a diagnosis or guess one.</label>
<p class="status" id="e_label_ex">Example: "If the learner says 'I have dyslexia,' offer the read-aloud and keep every question the same. Never make the work easier because of a label."</p>
<textarea id="e_label" data-save class="short" aria-describedby="e_label_ex"></textarea>

<label for="e_data">2 · Data: What information should learners never enter?</label>
<p class="status" id="e_data_ex">Example: "If the learner types a name, a grade or a health detail, do not repeat it. Ask the learner to leave it out."</p>
<textarea id="e_data" data-save class="short" aria-describedby="e_data_ex"></textarea>

<label for="e_disc">3 · Disclosure: How will learners know that the tool uses AI or was built with AI?</label>
<p class="status" id="e_disc_ex">Example: "The first screen says: I was built with AI, and I can be wrong." A chatbot should say that it is an AI.</p>
<textarea id="e_disc" data-save class="short" aria-describedby="e_disc_ex"></textarea>

<label for="e_hon">4 · Honesty: What should the tool never claim to be or to do?</label>
<p class="status" id="e_hon_ex">Example: "If the learner asks for a grade, say: I don't grade. Show this to your teacher."</p>
<textarea id="e_hon" data-save class="short" aria-describedby="e_hon_ex"></textarea>

<label for="e_fair">5 · Fairness: Which learners could be harmed if the tool makes a mistake?</label>
<p class="status" id="e_fair_ex">Example: "If the learner writes in another language or with misspellings, respond to the idea first."</p>
<textarea id="e_fair" data-save class="short" aria-describedby="e_fair_ex"></textarea>

<p>The label rule deserves special attention. Ophélie Desmet and I warn that an AI system may receive a disability label and quietly lower its expectations in every area (Parra-Martinez &amp; Desmet, 2026). One tool can repeat this mistake with many students.</p>

<!-- ============================================================ -->
<h2 id="change">8 · Two changes and a test <span class="t">8 min</span></h2>

<p>Use your two reviews to make two changes in <code>SKILL.md</code>. If your tool is a page, change the page too.</p>

<h3>Change 1: Lower one barrier</h3>
<label for="k1_before">The line before your change</label><textarea id="k1_before" data-save class="short"></textarea>
<label for="k1_after">The line after your change</label><textarea id="k1_after" data-save class="short"></textarea>
<label for="k1_how">How did you check that the change helps? What stayed the same?</label><textarea id="k1_how" data-save class="short"></textarea>

<h3>Change 2: Raise the ceiling</h3>
<label for="k2_before">The line before your change</label><textarea id="k2_before" data-save class="short"></textarea>
<label for="k2_after">The line after your change</label><textarea id="k2_after" data-save class="short"></textarea>
<label for="k2_how">How did you check that the new question requires deeper thinking? What does the learner skip?</label><textarea id="k2_how" data-save class="short"></textarea>

<h3>Combined test</h3>
<p>Test your tool as if you were Rafa. Use the access option <strong>and</strong> choose the challenge in the same turn. You can run the test with an AI, or ask another person to answer as your tool by following your SKILL.md.</p>
<label for="k3_test">What did the learner do? How did the tool respond? Did both rules work?</label>
<textarea id="k3_test" data-save></textarea>

<details><summary>Optional: ask an AI agent to review your tool</summary>
<p>Complete your own review first. The agent will report possible problems. Test each problem yourself before you decide what to change.</p>
<pre id="p6">Read skill/SKILL.md, and docs/index.html if it exists. Report the problems
you find. Do not fix anything yet. Quote the line for each problem.
1. Access: read aloud, keyboard, zoom, color, pictures and video,
   vocabulary, amount of information.
2. Challenge: where does a learner who already knows the content get
   stuck or receive more of the same work?
3. Access and challenge: do the access options work in the harder items?
4. Ethics: label, data, disclosure, honesty, fairness.
Never suggest making the thinking easier. Never suggest asking the
learner for a diagnosis. I will choose what to fix, one item at a time.</pre>
<button class="copy" type="button" id="copyP6">Copy the prompt</button> <span id="p6Status" role="status" aria-live="polite" class="status"></span>
</details>

<!-- ============================================================ -->
<h2 id="exit">9 · Exit card and Milestone 4 <span class="t">3 min</span></h2>

<div class="do">
  <span class="tag">Exit card</span>
  <label for="x_out">1 · Describe one learner your tool excluded before this workshop. Copy the line that now includes that learner.</label>
  <textarea id="x_out" data-save class="short"></textarea>
  <label for="x_both">2 · Describe one situation in which your access rule and your challenge rule could conflict. How did you address it?</label>
  <textarea id="x_both" data-save class="short"></textarea>
</div>

<p class="no-print">
  <button id="copyAll" type="button">Copy all my answers</button>
  <button class="ghost" type="button" onclick="window.print()">Print / save as PDF</button>
  <span id="copyStatus" role="status" aria-live="polite" class="status"></span>
</p>
<p>Paste your answers into <strong>Self-guided Workshop 4</strong> in Canvas.</p>

<h3>Milestone 4</h3>
<p>Your answers on this page are a first draft of Milestone 4. The instructions, rubric and deadline are in Canvas. The milestone has five parts:</p>
<ol>
  <li><strong>The barrier:</strong> a learner with a disability and a rule that provides access to the same goal.</li>
  <li><strong>The ceiling:</strong> an advanced learner and a rule that provides deeper work.</li>
  <li><strong>Access and challenge together:</strong> a twice-exceptional learner in two settings and one rule that addresses both needs.</li>
  <li><strong>Ethics:</strong> five rules for your tool.</li>
  <li><strong>Two changes and the combined test.</strong></li>
</ol>

<!-- ============================================================ -->
<footer class="footer">
  <p><strong>Sources and credits</strong></p>
  <ul>
    <li>Baum, S. M., Schader, R. M., &amp; Owen, S. V. (2017). <em>To be gifted and learning disabled</em> (3rd ed.). Prufrock Press.</li>
    <li>CAST. (2024). <em>Universal Design for Learning guidelines</em> (Version 3.0). <a href="https://udlguidelines.cast.org">udlguidelines.cast.org</a></li>
    <li>Eggen, P. D., &amp; Kauchak, D. P. (2025). <em>Using educational psychology in teaching</em> (12th ed.). Pearson. Chapters 4 and 5.</li>
    <li>Parra-Martinez, F. A., &amp; Desmet, O. A. (2026). Offload, surrender, or augment? Designing continuous talent development in the age of AI. <em>Gifted Education International.</em> Advance online publication.</li>
    <li>Reis, S. M., Baum, S. M., &amp; Burke, E. (2014). An operational definition of twice-exceptional learners: Implications and applications. <em>Gifted Child Quarterly, 58</em>(3), 217–230. <a href="https://doi.org/10.1177/0016986214534976">doi.org/10.1177/0016986214534976</a></li>
    <li>Reis, S. M., Westberg, K. L., Kulikowich, J. M., &amp; Purcell, J. H. (1998). Curriculum compacting and achievement test scores: What does the research say? <em>Gifted Child Quarterly, 42</em>(2), 123–129. <a href="https://doi.org/10.1177/001698629804200206">doi.org/10.1177/001698629804200206</a></li>
    <li>Wood, S. G., Moxley, J. H., Tighe, E. L., &amp; Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. <em>Journal of Learning Disabilities, 51</em>(1), 73–84. <a href="https://doi.org/10.1177/0022219416688170">doi.org/10.1177/0022219416688170</a></li>
    <li>World Wide Web Consortium. (2018). <em>Web Content Accessibility Guidelines (WCAG) 2.1.</em> <a href="https://www.w3.org/TR/WCAG21/">w3.org/TR/WCAG21</a> (used for the contrast, keyboard, zoom and caption checks).</li>
    <li>Workshop design: Andy Parra-Martinez, EPY 3143, Mississippi State University. I drafted this page with Claude (Anthropic), then reviewed it. The page runs in your browser, and your answers stay on this device.</li>
  </ul>
</footer>

<script>
(function(){
  var KEY='epy3143-w15-workshop4';
  var $=function(id){ return document.getElementById(id); };
  var fields=Array.prototype.slice.call(document.querySelectorAll('[data-save]'));
  var saveStatus=$('saveStatus');
  function getv(f){ return f.type==='checkbox' ? f.checked : f.value; }
  function setv(f,v){ if(f.type==='checkbox') f.checked=!!v; else f.value=v; }
  function load(){
    var data={};
    try{ data=JSON.parse(localStorage.getItem(KEY)||'{}')||{}; }catch(e){ data={}; }
    fields.forEach(function(f){ if(data[f.id]!==undefined) setv(f,data[f.id]); });
    saveStatus.textContent = Object.keys(data).length ? 'Restored your saved answers from this browser.' : 'Saves in this browser as you type.';
  }
  var t;
  function save(){
    var data={};
    fields.forEach(function(f){ data[f.id]=getv(f); });
    try{ localStorage.setItem(KEY,JSON.stringify(data)); saveStatus.textContent='Saved in this browser.'; }
    catch(e){ saveStatus.textContent='Could not save in this browser. Copy your answers before you leave.'; }
  }
  fields.forEach(function(f){ f.addEventListener('input',function(){ clearTimeout(t); t=setTimeout(save,300); }); f.addEventListener('change',save); });

  $('showBoth').addEventListener('click',function(){
    if($('c_both').value.trim().length<40){ $('bothStatus').textContent='Write your answer first. One or two sentences are enough.'; $('c_both').focus(); return; }
    $('bothStatus').textContent=''; $('bothAnswer').hidden=false; $('bothAnswer').focus();
  });

  function speak(ids){
    if(!('speechSynthesis' in window)){ $('speakStatus').textContent='This browser cannot read aloud. Try Edge, Chrome or Safari.'; return; }
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(new SpeechSynthesisUtterance(ids));
  }
  $('speak').addEventListener('click',function(){
    var a=Array.prototype.map.call(document.querySelectorAll('.ans'),function(b){return b.textContent;}).join('. ');
    speak($('scene').textContent+' Your choices: '+a+'.');
  });
  $('speak2').addEventListener('click',function(){ speak($('deeperText').textContent); });
  $('deeperBtn').addEventListener('click',function(){
    var open=$('deeper').hidden; $('deeper').hidden=!open; this.setAttribute('aria-expanded',String(open));
  });
  var fb={m:'Correct. Rosa succeeded at the task herself after practice.',
    v:'Try again. Vicarious experience comes from watching someone else succeed. Does Rosa watch someone in this scene?',
    p:'Try again. Verbal persuasion comes from what other people say. Does anyone speak to Rosa in this scene?',
    e:'Try again. This source comes from how the learner feels, such as being nervous or calm. Does the scene describe how Rosa feels?'};
  Array.prototype.forEach.call(document.querySelectorAll('.ans'),function(b){
    b.addEventListener('click',function(){ $('demoFb').textContent=fb[b.getAttribute('data-a')]; });
  });

  var v=function(id){ var e=$(id); return (e&&e.value||'').trim()||'—'; };
  function copyText(txt,status){
    var done=function(ok){ status.textContent= ok?'Copied.':'Could not copy. Select the text and copy it by hand.'; };
    if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(function(){done(true)},function(){done(false)}); }
    else{ try{ var ta=document.createElement('textarea'); ta.value=txt; document.body.appendChild(ta); ta.select(); var ok=document.execCommand('copy'); document.body.removeChild(ta); done(ok);}catch(e){done(false);} }
  }
  $('copyP6').addEventListener('click',function(){ copyText($('p6').textContent,$('p6Status')); });
  $('copyAll').addEventListener('click',function(){
    var acc=__ACCJS__.map(function(x){ return '  '+x[1]+': '+v('a_'+x[0]); }).join('\n');
    var ch=[['h_skip','lets me skip ahead'],['h_deep','deeper questions'],['h_more','no extra work of the same kind'],['h_fast','no reward for speed'],['h_open','any learner can choose it'],['h_both','access options work in the challenge']]
      .filter(function(x){ return $(x[0]).checked; }).map(function(x){ return x[1]; }).join(', ')||'—';
    copyText(['EPY 3143 · Week 15 · Workshop 4 — my answers','',
      'EXIT CARD','Learner excluded before, and the line that includes that learner: '+v('x_out'),'Where the rules could conflict: '+v('x_both'),'',
      'The learner I imagined: '+v('q_default'),'',
      'THREE LEARNERS','Jonah: '+v('c_jonah'),'Imani: '+v('c_imani'),'Rafa: '+v('c_rafa'),'Which might be 2e: '+v('c_both'),'',
      'What my tool asks learners to do most: '+v('q_setting'),'',
      'ACCESS REVIEW',acc,'Problem that excludes the most learners: '+v('a_worst'),'',
      'CHALLENGE REVIEW','True of my tool: '+ch,'My challenge rule: '+v('h_rule'),'',
      'ETHICS','Label: '+v('e_label'),'Data: '+v('e_data'),'Disclosure: '+v('e_disc'),'Honesty: '+v('e_hon'),'Fairness: '+v('e_fair'),'',
      'CHANGE 1: LOWER ONE BARRIER','Before: '+v('k1_before'),'After: '+v('k1_after'),'How I checked: '+v('k1_how'),'',
      'CHANGE 2: RAISE THE CEILING','Before: '+v('k2_before'),'After: '+v('k2_after'),'How I checked: '+v('k2_how'),'',
      'COMBINED TEST: '+v('k3_test')].join('\n'), $('copyStatus'));
  });
  load();
})();
</script>
</body>
</html>
'''

ACCJS = "[" + ",".join(f"['{k}','{n}']" for k, n, *_ in ACCESS) + "]"
HTML = (HTML.replace("__CSS__", CSS + EXTRA)
        .replace("__ACCESS__", access_cards())
        .replace("__ACCJS__", ACCJS))
open(OUT, "w", encoding="utf-8").write(HTML)
print("wrote", OUT, len(HTML) // 1024, "KB")
