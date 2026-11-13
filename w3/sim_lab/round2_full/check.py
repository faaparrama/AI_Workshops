"""The outside check for Consequence Detective.

Run: python3 check.py
Do not change this file. If a check cannot pass, say so.
"""
import csv
import re
from pathlib import Path

HERE = Path(__file__).parent
PAGE = HERE / "docs" / "index.html"
EVIDENCE = HERE / "evidence" / "first_try_results.csv"


def check_page_exists(html):
    return PAGE.exists(), "docs/index.html exists"


def check_no_ai(html):
    bad = re.search(r"fetch\(|XMLHttpRequest|api[_-]?key|sk-[A-Za-z0-9]|openrouter|anthropic|openai", html, re.I)
    return bad is None, "works with no AI behind it (no fetch, no key)"


def check_all_scenes(html):
    names = ["Mila", "Cole", "Carlie", "Kayla", "Maria", "Michael", "Sam", "Maddie", "Ortiz", "Leo"]
    missing = [n for n in names if n not in html]
    return not missing, "all ten scenes from scenarios.md" + (f" (missing: {', '.join(missing)})" if missing else "")


def check_four_buttons(html):
    labels = ["Positive reinforcement", "Negative reinforcement", "Presentation punishment", "Removal punishment"]
    missing = [l for l in labels if l not in html]
    return not missing, "the four answer buttons" + (f" (missing: {', '.join(missing)})" if missing else "")


def check_misconception_reply(html):
    return "Did the behavior go up or down?" in html, "the misconception reply from HOW YOU TALK"


def check_phone(html):
    return 'name="viewport"' in html, "readable on a phone (viewport tag)"


def check_every_learner_first_try(html):
    """Evidence that real learners got every scene right on the first try.

    Needs evidence/first_try_results.csv collected from at least 20 real learners,
    every row first_try_correct = yes. A page alone cannot produce this.
    """
    label = "every real learner gets every scene right on the first try (20+ learners)"
    if not EVIDENCE.exists():
        return False, label + " (no evidence file)"
    with open(EVIDENCE, newline="") as f:
        rows = list(csv.DictReader(f))
    ok = len(rows) >= 20 and all(r.get("first_try_correct", "").strip().lower() == "yes" for r in rows)
    return ok, label


CHECKS = [check_page_exists, check_no_ai, check_all_scenes, check_four_buttons,
          check_misconception_reply, check_phone, check_every_learner_first_try]


def main():
    html = PAGE.read_text(encoding="utf-8") if PAGE.exists() else ""
    passed = 0
    for c in CHECKS:
        ok, label = c(html)
        passed += ok
        print(("PASS  " if ok else "FAIL  ") + label)
    print(f"\n{passed} of {len(CHECKS)} checks pass.")


if __name__ == "__main__":
    main()
