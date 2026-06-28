---
title: Drawing with Turtle Graphics
description: Create your first turtle drawings using the Turtle and Screen objects, movement commands, pen control, colors, shapes, and speed settings.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 09:48:25
version: 0.09
---

# Drawing with Turtle Graphics

By the end of this lesson you'll be able to:

- Create a `turtle.Screen()` and a `turtle.Turtle()` object to set up a drawing window
- Move the turtle forward, backward, left, and right to draw lines
- Lift and lower the pen to skip spaces in your drawing
- Change the turtle's color, thickness, shape, and drawing speed

Imagine a tiny robot with a marker strapped to its belly.
You tell the robot where to walk, and the marker draws a trail wherever it goes.
That is exactly what **turtle graphics** does — and in this chapter you get to write the commands that bring that robot to life.

!!! mascot-welcome "Welcome to Chapter 5!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    This is the chapter where Python becomes truly visual! Every command you type makes your turtle move and draw — instantly, right here in the browser. There is no better way to build your Python instincts than to type a command, click Run, and watch the turtle obey. Let's code it together!

## Setting Up the Drawing Stage

Before any drawing can happen, Python needs two things in place: a **screen** to draw on, and a **turtle** to do the drawing.

### The turtle.Screen() Object

A **`turtle.Screen()`** creates the drawing window — the blank canvas where all your shapes will appear.
Think of it as the stage in a play: you have to set up the stage before the actors can perform.

You store the screen in a variable so you can send it instructions later:

```python
import turtle
wn = turtle.Screen()
```

The name `wn` stands for "window" — that is the most common nickname programmers use for this variable, but you can call it anything you like.

Once you have the screen, you can change its background color using **`bgcolor()`** (short for "background color"):

```python
wn.bgcolor("lightblue")
```

Put any color name in quotes — `"lightyellow"`, `"pink"`, `"white"`, `"black"`, or any of the 140 named web colors Python understands.
`bgcolor()` changes the window background the moment Python runs that line.

### The turtle.Turtle() Object

A **`turtle.Turtle()`** creates your drawing agent — the small arrow (or turtle shape!) that moves around the canvas, leaving a colored line wherever it goes.

In Chapter 4 you learned that **objects** have their own **methods** that you call with a dot.
A turtle is a perfect example of this idea in action.
You create one object and then call methods on it to make it move, turn, and draw.

```python
t = turtle.Turtle()
```

The variable `t` now holds your turtle.
Whenever you want the turtle to do something, write `t.` followed by a command name and parentheses.

!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, the **Stage** was the white backdrop where your sprites lived, and a **Sprite** was the character you programmed to move. In Python turtle, `turtle.Screen()` is your Stage and `turtle.Turtle()` is your Sprite. The big difference? Instead of dragging a sprite with your mouse, you write Python commands to control it — and that gives you far more power than drag-and-drop ever could!

## Moving the Turtle

The turtle always starts at the center of the screen, facing right (East).
You have four movement commands to work with:

| Command | What it does |
|---------|-------------|
| `t.forward(n)` | Move `n` pixels forward in the direction the turtle faces |
| `t.backward(n)` | Move `n` pixels backward (tail-first) |
| `t.right(n)` | Rotate the turtle `n` degrees clockwise |
| `t.left(n)` | Rotate the turtle `n` degrees counter-clockwise |

The `n` in `forward()` and `backward()` is measured in **pixels** — tiny dots on your screen.
One hundred pixels is roughly the length of your thumb held next to a typical monitor.

The `n` in `right()` and `left()` is measured in **degrees**, just like in your geometry class.
A full circle is 360°.
A right-angle corner — like the corner of a piece of paper — is exactly 90°.

These four commands map directly to blocks you already know from Scratch.
The **Move N steps** block is `forward(n)` in Python.
The **Turn ↻ N degrees** block is `right(n)`, and the **Turn ↺ N degrees** block is `left(n)` — same ideas, just written as text.

Before you run the first lab, take a moment to read the code carefully.

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Look at the program below before you click Run.
    The turtle moves forward 100, turns right 90°, moves forward 100, turns right 90°, then moves forward one more time.
    How many sides of a square do you think you will see?
    Make your guess — then click Run to find out!

