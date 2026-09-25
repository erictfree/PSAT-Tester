#!/usr/bin/env python3
"""Validate the question bank in app/questions/ against docs/question-format.md.

Usage: python3 tools/validate.py [pack.json ...]
With no arguments, validates every pack listed in app/questions/index.json.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app")
QDIR = os.path.join(ROOT, "questions")

SKILLS = {
    "alg-linear-1var": "algebra", "alg-linear-2var": "algebra", "alg-linear-func": "algebra",
    "alg-systems": "algebra", "alg-inequalities": "algebra",
    "adv-equivalent": "advanced", "adv-nonlinear-eq": "advanced", "adv-nonlinear-func": "advanced",
    "psda-ratios": "psda", "psda-percent": "psda", "psda-one-var": "psda", "psda-two-var": "psda",
    "psda-probability": "psda", "psda-inference": "psda", "psda-claims": "psda",
    "geo-area-volume": "geometry", "geo-lines-angles": "geometry", "geo-right-trig": "geometry",
    "geo-circles": "geometry",
}
ID_RE = re.compile(r"^[A-Za-z0-9-]+$")


def parse_number(s):
    s = s.strip().replace(" ", "")
    try:
        if "/" in s:
            n, d = s.split("/")
            return float(Fraction(n) / Fraction(d))
        return float(s)
    except (ValueError, ZeroDivisionError):
        return None


def check_question(q, errors, where):
    def err(msg):
        errors.append(f"{where} {q.get('id', '?')}: {msg}")

    for f in ("id", "family", "variant", "source", "domain", "skill", "difficulty",
              "inContext", "type", "prompt", "answer", "explanation"):
        if f not in q:
            err(f"missing field '{f}'")
    if errors and errors[-1].startswith(f"{where} {q.get('id', '?')}: missing"):
        return
    if not ID_RE.match(q["id"]) or not ID_RE.match(q["family"]):
        err("id/family may only use letters, digits and '-'")
    if q["skill"] not in SKILLS:
        err(f"unknown skill '{q['skill']}'")
    elif SKILLS[q["skill"]] != q["domain"]:
        err(f"skill '{q['skill']}' belongs to domain '{SKILLS[q['skill']]}', not '{q['domain']}'")
    if q["difficulty"] not in (1, 2, 3):
        err("difficulty must be 1, 2 or 3")
    if not isinstance(q["variant"], int) or q["variant"] < 0:
        err("variant must be a non-negative integer")
    if q["type"] == "mc":
        ch = q.get("choices")
        if not isinstance(ch, list) or len(ch) != 4:
            err("mc questions need exactly 4 choices")
        elif len(set(c.strip() for c in ch)) != 4:
            err("mc choices must be distinct")
        if q["answer"] not in ("A", "B", "C", "D"):
            err("mc answer must be A-D")
    elif q["type"] == "spr":
        a = q["answer"]
        if not isinstance(a, list) or not a or not all(isinstance(x, str) for x in a):
            err("spr answer must be a non-empty list of strings")
        else:
            vals = [parse_number(x) for x in a]
            if any(v is None for v in vals):
                err(f"spr answer not numeric: {a}")
            if "choices" in q:
                err("spr questions must not have choices")
    else:
        err("type must be 'mc' or 'spr'")
    fig = q.get("figure")
    if fig is not None:
        if "img" in fig:
            if not os.path.exists(os.path.join(ROOT, fig["img"])):
                err(f"figure image not found: {fig['img']}")
        elif "svg" in fig:
            if "viewBox" not in fig["svg"]:
                err("inline svg needs a viewBox")
        else:
            err("figure needs 'img' or 'svg'")
        if not fig.get("alt"):
            err("figure needs alt text")
    for f in ("prompt", "explanation"):
        s = q[f]
        if s.count("\\(") != s.count("\\)"):
            err(f"unbalanced \\( \\) in {f}")


def main(paths):
    if not paths:
        with open(os.path.join(QDIR, "index.json")) as fh:
            paths = [os.path.join(QDIR, p) for p in json.load(fh)["packs"]]
    errors, allq = [], []
    for p in paths:
        with open(p) as fh:
            data = json.load(fh)
        for q in data["questions"]:
            check_question(q, errors, os.path.basename(p))
            allq.append(q)
    ids = Counter(q.get("id") for q in allq)
    for i, n in ids.items():
        if n > 1:
            errors.append(f"duplicate id {i}")
    fams = defaultdict(list)
    for q in allq:
        fams[q.get("family")].append(q)
    for f, qs in fams.items():
        if len({q.get("skill") for q in qs}) > 1:
            errors.append(f"family {f} mixes skills")
    for e in errors:
        print("ERROR", e)
    by_skill = Counter(q.get("skill") for q in allq)
    print(f"{len(allq)} questions in {len(fams)} families; {len(errors)} errors")
    for s in SKILLS:
        print(f"  {s:20s} {by_skill.get(s, 0)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
