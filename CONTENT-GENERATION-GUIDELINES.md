# Content Generation Guidelines — Beginning Python

This file defines rules for generating student-facing content in this course.
All AI agents and human authors creating lessons, labs, quizzes, or other
student-facing pages must follow these guidelines. Instructor-facing content
(teacher's guide, course description) does not need to use the mascot.

---

## Primary Teaching Tool: Inline Interactive Turtle Graphics

**The core feature of this textbook is inline Skulpt turtle graphics that run directly in the browser.**

In Chapters 1–18, every lesson must teach through interactive turtle programs, not static
code listings. Students click **Run**, watch Monty draw something on the canvas, then
immediately modify the code and run it again — all without installing anything or leaving
the page. This live feedback loop is what makes the textbook engaging for ages 10–14.

### The "See It, Run It, Modify It" Cycle

Every Skulpt lab follows this three-phase experience:

1. **See it** — a short (5–15 line) working turtle program appears in the editable textarea,
   accompanied by a prose explanation of what it does.
2. **Run it** — the student clicks Run and sees the turtle draw something on the canvas to
   the right of the code.
3. **Modify it** — the Experiments section at the bottom of each lesson gives 3–5 specific
   invitations to change the code: a different color, a different number of sides, a new
   shape, a faster speed, etc.

**This cycle is the heartbeat of the textbook.** Do not replace it with static code blocks,
output screenshots, or off-site links (e.g., Trinket) in any lesson for Chapters 1–18.

### Predict Before You Run

Before every Skulpt demo lab, Monty asks the student to **predict what the program will do
before clicking Run.** Pausing to reason through code before executing it is one of the most
transferable habits a beginning programmer can build — it trains the mental model that lets
students debug independently instead of changing things at random.

**Placement:** the prediction prompt goes **immediately above** the Skulpt lab block, before
the student can run the code.

**Format — use `mascot-thinking`:**

```markdown
!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, look at the code below.
    How many sides do you think the turtle will draw? Make your guess — then find out!
```

**Rules:**

| Rule | Detail |
|------|--------|
| Ask one specific question | "How many sides?" / "What color?" / "How many times will the loop run?" — not vague "What happens?" |
| Calibrate difficulty | Aim for ~50% correct on a first guess — easy enough to attempt, surprising enough to build the habit |
| Close the loop | After the lab, add one short prose sentence ("Were you right?") — no second admonition needed |
| Skip in Learning Checks | Learning Check labs already give the student a task; stacking a prediction on top causes overload |
| Counts toward mascot cap | Prediction `mascot-thinking` and concept `mascot-thinking` both count in the 6-per-lesson limit |

### Learning Checks

For every important concept, include at least one **Learning Check** — a second Skulpt lab
(distinct from the main demo) where the student must actively produce or repair code:

| Type | When to use | Admonition |
|------|-------------|------------|
| **Add the missing line** — program stops short or gives the wrong result until the student adds one key line | Introducing a new command or concept | `mascot-thinking` |
| **Find and fix the bug** — program has a small deliberate error (wrong method name, off-by-one in `range()`, missing `pendown()`, etc.) | After a concept has been introduced | `mascot-warning` |

**Learning Check format — missing line:**

```markdown
!!! mascot-thinking "Your Turn — Add the Missing Line"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below draws three sides of a square and then stops.
    Add **one line** so Monty completes the fourth side!

[Skulpt lab block with the incomplete program in the textarea]
```

**Learning Check format — find the bug:**

```markdown
!!! mascot-warning "Spot the Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Something is wrong with the program below — Monty draws a straight line
    instead of a triangle. Can you find and fix the mistake?

[Skulpt lab block with the buggy program in the textarea]
```

### Skulpt Lab Sizing for Turtle Programs

Keep programs short enough that students can read the whole thing at a glance:

- **Introductory labs (Chapters 1–5):** 4–8 lines of Python
- **Mid-course labs (Chapters 6–18):** 8–20 lines of Python
- **Advanced labs (Chapters 19+):** no strict limit, but prefer several short focused labs over one long one

### When to Use Each Lab Type

There are two Skulpt lab layouts. Choose based on whether the program uses turtle graphics:

| Situation | Lab type | HTML class |
|-----------|----------|------------|
| Program uses `import turtle` or any turtle command | **Drawing lab** | *(no extra class — default)* |
| Program uses only `print()`, variables, loops, functions, etc. | **Text-only lab** | `class="skulpt-text-only"` |

**Drawing labs** (Chapters 1–18 turtle lessons) show a 400 × 400 px canvas to the right of the
code editor where the turtle draws.

**Text-only labs** hide the canvas panel entirely; the code editor stretches to fill the full
content width. Use these for any program that produces only text output — `print()` calls,
variable values, string results, etc. This layout is the default from Chapter 19 onward, and
can also appear in earlier chapters for the rare non-turtle concept (e.g., a `print()`-only
variable lesson).

Never put a text-only lab in a lesson that also needs the canvas, and never put a drawing
lab in a lesson whose programs do not call any turtle commands — the empty canvas just
wastes space and confuses students.

---

## Lesson Structure Requirements

These rules apply to every student-facing lesson page regardless of chapter.

### Learning Objectives

Every lesson must open with 1–3 student-facing learning objectives written in plain English.
Place them **before** the `mascot-welcome` admonition so students know what they are working
toward before Monty speaks.

**Format:**

```markdown
By the end of this lesson you'll be able to:

- Draw a square using a `for` loop with `forward()` and `right()`
- Explain why loops save you from writing the same line four times
- Change the number of sides to draw any regular polygon
```

**Rules:**

- Write from the student's perspective: "you'll be able to…"
- Use concrete, observable verbs: *draw, write, fix, explain, change, build* — never "understand" or "know about"
- 1 objective = 1 new concept; if you have 4+ objectives the lesson is too broad — split it into two lessons
- Keep language at a 5th-grade reading level — no jargon in the objectives themselves; define it later in the lesson

### Scratch Bridge

For every new concept in Chapters 1–14 that has a Scratch analogue, include a **Scratch Bridge**
callout immediately after the concept is first introduced. This is the highest-leverage move for
this audience — students already have a working mental model from Scratch; connecting to it
explicitly saves significant cognitive effort.

**Format — use `mascot-tip` with the label "Scratch Bridge":**

```markdown
!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch you used the **"Move 10 steps"** block.
    In Python, `forward(10)` does exactly the same thing —
    it tells Monty to walk forward 10 steps!
```

**Common Scratch-to-Python bridges:**

| Scratch block | Python equivalent | First appears |
|---------------|-------------------|---------------|
| Move ___ steps | `forward(n)` | Ch 5 |
| Turn ↻ ___ degrees | `right(n)` | Ch 5 |
| Turn ↺ ___ degrees | `left(n)` | Ch 5 |
| Pen down / Pen up | `pendown()` / `penup()` | Ch 5 |
| Set pen color | `pencolor("red")` | Ch 5 |
| Repeat ___ | `for i in range(n):` | Ch 7 |
| If ___ then | `if condition:` | Ch 9 |
| If ___ then / else | `if condition: … else:` | Ch 9 |
| Set ___ to ___ | `variable = value` | Ch 3 |
| Say ___ | `print(...)` | Ch 1 |
| Ask ___ and wait | `input(...)` | Ch 13 |

**Rules:**

- Required whenever a Scratch analogue exists (Chapters 1–10); optional but encouraged in Chapters 11–14
- Skip in Chapter 15+ — students have moved past the Scratch mental model
- Always frame Python as the natural next step — never say "in Scratch you had to…" (sounds dismissive)
- Counts toward the 6-per-lesson mascot admonition cap

### One New Concept Per Lab

Each Skulpt **demo lab** must introduce exactly **one new concept**. If a lesson covers three
new turtle commands, write three short sequential labs — not one lab that introduces all three
at once.

This is the single most important cognitive load rule in this textbook. A novice programmer
cannot simultaneously parse unfamiliar syntax, predict program behavior, and map it to prior
knowledge. Isolate each new idea in its own runnable chunk.

**Correct pattern:** Lab A shows `penup()` alone → Lab B adds `goto()` → Lab C completes the
idea with `pendown()`, each building on the last.

**Incorrect pattern:** One lab where `penup()`, `goto()`, and `pendown()` all appear for the
first time together.

The demo lab for any concept should be the **simplest possible program** that demonstrates
only that concept. Save combinations and creative uses for the Experiments section.

### New Vocabulary

When a technical term appears **for the first time**, follow this three-step rule:

1. **Bold** the term on first use: `**parameter**`
2. Define it immediately in one plain-English sentence using a concrete analogy
3. Show it in working code on the same page

**Example:**
> A **parameter** is information you pass into a function when you call it — like telling
> a vending machine which button to press before it does anything.

**Additional rules:**

- Never introduce a term in the first sentence of an explanation — establish the concept in plain English first, then name it
- Do not define two new terms in the same sentence
- Reinforce the term at least once more in the same lesson (in the explanation table, an experiment prompt, or Monty's dialogue)
- Do not bold a term on its second or later appearance — bolding signals "this is new"

### Spaced Repetition and Spiral Review

Each lesson must naturally use at least 2–3 concepts from **previous chapters** as background
context in its demo labs — without re-teaching them. Students consolidate earlier learning by
encountering it in new situations.

**How to apply:**

- Teaching `for` loops (Ch 7)? Write the loop body using `forward()` and `right()` — reinforcing Ch 5 commands
- Teaching `if/else` (Ch 9)? Use a variable for the condition — reinforcing Ch 3 variables
- Teaching string methods (Ch 14)? Feed them from `input()` — reinforcing Ch 13 user input

**What not to do:**

- Do not add a "reminder" paragraph re-explaining a prior concept — just use it
- Do not re-introduce a prior concept as if new: "First, recall that `forward()` moves the turtle…" — trust that students read the earlier chapters

### Handling Skulpt Error Messages

Students will produce errors while modifying code. Skulpt prints tracebacks to
`<pre id="output">`. Lessons should prepare students to read errors calmly.

**By chapter range:**

| Chapters | Guidance |
|----------|----------|
| 1–5 | Add a short plain-text "If you see a red error message" note after the first lab. 2–3 sentences max. |
| 6–12 | Fold error guidance into the `mascot-warning` admonition for the most likely mistake in that lesson. |
| 13+ | Expect students to read tracebacks independently. Only add notes for genuinely tricky errors (e.g., `TypeError: can only concatenate str (not "int") to str`). |

**Most common Skulpt errors by chapter range:**

| Chapters | Common errors |
|----------|---------------|
| 1–4 | `NameError` from misspelled command, wrong indentation |
| 5–8 | Missing `pendown()`, wrong argument type passed to `forward()` |
| 9–12 | Missing colon after `if` / `for`, wrong indentation after colon |
| 13–18 | `TypeError` mixing `str` + `int`, `ValueError` from bad `int()` conversion |

**"If you see an error" note format (Chapters 1–5):**

```markdown
**If you see a red error message:** Check your spelling — Python is case-sensitive,
so `Forward(100)` won't work but `forward(100)` will.
Also make sure every line inside the loop is indented by exactly 4 spaces.
```

---

## Learning Mascot: Monty the Python

### Mascot File Index

The canonical files for this mascot. When editing any of these, update the
others in the same turn so they stay in sync.

| File | Purpose |
|------|---------|
| [`docs/img/mascot/neutral.png`](docs/img/mascot/neutral.png) | Default / general-purpose pose |
| [`docs/img/mascot/welcome.png`](docs/img/mascot/welcome.png) | Chapter-opening pose |
| [`docs/img/mascot/thinking.png`](docs/img/mascot/thinking.png) | Key-concept / prediction / learning-check pose |
| [`docs/img/mascot/tip.png`](docs/img/mascot/tip.png) | Hint / Scratch Bridge / helpful-guidance pose |
| [`docs/img/mascot/warning.png`](docs/img/mascot/warning.png) | Common-mistake / bug-fix / pitfall pose |
| [`docs/img/mascot/encouraging.png`](docs/img/mascot/encouraging.png) | Difficult-content / struggle pose |
| [`docs/img/mascot/celebration.png`](docs/img/mascot/celebration.png) | End-of-lesson / achievement pose |
| [`docs/css/mascot.css`](docs/css/mascot.css) | Custom admonition styles for the seven pose contexts |
| [`docs/learning-graph/mascot-test.md`](docs/learning-graph/mascot-test.md) | Rendering test page that exercises every admonition style |

### Character Overview

- **Name**: Monty
- **Species**: Python snake
- **Personality**: Curious, encouraging, patient, playful, never sarcastic or intimidating
- **Catchphrase**: "Let's code it together!"
- **Visual**: Friendly cartoon python with bright emerald-green scales, oversized round wire-rim
  glasses, large sparkling blue-green eyes, two small expressive arms, and a curling tail.
  Flat vector style, transparent background, consistent across all poses.

### Voice Characteristics

- Uses simple, encouraging language appropriate for ages 10–14
- Celebrates small wins — never dismisses a question as "easy"
- Refers to students as "coders" or "programmers"
- Occasionally uses Python puns ("Let's uncoil this problem!", "I've got a hiss-tory of coding!")
- Never uses jargon without defining it first
- Signature phrases: "Let's code it together!", "You've got this!", "Great question!"

### Mascot Admonition Format

**Always** place mascot images in the admonition body, never in the title bar.
Use the Markdown image syntax with the `mascot-admonition-img` class:

```markdown
!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Admonition text goes here after the image. Keep it to 1–3 sentences.
```

**Image path depth:** The path `../../img/mascot/` is correct for pages two
directories deep (e.g., `chapters/05-drawing-with-turtle/` or `skulpt/02-simple-square/`).
For pages at the root of `docs/`, use `img/mascot/`.
For pages one level deep (e.g., `docs/strategy/index.md`), use `../img/mascot/`.

### Placement Rules

| Context | Admonition Type | Image | Frequency |
|---------|----------------|-------|-----------|
| Lesson opening | `mascot-welcome` | `welcome.png` | Once per lesson — always first |
| Prediction prompt | `mascot-thinking` | `thinking.png` | Once per demo lab |
| Key concept or insight | `mascot-thinking` | `thinking.png` | 1–2 per lesson |
| Scratch Bridge | `mascot-tip` | `tip.png` | Once per new concept with a Scratch analogue |
| Helpful hint or shortcut | `mascot-tip` | `tip.png` | As needed |
| Common mistake / pitfall | `mascot-warning` | `warning.png` | As needed |
| Find-the-bug Learning Check | `mascot-warning` | `warning.png` | Once per learning check of this type |
| Difficult content | `mascot-encourage` | `encouraging.png` | Where students may struggle |
| End of lesson / experiments | `mascot-celebration` | `celebration.png` | Once per lesson — always last |
| General sidebar | `mascot-neutral` | `neutral.png` | As needed |

### Hard Limits

- **Maximum 6 mascot admonitions per lesson** — more than this interrupts reading flow
- **No back-to-back mascot admonitions** — always separate with at least one paragraph of content
- **One `mascot-welcome` maximum per lesson** — always at the very start (after learning objectives)
- **One `mascot-celebration` maximum per lesson** — always at the very end
- Do not use mascot admonitions purely for decoration — every use must add instructional value

### Do's and Don'ts

**Do:**
- Use Monty to introduce new topics warmly at the start of every lesson
- Include the catchphrase "Let's code it together!" in welcome admonitions
- Keep dialogue brief (1–3 sentences maximum)
- Match the pose image to the content type (tip pose for Scratch Bridge and hints, warning pose for bugs and pitfalls)
- Write in Monty's encouraging, kid-friendly voice

**Don't:**
- Use Monty more than 6 times in a single lesson
- Put mascot admonitions back-to-back without intervening content
- Change Monty's personality or make him sound sarcastic or intimidating
- Use `<img>` HTML tags — always use Markdown image syntax with `{ class="mascot-admonition-img" }`
- Place images in the admonition title bar

---

## Skulpt Lab Format

All Skulpt interactive labs share a common structure. Follow this template exactly
when generating a new lesson page.

### Page Structure

```markdown
# Lesson Title

By the end of this lesson you'll be able to:

- [Objective 1 — concrete, observable, student-facing]
- [Objective 2]
- [Objective 3 — maximum 3; if you need more, split the lesson]

Brief intro paragraph (1–2 sentences setting up what problem the code solves or what
the student will build).

!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    1–3 sentences from Monty introducing the lesson. Include "Let's code it together!"

## [Concept Name]

One short paragraph introducing the new concept in plain English **before** naming it
technically. Bold the term on first use and define it with an analogy.

[Scratch Bridge admonition here if a Scratch analogue exists — use mascot-tip]

## Sample Code

```python
[working turtle program — as short as possible for this concept]
```

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    [One specific, answerable prediction question about the code above.]
    Make your guess — then click Run to find out!

## Try It Now

Edit the code below and click **Run** to see the result right on this page.
No account needed — everything runs in your browser.

[Skulpt lab HTML block — see below]

Were you right? [One sentence closing the prediction loop.]

[Optional: "If you see a red error message" note for Chapters 1–5 only]

## How It Works

[Explanation of the key concept. Use the bolded term again here to reinforce it.]

[Optional mascot-tip for a helpful shortcut, OR mascot-encourage for a hard idea]

## Explanation Table

| Line | What it does |
|------|-------------|
| `import turtle` | Loads the turtle library so Python knows how to draw |
| ... | ... |

[Optional mascot-warning for a common mistake — include brief "If you see…" guidance]

## Learning Check

!!! mascot-thinking "Your Turn!"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    [Clear task description — add one line, or spot the bug.]

[Skulpt lab block with the incomplete or buggy program]

## Experiments

Try these changes to the code above. For each one, predict what will happen first,
then run it to check!

1. [Specific change to make.] **You'll know it worked when** [observable result].
2. [Specific change to make.] **You'll know it worked when** [observable result].
3. [Specific change to make.] **You'll know it worked when** [observable result].
4. [Optional harder challenge.]
5. [Optional creative challenge — no single right answer.]

!!! mascot-celebration "Great Work!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You've completed this lesson — and that's something to celebrate!
    Try the experiments above to go even further. Let's code it together!
```

### Skulpt HTML Block

There are two lab templates. Pick based on whether the program uses turtle graphics
(see [When to Use Each Lab Type](#when-to-use-each-lab-type)).

The CDN `<script>` tags must appear **once per page**, before the first lab block.
`skulpt.js` (via `extra_javascript`) and `skulpt.css` (via `extra_css`) provide the
shared runtime and styles — do not add inline `<style>` or `<script>` tags.

```html
<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
```

#### Drawing Lab (turtle programs)

Use when the program calls `import turtle` or any turtle command.
The canvas appears to the right of the code editor.

```html
<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">PYTHON CODE HERE
</textarea>
    <div id="button-row">
      <button id="run-btn" onclick="runSkulpt()">&#9654; Run</button>
      <button id="reset-btn" onclick="resetSkulpt()">&#8635; Reset</button>
    </div>
    <pre id="output"></pre>
  </div>
  <div id="canvas-container">
    <div id="turtle-target"></div>
  </div>
</div>
```

#### Text-Only Lab (print/variables/logic — no turtle)

Use when the program produces only text output. Add `class="skulpt-text-only"` to
the outer div. The canvas container is hidden by CSS; the editor fills the full
content width. The `turtle-target` div must still be present so `runSkulpt()` can
initialise without errors — it just isn't visible.

```html
<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">PYTHON CODE HERE
</textarea>
    <div id="button-row">
      <button id="run-btn" onclick="runSkulpt()">&#9654; Run</button>
      <button id="reset-btn" onclick="resetSkulpt()">&#8635; Reset</button>
    </div>
    <pre id="output"></pre>
  </div>
  <div id="canvas-container">
    <div id="turtle-target"></div>
  </div>
</div>
```

#### Rules that apply to both templates

- The Python code inside `<textarea>` must match the Sample Code block exactly
- **Do not set a `height` or `rows` attribute on the `<textarea>`** — `skulpt.js` auto-sizes it on page load so all code is visible without scrolling
- The first lab on a page uses the plain IDs above; `skulpt.js` depends on them

#### Multiple labs on one page (Learning Checks, etc.)

Every lab after the first must use a `-2`, `-3`, … suffix on **every** ID, and pass
the matching suffix to the button `onclick` handlers. The `skulpt-text-only` class
applies to multiple labs independently — a page may have a drawing lab first and a
text-only lab second, or vice versa.

```html
<!-- Second drawing lab -->
<div id="skulpt-lab-2">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">PYTHON CODE HERE
</textarea>
    <div id="button-row-2">
      <button id="run-btn-2" onclick="runSkulpt('-2')">&#9654; Run</button>
      <button id="reset-btn-2" onclick="resetSkulpt('-2')">&#8635; Reset</button>
    </div>
    <pre id="output-2"></pre>
  </div>
  <div id="canvas-container-2">
    <div id="turtle-target-2"></div>
  </div>
</div>

<!-- Second text-only lab -->
<div id="skulpt-lab-2" class="skulpt-text-only">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">PYTHON CODE HERE
</textarea>
    <div id="button-row-2">
      <button id="run-btn-2" onclick="runSkulpt('-2')">&#9654; Run</button>
      <button id="reset-btn-2" onclick="resetSkulpt('-2')">&#8635; Reset</button>
    </div>
    <pre id="output-2"></pre>
  </div>
  <div id="canvas-container-2">
    <div id="turtle-target-2"></div>
  </div>
</div>
```

Do not add the `<script>` CDN tags a second time — one copy per page is enough.

---

## General Writing Style

- **Audience**: Kids ages 10–14, just finished learning Scratch
- **Tone**: Friendly, encouraging, never condescending
- **Sentences**: Short and clear — aim for a 5th-grade reading level
- **Code comments**: Use `#` comments in Python code to explain non-obvious lines; omit comments on lines that are self-explanatory
- **New terms**: Bold on first use, define immediately with a plain-English analogy (see [New Vocabulary](#new-vocabulary))
- **Experiments section**: Every lesson must end with 3–5 numbered experiments. Each must include a **"You'll know it worked when…"** success criterion so students can self-assess without a teacher present
- **No external links to Trinket** in Skulpt lessons — these labs are fully self-contained
- **One idea at a time**: Never introduce more than one new concept in a single code example (see [One New Concept Per Lab](#one-new-concept-per-lab))