## Try It Now

Edit the code below and click **Run** to see the result right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">import turtle
wn = turtle.Screen()
wn.bgcolor("lightyellow")
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
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

Were you right? The turtle drew exactly three sides of a square — one 90° right turn for each corner!

**If you see a red error message:** Check your spelling carefully.
Python is case-sensitive, so `Forward(100)` will not work but `forward(100)` will.
Also make sure each line ends with a closing parenthesis `)`.

## How It Works

Here is what each line of the program does:

| Line | What it does |
|------|-------------|
| `import turtle` | Loads the turtle library so Python knows all the drawing commands |
| `wn = turtle.Screen()` | Creates the drawing window and stores it in `wn` |
| `wn.bgcolor("lightyellow")` | Sets the window background to light yellow |
| `t = turtle.Turtle()` | Creates a turtle object and stores it in `t` |
| `t.forward(100)` | Moves the turtle forward 100 pixels in the direction it is currently facing |
| `t.right(90)` | Rotates the turtle 90° clockwise — a perfect right-angle corner |

Notice the pattern: every command uses the object (`wn` or `t`), then a dot, then the method name with a number inside the parentheses.
This is exactly the object-method pattern from Chapter 4.

## Pen Control: penup() and pendown()

Right now the turtle draws a line everywhere it moves.
But what if you want two separate shapes with a gap between them?

Think about drawing with a real pen: you would lift the pen off the paper, slide it to the new spot, then press it back down.
Turtle graphics works the same way.

- **`t.penup()`** lifts the pen off the canvas. The turtle can move without drawing anything.
- **`t.pendown()`** sets the pen back on the canvas. Every step after this leaves a line.

The turtle always starts with the pen down, which is why the very first `forward()` call draws a line.

In Scratch you may have used the **Pen Up** and **Pen Down** blocks from the pen extension — `penup()` and `pendown()` work exactly the same way.

Here is a program that draws two separate lines with a gap in the middle:

```python
import turtle
t = turtle.Turtle()
t.forward(80)      # draw a line
t.penup()          # lift the pen
t.forward(40)      # move 40 pixels — nothing drawn here
t.pendown()        # lower the pen
t.forward(80)      # draw another line
```

Try this in the lab below — pay close attention to the blank space in the middle of the drawing.

<div id="skulpt-lab-2">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">import turtle
t = turtle.Turtle()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
t.forward(80)
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

The gap is where the turtle traveled with its pen in the air.
Try changing the `40` in the middle `t.forward(40)` to `80` — the gap doubles in width.

!!! mascot-warning "Don't Forget pendown()!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    The most common `penup()` mistake is forgetting to call `pendown()` afterward. If your turtle moves but the canvas stays completely blank, look for a missing `pendown()`. The turtle moves exactly as you command it — it just leaves no trace because the pen is still lifted. Add `t.pendown()` before the line you want drawn and you are back in business!

## Pen Size and Color

A black line on a white background is just the beginning.
You can choose any color and any thickness for your turtle's pen.

Two commands control how the line looks:

- **`t.pensize(n)`** sets the line thickness in pixels. The default is `1`. Try `3`, `5`, or `10` to draw bolder lines.
- **`t.pencolor("color")`** sets the color of the line the turtle draws. Use a color name in quotes: `"red"`, `"blue"`, `"green"`, `"orange"`, `"purple"`, or any named web color.

Just like the **Set pen color** block in Scratch, `pencolor()` changes the color for every line drawn after that call.
You can change colors in the middle of a program — each call to `pencolor()` affects only the lines that come after it.

## Turtle Appearance: shape(), hideturtle(), and showturtle()

The default turtle looks like a small arrowhead.
The **`t.shape()`** command swaps it for a different look.
Here are all six built-in shapes:

| Shape name | What it looks like |
|------------|-------------------|
| `"arrow"` | A small arrowhead (the default) |
| `"turtle"` | A top-down cartoon turtle |
| `"circle"` | A filled circle |
| `"square"` | A small filled square |
| `"triangle"` | A small triangle |
| `"classic"` | A slightly different arrowhead shape |

