# Question format

The question bank lives in `app/questions/`. `app/questions/index.json` lists the pack files to load:

```json
{ "packs": ["pt2-m1-a.json", "pt2-m1-b.json"] }
```

Each pack is a JSON file with a `questions` array. Adding more questions means adding a new pack (or appending to one), listing it in `index.json`, running `python3 tools/validate.py`, and republishing the app.

## Concept families

Every question belongs to a **family**: one concept, tested the same way. The student never sees the same question twice. When the scheduler brings a concept back (after a miss, or for spaced review), it serves an unseen member of the same family: same concept and same reasoning steps, but different numbers, scenario, names and context.

- The original question from a practice test is the family head: `"id": "pt2-m1-q05"`, `"family": "pt2-m1-q05"`, `"variant": 0`.
- Variants: `"id": "pt2-m1-q05-v1"`, `"family": "pt2-m1-q05"`, `"variant": 1`, and so on.
- A family you write from scratch uses its own family id, e.g. `"family": "extra-circles-01"`.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique id. Letters, digits, `-` only. |
| `family` | yes | Concept family id (see above). |
| `variant` | yes | 0 for the original, 1+ for variants. |
| `source` | yes | Where it came from, e.g. `"PSAT/NMSQT Practice Test 2 · Math Module 1 · Q5"` or `"Variant of Module 1 Q5"`. |
| `domain` | yes | One of `algebra`, `advanced`, `psda`, `geometry`. |
| `skill` | yes | One of the skill ids below. |
| `difficulty` | yes | 1 easy, 2 medium, 3 hard. |
| `inContext` | yes | `true` for word problems set in a real-world, science or social-studies scenario. |
| `type` | yes | `"mc"` (multiple choice) or `"spr"` (student-produced response). |
| `prompt` | yes | HTML. Math in TeX between `\(` and `\)`, e.g. `"What is \\(x\\) if \\(3x+5=20\\)?"` (backslashes doubled in JSON). Tables as plain `<table>` HTML. |
| `figure` | no | `{ "img": "img/pt2-m1-q05.png", "alt": "..." }` for a cropped image, or `{ "svg": "<svg ...>...</svg>", "alt": "..." }` for inline SVG. |
| `choices` | mc only | Exactly 4 strings (HTML/TeX), in order A–D. |
| `answer` | yes | mc: `"A"`–`"D"`. spr: array of accepted answers as strings, e.g. `["3/4", ".75", "0.75"]`. The checker compares numerically too, so `"0.75"` also accepts `.750`. |
| `explanation` | yes | HTML/TeX. Why the right answer is right; for mc, short notes on the tempting wrong choices. |

## Skills

| Domain | Skill id | Skill |
|---|---|---|
| algebra | `alg-linear-1var` | Linear equations in one variable |
| algebra | `alg-linear-2var` | Linear equations in two variables |
| algebra | `alg-linear-func` | Linear functions |
| algebra | `alg-systems` | Systems of two linear equations in two variables |
| algebra | `alg-inequalities` | Linear inequalities in one or two variables |
| advanced | `adv-equivalent` | Equivalent expressions |
| advanced | `adv-nonlinear-eq` | Nonlinear equations in one variable and systems of equations in two variables |
| advanced | `adv-nonlinear-func` | Nonlinear functions |
| psda | `psda-ratios` | Ratios, rates, proportional relationships, and units |
| psda | `psda-percent` | Percentages |
| psda | `psda-one-var` | One-variable data: distributions and measures of center and spread |
| psda | `psda-two-var` | Two-variable data: models and scatterplots |
| psda | `psda-probability` | Probability and conditional probability |
| psda | `psda-inference` | Inference from sample statistics and margin of error |
| psda | `psda-claims` | Evaluating statistical claims: observational studies and experiments |
| geometry | `geo-area-volume` | Area and volume |
| geometry | `geo-lines-angles` | Lines, angles, and triangles |
| geometry | `geo-right-trig` | Right triangles and trigonometry |
| geometry | `geo-circles` | Circles |

## Inline SVG figures

Draw with `stroke="currentColor"` and `fill="none"` (or `fill="currentColor"` for dots and text) so figures read in light and dark themes. Give the root `<svg>` a `viewBox` and no fixed width/height. Keep labels inside the viewBox.
