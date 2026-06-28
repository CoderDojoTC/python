---
title: Python Code Structure
description: Learn how Python uses indentation to group code, discover Python keywords, and add named colors to your turtle drawings.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:35:09
version: 0.09
---

# Python Code Structure

## Summary

Python has a very clean look: instead of curly braces or `begin/end` keywords,
it uses **indentation** (spaces) to group lines of code together.
This chapter explores those rules — indentation, code blocks, statements,
whitespace — plus Python keywords and named colors that you'll use with turtle.

## Concepts Covered

This chapter covers the following 7 concepts from the learning graph:

1. Multi-Line Strings
2. Indentation as Syntax
3. Python Keywords
4. Code Block Structure
5. Statement vs Expression
6. Whitespace Rules
7. Named Colors

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Welcome to Python and Skulpt](../01-welcome-to-python/index.md)

---

By the end of this lesson you'll be able to:

- Write multi-line text using triple quotes
- Explain why Python uses indentation to group lines of code together
- Recognize Python keywords and understand why they cannot be used as variable names
- Use named colors like `"red"` and `"forestgreen"` in turtle graphics programs

In Chapter 1 you wrote your first Python lines: `print()`, comments, and a turtle drawing. Now you are ready to look at how Python is *structured* — the rules that govern how code is arranged on the page and what makes a Python program readable and correct.

!!! mascot-welcome "Welcome Back, Coder!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ready to go deeper? This chapter is all about how Python code is organized — and the rules are simpler than you might think. By the end you will also make your turtle drawings way more colorful. Let's code it together!

## Multi-Line Strings

In Chapter 1 you used `print()` to display text surrounded by double quotes, like `"Hello, world!"`. That works great for short messages on one line. But what if you want to write several lines of text stored in a single variable?

Python solves this with a **multi-line string** — a string that spans multiple lines, created by wrapping text in **triple quotes**: three double-quote marks (`"""`) or three single-quote marks (`'''`). Everything between the opening triple quotes and the closing triple quotes — including line breaks — becomes part of the string.

```python
haiku = """An old silent pond.
A frog jumps into the pond.
Splash! Silence again."""
print(haiku)
```

**Before you click Run:** how many lines do you think will appear in the output? Count the line breaks inside the triple quotes to make your prediction!

