# Beginning Python — Project Instructions

## Core Teaching Philosophy

**The primary teaching tool in Chapters 1–18 is inline interactive turtle graphics powered by Skulpt.**

Every lesson in the early chapters must include at least one Skulpt lab where the student can:
1. **Read** a short, working Python program
2. **Run** it instantly in the browser (no install, no account)
3. **Modify** it — change a number, a color, a direction — and run it again

This "see it, run it, modify it" cycle is the heartbeat of this textbook. It is what separates
it from a static reference and makes it usable in coding club or classroom setting.

### Predict Before You Run

Before every Skulpt lab, ask the student to **predict what the program will do** before
clicking Run. This one habit — pausing to reason through code before executing it — is
one of the most valuable skills a beginning programmer can build.

Monty frames the prediction using `mascot-thinking`:

```markdown
!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, look at the program below.
    How many sides do you think the turtle will draw?
    Make your guess, then run it to find out!
```

**Rules for prediction prompts:**
- Ask one specific, answerable question (shape drawn, number of lines printed, color used, how many times the loop repeats, etc.) — not an open-ended "what happens?"
- Place the `mascot-thinking` prediction prompt **immediately above** the Skulpt lab block, before the student can run the code
- After the lab, add a brief "Were you right?" sentence in prose to close the loop — no second admonition needed
- Keep the prediction question at a difficulty level where roughly half the students will guess correctly on their first try — too easy builds no habit, too hard discourages guessing

### Learning Checks

For every important concept, include at least one **Learning Check** — a Skulpt lab where:
- The program is **almost complete** but is missing one key line the student must add, OR
- The program contains a **small, deliberate bug** the student must find and fix

Learning checks should be clearly labeled and framed by Monty so students know they are being
asked to think, not just read. Use `mascot-thinking` for "add the missing line" challenges and
`mascot-warning` for "find the bug" challenges.

**Learning Check format:**
```markdown
!!! mascot-thinking "Your Turn — Add the Missing Line"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below draws three sides of a square but stops short.
    Add **one line** to make it draw the fourth side and complete the shape!
```

Followed immediately by a Skulpt lab whose textarea contains the incomplete or buggy program.

## Content Generation Guidelines

**Read `CONTENT-GENERATION-GUIDELINES.md` before generating any student-facing content.**

That file is the authoritative source for:
- Monty the Python mascot usage (admonition types, image paths, placement rules, hard limits)
- Skulpt lab HTML block structure and required element IDs
- General writing style (audience ages 10–14, post-Scratch, encouraging tone)

Key rules to keep in mind at all times:

- **Mascot max 6 admonitions per lesson** — never back-to-back
- **Always open with `mascot-welcome`** and **close with `mascot-celebration`**
- **Image path depth matters**: chapters live two levels deep → use `../../img/mascot/`
- **Never use `<img>` tags** — always `![alt](path){ class="mascot-admonition-img" }`
- **Skulpt element IDs are fixed** — `skulpt.js` depends on them; do not rename them
- Instructor-facing content (teachers' guide, course description) does NOT use the mascot

## Chapter Structure

38 chapters covering 450 concepts, all validated with 0 dependency violations.
Chapter files live in `docs/chapters/##-slug/index.md`.
The chapter concept assignment is the source of truth for which concepts belong where.

## MkDocs

- Do NOT add `- navigation.tabs` to mkdocs.yml.
- Do not start or kill `mkdocs serve` — the user runs it in their own terminal.
