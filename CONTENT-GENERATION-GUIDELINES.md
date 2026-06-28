# Content Generation Guidelines — Beginning Python

This file defines rules for generating student-facing content in this course.
All AI agents and human authors creating lessons, labs, quizzes, or other
student-facing pages must follow these guidelines. Instructor-facing content
(teacher's guide, course description) does not need to use the mascot.

---

## Learning Mascot: Monty the Python

### Mascot File Index

The canonical files for this mascot. When editing any of these, update the
others in the same turn so they stay in sync.

| File | Purpose |
|------|---------|
| [`docs/img/mascot/neutral.png`](docs/img/mascot/neutral.png) | Default / general-purpose pose |
| [`docs/img/mascot/welcome.png`](docs/img/mascot/welcome.png) | Chapter-opening pose |
| [`docs/img/mascot/thinking.png`](docs/img/mascot/thinking.png) | Key-concept pose |
| [`docs/img/mascot/tip.png`](docs/img/mascot/tip.png) | Hint / helpful-guidance pose |
| [`docs/img/mascot/warning.png`](docs/img/mascot/warning.png) | Common-mistake / pitfall pose |
| [`docs/img/mascot/encouraging.png`](docs/img/mascot/encouraging.png) | Difficult-content / struggle pose |
| [`docs/img/mascot/celebration.png`](docs/img/mascot/celebration.png) | End-of-chapter / achievement pose |
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
directories deep (e.g., `skulpt/02-simple-square/` or `trinket/04-loops/`).
For pages at the root of `docs/`, use `img/mascot/`.
For pages one level deep (e.g., `docs/strategy/index.md`), use `../img/mascot/`.

### Placement Rules

| Context | Admonition Type | Image | Frequency |
|---------|----------------|-------|-----------|
| Lesson opening | `mascot-welcome` | `welcome.png` | Once per lesson — always first |
| Key concept or insight | `mascot-thinking` | `thinking.png` | 1–2 per lesson |
| Helpful hint or shortcut | `mascot-tip` | `tip.png` | As needed |
| Common mistake / pitfall | `mascot-warning` | `warning.png` | As needed |
| Difficult content | `mascot-encourage` | `encouraging.png` | Where students may struggle |
| End of lesson / experiments | `mascot-celebration` | `celebration.png` | Once per lesson — always last |
| General sidebar | `mascot-neutral` | `neutral.png` | As needed |

### Hard Limits

- **Maximum 6 mascot admonitions per lesson** — more than this interrupts reading flow
- **No back-to-back mascot admonitions** — always separate with at least one paragraph of content
- **One `mascot-welcome` maximum per lesson** — always at the very start
- **One `mascot-celebration` maximum per lesson** — always at the very end
- Do not use mascot admonitions purely for decoration — every use must add instructional value

### Do's and Don'ts

**Do:**
- Use Monty to introduce new topics warmly at the start of every lesson
- Include the catchphrase "Let's code it together!" in welcome admonitions
- Keep dialogue brief (1–3 sentences maximum)
- Match the pose image to the content type (tip pose for tips, warning pose for warnings)
- Write in Monty's encouraging, kid-friendly voice

**Don't:**
- Use Monty more than 6 times in a single lesson
- Put mascot admonitions back-to-back without intervening content
- Change Monty's personality or make him sound sarcastic or intimidating
- Use `<img>` HTML tags — always use Markdown image syntax with `{ class="mascot-admonition-img" }`
- Place images in the admonition title bar

---

## Skulpt Lab Format

All Skulpt interactive labs share a common structure. When generating a new
Skulpt lab page, follow this template exactly:

### Page Structure

```markdown
# Lesson Title

Brief intro paragraph (1–2 sentences about what the lesson covers).

!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    1–3 sentences from Monty introducing the lesson in his encouraging voice.

## Sample Code

[fenced code block with Python]

## Try It Now

Edit the code below and click **Run** to see the result right on this page.
No account needed — everything runs in your browser.

[Skulpt lab HTML block — see below]

## How It Works

Explanation of the key concepts in the code.

[optional mascot-thinking or mascot-tip admonition here]

## Explanation Table

| Line | What it does |
|------|-------------|
| ... | ... |

[optional mascot-warning admonition if there are common mistakes]

## Experiments

1–5 numbered experiments for students to try.

!!! mascot-celebration "Great Work!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Congratulations! You've completed this lesson. Try the experiments above to go further!
```

### Skulpt HTML Block

Every Skulpt lab uses this exact HTML block. The CDN scripts load Skulpt;
`skulpt.js` (via `extra_javascript`) and `skulpt.css` (via `extra_css`)
provide the shared functions and styles.

```html
<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

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

**Rules:**
- The Python code inside `<textarea>` must match the Sample Code block exactly
- Do not add inline `<style>` or `<script>` tags — all CSS/JS is centralized
- The element IDs (`skulpt-lab`, `editor-container`, `code`, `button-row`,
  `run-btn`, `reset-btn`, `output`, `canvas-container`, `turtle-target`) must
  not be changed — `skulpt.js` depends on them

---

## General Writing Style

- **Audience**: Kids ages 10–14, just after learning Scratch
- **Tone**: Friendly, encouraging, never condescending
- **Sentences**: Short and clear — aim for a 6th-grade reading level
- **Code comments**: Use `#` comments in Python code to explain non-obvious lines
- **Experiments section**: Every lesson must end with 3–5 open-ended experiments
  that invite students to modify the code and explore
- **No external links to Trinket** in new Skulpt lessons — these labs are self-contained
