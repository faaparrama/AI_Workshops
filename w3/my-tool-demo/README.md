# my-tool-demo

A finished example of a project folder. Copy it, rename it after your tool, and put your own content in each file.

The tool in this demo is made up: **Where Does Confidence Come From?**, a sorter for the four sources of self-efficacy (Week 11).

## The minimum

```
my-tool/
  skill/
    SKILL.md        required · LEARNER · TASK · HOW YOU TALK · guardrails
    knowledge.md    required · standard · ideas · sources · off limits
  assets/           optional · pictures, icons, audio · CREDITS.md · links.md
  docs/             the agent builds the page here. Leave it empty.
```

**Two files are required.** Everything in `assets/` is optional.

## Check before an agent opens it

- [ ] `skill/SKILL.md` has all four parts: LEARNER, TASK, HOW YOU TALK, guardrails.
- [ ] LEARNER names the misconception the way a learner would say it.
- [ ] HOW YOU TALK has at least three "If the learner…, say…" lines. That part is your M3.
- [ ] `skill/knowledge.md` quotes a standard and names its source.
- [ ] Every idea in `knowledge.md` is a sentence a learner can get wrong.
- [ ] Off limits says what the tool must not teach.
- [ ] Each picture in `assets/` has one line in `CREDITS.md`. Each link has one line in `links.md`.
- [ ] No real student's face, name or work, anywhere in the folder.
- [ ] No API key, anywhere in the folder.

## Pictures, icons and links

Welcome, not required.

- You made it, or its license lets you share it: public domain or Creative Commons. A screenshot from a textbook doesn't qualify.
- What it shows goes in `CREDITS.md`. That line becomes the alt text a screen reader says aloud.
- Under 1 MB per file.
- Only `docs/` goes online. The agent copies the pictures it uses into `docs/assets/`.

## Next

Workshop 3 is about `SKILL.md`. The build kit in `lane_c/` takes this folder to a live website.
