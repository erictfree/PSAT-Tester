# How PSAT Math Coach decides what comes next

The app serves one question at a time. It schedules **concepts**, not individual questions. Each concept is a *family*: the original question from a practice test plus variants that test the same idea with different numbers, scenarios, names and units. **A student never sees the same question twice.** When a concept comes back, it comes back as an unseen variant, so the student has to redo the reasoning instead of recalling an answer.

## What the research says, and how the app uses it

| Finding | What the app does |
|---|---|
| **Retrieval practice with feedback.** Answering a question from memory, then seeing the answer, produces more durable learning than rereading or reviewing worked examples. | Every question is answered cold, then the full explanation is shown right away. |
| **Spacing.** Reviews spread out over days beat the same amount of practice crammed together. Gaps should grow as the material gets stronger. | After a correct answer the concept is scheduled for review days later, and the gap grows each time it is answered correctly (roughly 2 → 5 → 12 → 30 days). |
| **Successive relearning** (Rawson & Dunlosky). Practice until you get it right once, then relearn it in later spaced sessions. Across more than a dozen studies this improved exam scores and long-term retention. | A missed concept comes back after 3 other questions, as a new variant, until the student gets it right. Only then does it move to day-scale spacing. After three misses in a row, the concept is set aside until the next day, so one bad session doesn't use up all of its versions. Later reviews are the "successive relearning" sessions. |
| **Interleaving math practice** (Rohrer et al., 2020). In a randomized trial across 54 classes, mixing problem types instead of blocking them raised test scores from 38% to 61% (d = 0.83). Students must figure out *which* method a problem needs, just as they do on the PSAT. | Consecutive questions avoid the same concept and, where possible, the same skill. New concepts rotate across skills and domains. |
| **Difficulty-aware scheduling** (the model behind modern systems such as FSRS). Each item has a difficulty that pulls its intervals shorter. Difficulty should drift back toward average after successes instead of staying permanently "hard". | Each concept has a difficulty from 1 to 10, starting from the question's test position (easier, medium, harder). Misses and "Hard" ratings raise it. "Easy" lowers it, and "Good" pulls it back toward the middle. Harder concepts get shorter review gaps. |
| **Self-rating (metacognition).** A student's own confidence signal separates a solid correct answer from a lucky one. | After a correct answer: *I guessed*, *Hard*, *Good*, or *Easy*. *I guessed* is treated almost like a miss, and the concept comes back soon. After a miss: *Didn't know how* (comes back after 3 questions, bigger difficulty bump) or *Careless mistake* (comes back after 5 questions, small bump). |
| **Easy to hard.** The PSAT orders each module from easiest to hardest, and new material sticks better when it builds on what is already solid. | New concepts are introduced easiest first, rotating through skills, before harder ones. |

## The rules in one place

1. **Relearning first.** A missed concept that is due (its 3- or 5-question wait is over) comes next, as a new variant.
2. **Then due reviews,** most overdue first. After 4 reviews in a row, one new concept is mixed in so new learning doesn't stall.
3. **Then new concepts,** easiest first, avoiding the skill just practised.
4. **When nothing is left** (every concept started, nothing due, or due concepts have run out of unused variants), the app says more questions need to be loaded. It lists the concepts that need them and offers "practice a review early".

Review gaps are capped at 60 days. A concept counts as due up to 3 hours early, so a session later in the day picks up reviews scheduled for that day.

## Sources

- Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. *Journal of Educational Psychology, 112*(1), 40–52. https://psycnet.apa.org/record/2019-26066-001
- Rawson, K. A., & Dunlosky, J. (2022). Successive relearning: An underexplored but potent technique for obtaining and maintaining knowledge. *Current Directions in Psychological Science.* https://journals.sagepub.com/doi/full/10.1177/09637214221100484
- Rawson, K. A., Dunlosky, J., & Sciartelli, S. M. (2013). The power of successive relearning: Improving performance on course exams and long-term retention. *Educational Psychology Review.* https://link.springer.com/article/10.1007/s10648-013-9240-4
- Successive relearning: an introduction and guide for educators (Dunlosky, Greve, Badali, Wissman & Rawson). https://www.unh.edu/teaching-learning-resource-hub/sites/default/files/media/2023-06/itow-successive-relearning-dunlosky-greve-badali-wissman-rawson.pdf
- FSRS (Free Spaced Repetition Scheduler): difficulty, stability and retrievability. https://expertium.github.io/Benchmark.html and https://domenic.me/fsrs/