## Try It: Multi-Line Strings

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">haiku = """An old silent pond.
A frog jumps into the pond.
Splash! Silence again."""
print(haiku)
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

Were you right? Three lines appear — one for each line inside the triple quotes. The variable `haiku` holds all three lines as a single string, and `print()` displays them all at once with the line breaks preserved.

## How Multi-Line Strings Work

A regular string uses one pair of quotes: `"Hello"`. A multi-line string uses three pairs: `"""Hello"""`. The triple quotes tell Python: "keep reading until you see three more quotes — no matter how many line breaks are in between."

| Syntax | Can span multiple lines? | Example |
|--------|-------------------------|---------|
| `"text"` | No — one line only | `"Hello, world!"` |
| `'text'` | No — one line only | `'Hello, world!'` |
| `"""text"""` | Yes | `"""Line one\nLine two"""` |
| `'''text'''` | Yes | `'''Line one\nLine two'''` |

Multi-line strings are useful for writing poems, paragraphs, or any block of text you want to keep together in one variable.

## Indentation as Syntax

Most programming languages use **curly braces** `{ }` or the words `begin` and `end` to show that lines of code belong together. Python does something different — it uses **indentation**: the number of spaces at the start of each line.

**Indentation** means pressing the spacebar (or the Tab key) before a line of code to push it to the right. In Python, indentation is not just for looks — it is part of the grammar of the language. Python reads the spaces at the start of a line to decide which lines belong together.

!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, you put blocks *inside* another block (like a Repeat block) by dragging them so they snap together inside it. In Python, you put lines *inside* a group by **indenting** them — adding 4 spaces at the start. The visual nesting you saw in Scratch now lives in those 4 spaces of whitespace.

Here is a preview of what indentation looks like in action. You have not learned `for` loops yet — that is Chapter 7 — but look at the spacing pattern right now:

```python
# PREVIEW — you will learn for loops in Chapter 7
# For now, just notice the indentation pattern

for i in range(4):   # This line starts at the left edge
    t.forward(100)   # These two lines are indented 4 spaces
    t.right(90)      # They belong INSIDE the for loop
```

The two lines with 4 spaces before them are *inside* the loop. The `for` line itself is at the left edge. That difference in spacing is what Python uses to know which lines are part of the loop — not braces, not keywords, just spaces.

!!! mascot-warning "IndentationError — The Most Common Python Mistake"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    If you accidentally put too many spaces, too few spaces, or mix tabs with spaces, Python will stop and show you an `IndentationError`. This is one of the most common errors beginners see. The fix is always the same: use exactly **4 spaces** for each level of indentation, and never mix tabs and spaces. Most code editors (including Skulpt) automatically insert 4 spaces when you press Tab.

## Code Block Structure

A **code block** is a group of lines that belong together because they are all indented at the same level. Every block starts after a line that ends with a colon `:`, and every line in the block is indented by exactly 4 more spaces than the line that opened it.

You will see this pattern constantly in Python:

```python
some_statement:        # colon opens a block
    first line         # 4 spaces — inside the block
    second line        # 4 spaces — still inside the block
    third line         # 4 spaces — still inside the block
back_to_normal         # 0 spaces — block is over
```

Right now all your programs are a flat list of lines with no blocks. That changes when you reach loops (Chapter 7) and conditionals (Chapter 9). When you get there, you will already understand how blocks work — because you are learning it now.

## Whitespace Rules

Whitespace is the name for any invisible characters in your code: spaces, tabs, and blank lines. Python has clear rules about how whitespace is used:

- **Inside a line:** add a single space around operators (`2 + 3`, not `2+3`) to make expressions easier to read. Python ignores extra spaces inside a line, but one space is the convention.
- **At the start of a line:** these spaces are *indentation* and they matter to Python (see above).
- **Blank lines:** Python ignores blank lines completely. Use them to separate logical sections of your program.

Here is the same turtle program written two ways:

```python
# Hard to read — no whitespace
import turtle
t=turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
```

```python
# Easy to read — good whitespace
import turtle

t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
```

Both programs do exactly the same thing. The second one is much easier to read at a glance. Good programmers always choose the second style.

## Python Keywords

Python reserves certain words for its own use. These are called **keywords** — words that already mean something specific in the Python language and cannot be used as names for your variables or functions.

For example, `for` is a Python keyword. You cannot name a variable `for` because Python would be confused — it would not know whether you meant the loop command or a variable. The same is true for `if`, `while`, `def`, `class`, and all the others in the table below.

Here is the complete list of Python keywords:

| Keywords | | | | |
|---|---|---|---|---|
| `False` | `None` | `True` | `and` | `as` |
| `assert` | `async` | `await` | `break` | `class` |
| `continue` | `def` | `del` | `elif` | `else` |
| `except` | `finally` | `for` | `from` | `global` |
| `if` | `import` | `in` | `is` | `lambda` |
| `nonlocal` | `not` | `or` | `pass` | `raise` |
| `return` | `try` | `while` | `with` | `yield` |

You do not need to memorize this list. As you write more Python programs, you will naturally come to recognize the keywords — most code editors highlight them in a different color to help you spot them at a glance.

## Statement vs Expression

Two words come up constantly when talking about Python code: **statement** and **expression**. They sound similar but they do different jobs.

A **statement** is an instruction that *does* something. It performs an action. Statements do not produce a value you can store or pass around — they just act.

An **expression** is a piece of code that *produces a value*. You can use an expression anywhere a value is expected — store it in a variable, pass it to a function, or print it.

The table below shows examples side by side:

| Type | Example | What it does |
|------|---------|-------------|
| Statement | `print("Hello")` | Displays text — does not produce a value |
| Statement | `import turtle` | Loads a library — does not produce a value |
| Expression | `2 + 3` | Produces the value `5` |
| Expression | `"Hello"` | Produces the string `"Hello"` |
| Expression | `100 * 2` | Produces the value `200` |

In practice, many lines of Python combine both: `print(2 + 3)` is a *statement* (the print) that contains an *expression* (the addition). Knowing the difference helps you understand error messages — Python will tell you when it expected an expression and got a statement, or the other way around.

## Named Colors

The turtle library knows the names of hundreds of colors. Instead of describing a color mathematically, you can use a color's English name — a **named color** — as a string. Just pass it to `t.pencolor()` before you draw a line and the turtle will switch to that color.

Some named colors you can use right away:

- Common: `"red"`, `"blue"`, `"green"`, `"yellow"`, `"orange"`, `"purple"`, `"black"`, `"white"`
- Shades: `"forestgreen"`, `"skyblue"`, `"salmon"`, `"coral"`, `"gold"`, `"crimson"`
- Fun ones: `"hotpink"`, `"deepskyblue"`, `"limegreen"`, `"tomato"`, `"orchid"`

The complete list of named colors comes from a standard called **X11 colors**, which includes 140 names. You can experiment freely — if a name does not work, you will see an error in the output box and you can try a different spelling.

Here is a turtle program that draws a square with a different color on each side:

```python
import turtle

t = turtle.Turtle()

t.pencolor("red")
t.forward(100)
t.right(90)

t.pencolor("blue")
t.forward(100)
t.right(90)

t.pencolor("forestgreen")
t.forward(100)
t.right(90)

t.pencolor("orange")
t.forward(100)
```

!!! mascot-thinking "What Will You See?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Look at the program above. The turtle calls `pencolor()` four times — once before each side. How many different colors will you see in the drawing? What color will the very last side be? Make your predictions, then click Run!

## Try It: Colored Turtle Drawing

<div id="skulpt-lab-2">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">import turtle

t = turtle.Turtle()

t.pencolor("red")
t.forward(100)
t.right(90)

t.pencolor("blue")
t.forward(100)
t.right(90)

t.pencolor("forestgreen")
t.forward(100)
t.right(90)

t.pencolor("orange")
t.forward(100)
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

Were you right? Each side of the square is a different color — red, blue, forest green, and orange. Notice the blank lines in the code separating each color-change group: they do not affect how the program runs, but they make the structure immediately clear to a reader.

## How pencolor() Works

`t.pencolor("color name")` changes the color of the turtle's pen for all lines drawn after that call. It does not affect lines already drawn. Think of it like changing the color of a marker before drawing the next stroke.

| Line | What it does |
|------|-------------|
| `t.pencolor("red")` | Switches the pen to red |
| `t.forward(100)` | Draws a red line 100 steps long |
| `t.pencolor("blue")` | Switches the pen to blue |
| `t.forward(100)` | Draws a blue line 100 steps long |

The color stays set until you call `pencolor()` again with a different color. If you never call `pencolor()`, the turtle draws in black by default.

## Learning Check

!!! mascot-thinking "Your Turn — Add the Missing Color"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below draws a three-sided shape, but the second side is missing its color change — it will draw in whatever color came before it. Add **one line** — a `t.pencolor()` call with the color `"purple"` — between the first `t.right(90)` and the second `t.forward(100)` to make the second side purple.

<div id="skulpt-lab-3">
  <div id="editor-container-3">
    <textarea id="code-3" spellcheck="false">import turtle

t = turtle.Turtle()

t.pencolor("red")
t.forward(100)
t.right(120)

# Add one line here to change the color to purple

t.forward(100)
t.right(120)

t.pencolor("gold")
t.forward(100)
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

When you add the right line and click Run, you should see a triangle with sides in red, purple, and gold. If the second side is still red, check that you spelled `pencolor` in all lowercase and passed `"purple"` in quotes.

## Experiments

Try these changes to the programs above. For each one, predict what will happen first — then run it to check!

1. **Write your own multi-line string.** Change the haiku in the first program to a three-line poem you make up yourself. **You'll know it worked when** your poem appears in the output, one line at a time.

2. **Change the colors in the square program.** Replace `"red"` with `"hotpink"`, `"blue"` with `"deepskyblue"`, `"forestgreen"` with `"limegreen"`, and `"orange"` with `"gold"`. **You'll know it worked when** the square draws in your four new colors.

3. **Add a fifth side.** In the square program, add `t.pencolor("purple")` and `t.right(90)` and `t.forward(100)` at the end. Does the result look like a square with an extra line? **You'll know it worked when** you see a fifth line drawn in purple.

4. **Try a color that might not exist.** Change one `pencolor()` argument to `"neonblue"` and run the program. Read the error message carefully — it tells you what went wrong. Then switch it back to a valid color like `"cornflowerblue"`.

5. **Challenge — draw a rainbow triangle.** Use three named colors of your choice to draw an equilateral triangle (three equal sides, `right(120)` at each corner). Add blank lines and comments in the code to label each side. **You'll know it worked when** you see a closed triangle with three distinct colors and clean, readable code.

!!! mascot-celebration "Brilliant Work!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You just learned how Python organizes code — multi-line strings, indentation, keywords, code blocks, statements, expressions, and whitespace rules — and you made your turtle drawings colorful in the process. Seven concepts in one chapter, and you handled them all beautifully. Keep going — you are building real programming skills! Let's code it together!