Sometimes you want the turtle cursor to disappear from a finished drawing so it does not distract from your art.
Two commands handle this:

- **`t.hideturtle()`** makes the turtle cursor invisible. Your drawing still shows — the turtle just steps out of the way.
- **`t.showturtle()`** brings a hidden turtle back into view.

## Speed Control: speed()

Every turtle starts at a medium drawing speed.
The **`t.speed(n)`** command controls how fast it moves, using a number from `0` to `10`:

| Value | Speed |
|-------|-------|
| `1` | Slowest — good for watching each step |
| `5` | Medium — the default |
| `10` | Fast |
| `0` | Instant — skips the animation entirely |

Use `speed(0)` when your program draws many lines and you do not want to wait.
Use `speed(1)` when you are learning or debugging and want to see the turtle move one step at a time.

Now try a lab that combines color, appearance, and speed — all in one program:

<div id="skulpt-lab-3">
  <div id="editor-container-3">
    <textarea id="code-3" spellcheck="false">import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.pensize(4)
t.pencolor("blue")
t.forward(100)
t.right(90)
t.pencolor("red")
t.forward(100)
t.hideturtle()
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

Notice that the first line is blue and the second is red — changing `pencolor()` in the middle of a drawing affects only the lines that come after that call.
When the program finishes, the turtle cursor itself disappears because of `hideturtle()`.

## Learning Check

You have now seen all ten commands from this chapter.
Time to put them to the test!
The program below draws two sides of a square and then stops.

!!! mascot-thinking "Your Turn — Add the Missing Line"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below draws two sides of a square and then stops short.
    After the second `t.right(90)`, the turtle is already pointing in the right direction for the third side.
    Add **one line** to make it draw that third side — 100 pixels long.
    Hint: which command moves the turtle forward?

<div id="skulpt-lab-4">
  <div id="editor-container-4">
    <textarea id="code-4" spellcheck="false">import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.pencolor("green")
t.pensize(3)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
# Add ONE line below to draw the third side of the square
</textarea>
    <div id="button-row-4">
      <button id="run-btn-4" onclick="runSkulpt('-4')">&#9654; Run</button>
      <button id="reset-btn-4" onclick="resetSkulpt('-4')">&#8635; Reset</button>
    </div>
    <pre id="output-4"></pre>
  </div>
  <div id="canvas-container-4">
    <div id="turtle-target-4"></div>
  </div>
</div>

If you got it right, you will see three sides of a square drawn in green.
The missing line is `t.forward(100)` — the turtle was already facing the right direction after two right turns, so it just needed one more push forward!

## Experiments

Try these changes to the programs above.
For each one, predict what will happen first — then run it to check!

1. In Lab 1, change both `t.right(90)` calls to `t.right(120)`. **You'll know it worked when** the turtle draws the corner of a triangle instead of a square corner.
2. In Lab 1, change `wn.bgcolor("lightyellow")` to `wn.bgcolor("lightblue")`. **You'll know it worked when** the background turns a soft sky blue.
3. In Lab 2, change the `40` in `t.forward(40)` (the middle one, between penup and pendown) to `100`. **You'll know it worked when** the gap between the two lines is much wider than the lines themselves.
4. In Lab 3, try each of the six shape names in `t.shape()`: `"arrow"`, `"turtle"`, `"circle"`, `"square"`, `"triangle"`, `"classic"`. **You'll know it worked when** the turtle cursor changes shape before it starts drawing.
5. **Challenge:** In Lab 3, change `t.speed(5)` to `t.speed(1)` and watch the turtle draw slowly. Then change it to `t.speed(0)` and run again. What is different? When would each speed setting be useful?

!!! mascot-celebration "You Can Command a Turtle!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You have just learned ten Python turtle commands and used them to draw real shapes on the screen — that is a big deal! In the chapters ahead you will combine these commands with loops and functions to draw patterns no human could make by hand. You have earned this one. Let's keep coding it together!
