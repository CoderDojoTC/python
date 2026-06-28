---
title: Variables and Numbers
description: Learn how to create variables, store integers and floats, follow Python naming conventions, and understand the None value.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:55:45
version: 0.09
---

# Variables and Numbers

By the end of this lesson you'll be able to:

- Create a variable in Python and store a number inside it
- Name variables using `snake_case` and choose clear, descriptive names
- Explain the difference between an integer and a float

Imagine you are playing a video game and you need to remember your score.
You could try to hold it in your head — but what if it changes?
What if you need that number in five different places in your code?
A **variable** solves this problem.
A variable is a labeled storage location in your program's memory.
You give it a name, put a value inside it, and Python remembers that value for you.

!!! mascot-welcome "Welcome to Chapter 3!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Variables are one of the most powerful ideas in all of programming — and you've already used them in Scratch! Today we learn how Python does the same thing with just a few keystrokes. Let's code it together!

## What Is a Variable?

Picture a sticky note on your desk.
The front has a name written on it — like **score** — and on the back you write the current value, like **10**.
Whenever you need to know the score, you flip it over and read it.
If the score changes, you erase the old number and write a new one — but the name on the front stays the same.

In Python, a variable works exactly like that sticky note.
You create a variable by writing its name, then an equals sign, then the value you want to store.
This is called **variable assignment**:

```python
score = 10
```

- The name on the left (`score`) is the variable's label.
- The equals sign (`=`) means "store this value in this name."
- The value on the right (`10`) is what gets stored.

Notice that `=` in Python does **not** mean "is equal to" the way it does in math.
It is a one-way instruction: "take the value on the right and put it in the box on the left."
The value flows from right to left, always.

After you store a value, you can read it back using `print()`:

```python
score = 10
print(score)
```

!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, you clicked the **"Set score to 10"** block to create a variable and give it a starting value. In Python, `score = 10` does exactly the same thing — same idea, just written as text instead of snapped together as blocks!

## Sample Code

Here is a short program that creates two variables and prints both of them.
Read through it before you run it.

```python
score = 10
lives = 3
print(score)
print(lives)
```

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, look at those four lines. The program stores two numbers and then prints them. What do you think the output will look like — will both numbers appear, or just one? And in what order? Make your prediction, then click Run to find out!

## Try It Now

Edit the code below and click **Run** to see the result right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">score = 10
lives = 3
print(score)
print(lives)
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

Were you right?
Python printed `10` on the first line and `3` on the second — one value per `print()` call, in the order they appeared.

**If you see a red error message:** Check your spelling carefully.
Python is case-sensitive, so `Score = 10` and `score = 10` are two completely different variables.
Make sure there are no extra spaces around the `=` sign.

## How It Works

When Python runs `score = 10`, it sets aside a small storage location in memory, writes `10` into it, and attaches the label `score`.
When Python then sees `print(score)`, it looks up that label, retrieves the stored value, and displays it.

The table below explains each line of the program:

| Line | What it does |
|------|-------------|
| `score = 10` | Creates a variable named `score` and stores the integer `10` inside it |
| `lives = 3` | Creates a second variable named `lives` and stores `3` inside it |
| `print(score)` | Looks up the value in `score` and prints it |
| `print(lives)` | Looks up the value in `lives` and prints it |

Each variable is independent.
Changing one does not affect the other.
You can have as many variables as you like — your program's memory can hold thousands of them.

## Naming Your Variables

Python lets you name a variable almost anything — but there are rules you must follow:

- **Start with a letter or underscore** — not a digit. `score` is fine; `1score` causes an error.
- **Use only letters, digits, and underscores** — no spaces, hyphens, or symbols like `@` or `!`.
- **Avoid Python keywords** — words like `print`, `for`, `if`, and `while` are reserved. Python needs those words for itself.

Python is also **case-sensitive**: `Score`, `SCORE`, and `score` are three completely separate variables.
Mixing upper and lower case accidentally is one of the most common sources of bugs for beginners.

### Snake_case: Python's Naming Style

When a variable name has more than one word, Python programmers join the words with underscores and keep all letters lowercase.
This style is called **snake_case** (picture the underscores as a snake lying flat between the words).

The table below shows common naming mistakes and their snake_case fixes:

| Problematic name | What's wrong | Better name |
|-----------------|-------------|-------------|
| `myscore` | Words run together — hard to read | `my_score` |
| `MyScore` | Capital letters belong to a different naming style | `my_score` |
| `my score` | Spaces are not allowed in variable names | `my_score` |
| `my-score` | Python reads the dash as **subtraction** — `my - score` — not a name! | `my_score` |
| `x` | Too vague — what does `x` mean? | `player_score` |
| `s` | Single letters give no information | `lives_remaining` |

### Meaningful Variable Names

The best variable names describe exactly what the variable holds.
A name like `player_score` tells you immediately what the number represents.
A name like `x` gives you no information at all.

This matters because programs grow.
A program you write today might be 10 lines — easy to keep in your head.
But programs grow to hundreds and thousands of lines.
When that happens, a good name is the difference between code you can read and code that feels like a puzzle.

!!! mascot-warning "Naming Pitfalls!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Watch out for the dash! If you write `my-score` instead of `my_score`, Python reads the dash as a minus sign and thinks you are subtracting a variable called `score` from a variable called `my`. Use an **underscore** (`_`), never a dash (`-`), to join words in a name. Other common traps: single-letter names like `x` that tell you nothing, capital letters that break snake_case, and accidentally using a Python keyword as your variable name.

## Integers: Whole Numbers

Now that you know how to create and name variables, let's look more carefully at the kinds of numbers Python understands.

