# PSAT Math Coach

A practice app for PSAT/NMSQT math that serves one question at a time and uses spaced repetition by concept. It never repeats a question: when a concept comes back, it's a new version with the same idea but different numbers and a different scenario.

- **Practice:** one question at a time, multiple choice or typed answer (student-produced response, like the real test). There's a pace timer (1:35 per question on the real test), a reference sheet, and a link to the Desmos test calculator. After each answer the student sees the explanation and rates how it felt, and that rating sets when the concept comes back.
- **Progress:** accuracy, day streak, median time, a daily practice chart, and a status for each of the 19 official PSAT math skills (Not started, Relearning, Shaky, Building, Solid).
- **Log:** every answer with time, rating and mode. Click a row to see the question, the student's answer, and the explanation.
- **Motivation:** confetti on correct answers (bigger for streaks and milestones), a streak counter, a daily goal ring (5–30 questions, set on the Progress page), "Comeback!" when a missed concept is conquered, skill level-ups, and 20 badges. Short encouraging notes follow a miss. Confetti is skipped when the device asks for reduced motion.
- **Pick up any time:** progress is saved after every answer. Reopening the app resumes where the student left off, including a question that was on screen.
- **Out of questions:** when every loaded question has been used (or a due concept has no unused versions left), the app tells the student more questions need to be loaded and lists which concepts need them.

How the scheduling works, and the research behind it: [docs/learning-method.md](docs/learning-method.md).

## Layout

```
app/index.html            the app (published as a claude.ai artifact)
app/questions/index.json  which question packs to load
app/questions/*.json      question packs
app/img/                  figures cropped from the practice test
docs/question-format.md   question JSON format and skill list
docs/learning-method.md   scheduling rules and sources
tools/validate.py         checks every pack against the format
```

## Question bank

The bank starts from the 54 math questions in *PSAT/NMSQT Practice Test 2* (College Board). Each one heads a concept family with 7 variants, which are the same concept with new numbers and scenarios. Extra families cover skills that test doesn't include: inference and margin of error, evaluating statistical claims, and more probability, trigonometry, circles, percentages and inequalities. Every answer was checked by computing it.

The practice-test questions are College Board material, included for personal study. Keep this repository private.

### Adding questions

1. Write a pack in `app/questions/` following [docs/question-format.md](docs/question-format.md). New variants of an existing concept use the same `family` id; new concepts get a new family id.
2. Add the file name to `app/questions/index.json`.
3. Run `python3 tools/validate.py`.
4. Republish the app. The student's progress is stored separately and is kept.

## GitHub Pages

Pages serves the repo root from `main`. The root `index.html` is generated from `app/index.html` by `python3 tools/build_pages.py`, which adds the page header the artifact normally supplies and points it at `app/`. Re-run it after changing the app, and commit both files. The Pages site is public, and its progress is saved only in the student's browser.

## Where progress is stored

In the published artifact, progress lives in the artifact's database (`progress/state` for scheduling state, `logs/c0`, `logs/c1`, … for the answer log in chunks of 300). It follows the student across devices. The student needs **Contributor** access to the artifact to save progress. If the database isn't available (for example when the file is opened locally), the app saves to the browser's local storage instead, and the header shows "Saved on this device only".