A whole number — one with no decimal point — is called an **integer**, or `int` for short.
Integers can be positive, negative, or zero.
You use integers for things you count: the number of lives in a game, the number of sides on a shape, a player's score.

```python
sides = 6
lives = 3
temperature = -5
```

All three of those variables hold integers.

## Floats: Decimal Numbers

A number with a decimal point is called a **float** — short for "floating-point number."
Floats are used for measurements and values that don't land exactly on a whole number.

```python
price = 4.99
height = 1.75
pi = 3.14159
```

The name "float" comes from how computers store these numbers internally — the decimal point can "float" to different positions.
You don't need to know the internal details.
What matters is when to use each type:

| Kind | Python type | When to use | Examples |
|------|-------------|-------------|---------|
| Whole number | `int` | Counting, game scores, number of repetitions | `0`, `7`, `-12`, `1000` |
| Decimal number | `float` | Measurements, money, percentages, averages | `3.14`, `0.5`, `-2.7`, `99.0` |

One important detail: dividing two integers with `/` always gives you a float, even when the result is a whole number.

```python
result = 10 / 2
print(result)
```

That prints `5.0`, not `5` — note the decimal point.
Python uses `//` (floor division) if you want a whole-number result: `10 // 2` gives `5`.

## Variable Reassignment

One of the most powerful things about variables is that you can change them.
You **reassign** a variable by writing its name again on the left side of `=` with a new value on the right.
Python discards the old value and stores the new one under the same label.

Here is a program that changes a score partway through:

```python
score = 10
print(score)

score = 25
print(score)
```

Read through that before you run it.
The first `print` shows the original value.
The second assignment replaces it.
The second `print` shows the updated value.

## Sample Code — Reassignment

```python
score = 10
print(score)

score = 25
print(score)
```

## Try It Now — Reassignment

<div id="skulpt-lab-2" class="skulpt-text-only">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">score = 10
print(score)

score = 25
print(score)
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

Python printed `10` first and `25` second.
The name `score` stayed the same; only the value changed.

You can also use the current value of a variable to calculate a new one:

```python
score = 10
score = score + 5
print(score)
```

Python evaluates the right side first: `score + 5` is `10 + 5`, which equals `15`.
Then it stores `15` back into `score`.
This pattern — "take the old value, add something, store the result back" — appears constantly in real programs.

## None: The "Nothing" Value

Python has one special value that is neither an integer nor a float.
It is called **None**, and its type is called `NoneType`.

None means "no value yet" or "nothing here."
You will see it in two common situations:

1. When you want a variable to exist but you haven't decided its value yet.
2. When a function finishes without returning anything — Python automatically gives back `None` in that case.

```python
winner = None
print(winner)
print(type(winner))
```

Running that program prints:
```
None
<class 'NoneType'>
```

None is not zero.
None is not an empty string.
None is its own special thing that means "the absence of a value."
Think of it like a sticky note that exists on your desk but has nothing written on the back yet.

Later in the course you will use None to mark the start of a search, represent an empty box in a game board, or signal that a function didn't find what it was looking for.

## What `type()` Tells You

Python has a built-in function called `type()` that tells you what kind of value is stored in a variable.
You saw it used with `None` above.
Here it is with an integer and a float:

```python
score = 10
price = 4.99

print(type(score))
print(type(price))
```

Output:
```
<class 'int'>
<class 'float'>
```

The word `class` in the output is how Python describes categories of values.
For now, just read `<class 'int'>` as "this is an integer" and `<class 'float'>` as "this is a float."
You will learn much more about classes later in the course.

## Learning Check

!!! mascot-thinking "Your Turn — Add the Missing Line"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below creates two variables — `player_score` and `bonus_points`. It prints `player_score` just fine, but something is missing: `bonus_points` never gets printed. Add **one line** so the output shows both numbers, one on each line.

<div id="skulpt-lab-3" class="skulpt-text-only">
  <div id="editor-container-3">
    <textarea id="code-3" spellcheck="false">player_score = 42
bonus_points = 10
print(player_score)
# Add one line below to also print bonus_points
</textarea>
    <div id="button-row-3">
      <button id="run-btn-3" onclick="runSkulpt('-3')">&#9654; Run</button>
      <button id="reset-btn-3" onclick="resetSkulpt('-3')">&#8635; Reset</button>
    </div>
    <pre id="output-3"></pre>
  </div>
  <div id="canvas-container-3">
    <div id="turtle-target-3"></div>
  </div>
</div>

If your output shows `42` on the first line and `10` on the second, you got it!
The missing line was `print(bonus_points)`.

## Experiments

Try these changes in the labs above.
For each one, predict what will happen first — then run the code to check!

1. In Lab 1, change `score = 10` to `score = 750`. **You'll know it worked when** the output shows `750` instead of `10`.
2. In Lab 1, add a third variable called `high_score` set to `100`. Add a `print(high_score)` line. **You'll know it worked when** you see three numbers in the output.
3. In Lab 2 (the reassignment lab), change `score = 25` to `score = score * 2`. **You'll know it worked when** the output shows `10` on the first line and `20` on the second.
4. Create a float variable called `average_score` and set it to `87.5`. Print it. **You'll know it worked when** the output shows `87.5`.
5. Create a variable called `champion` and set it to `None`. Print it. Then reassign `champion` to `1`. Print it again. **You'll know it worked when** the output shows `None` on one line and `1` on the next.

!!! mascot-celebration "You've Got Variables!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Variables, integers, floats, snake_case naming, reassignment, None — you now have the building blocks every Python program is built on. Every chapter from here uses what you just learned. Brilliant work, coder! Let's code it together!
