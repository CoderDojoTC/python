# Drawing a Square

By the end of this lesson you'll be able to:

- Move the turtle forward and turn it using `forward()` and `right()`
- Explain what the numbers inside `forward(100)` and `right(90)` control
- Draw a square by repeating the same two commands four times

The turtle starts in the center of the canvas and draws lines as it moves —
like a pen attached to a robot. In this lesson you'll give it your first
drawing commands and watch a square appear.

!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Hi, I'm Monty! I'm a Python snake, and today I'm going to teach you how to
    make me draw a square on the screen. It's easier than you think —
    let's code it together!

## Moving and Turning

The two most important turtle commands are `forward()` and `right()`.

`forward(100)` tells the turtle to walk **forward** 100 steps, drawing a line as it goes.
The number inside the parentheses is called a **parameter** — it controls how much the
command does. Here, `100` sets how long each side of the square will be.

`right(90)` tells the turtle to **turn right** 90 degrees without drawing anything.
The number 90 is a quarter-turn — exactly the angle at each corner of a square.

!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch you used the **"Move 10 steps"** block and the **"Turn ↻ 15 degrees"** block.
    In Python, `forward(100)` and `right(90)` do exactly the same things — just written differently!

## Sample Code

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)
```

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, count the `forward` commands in the code above.
    How many sides will the turtle draw? Make your guess — then find out!

## Try It Now

Edit the code below and click **Run** to see Monty draw right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">import turtle
monty = turtle.Turtle()
monty.shape('turtle')

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)
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

Were you right? The turtle draws **4 sides** — one for each `forward()` + `right()` pair — making a perfect square.

**If you see a red error message:** Check your spelling — Python is case-sensitive,
so `Forward(100)` won't work but `forward(100)` will.
Make sure you have parentheses `()` around every number.

## How It Works

The turtle starts in the center of the canvas facing right.
Each `forward(100)` moves it 100 steps in the direction it is currently facing.
Each `right(90)` rotates it 90 degrees clockwise — a quarter turn.
After four forward-and-turn pairs the turtle is back where it started: a perfect square.

## Explanation Table

| Line | What it does |
|------|-------------|
| `import turtle` | Loads the turtle graphics library |
| `monty = turtle.Turtle()` | Creates a turtle and names it `monty` |
| `monty.shape('turtle')` | Shows the turtle icon instead of a plain arrow |
| `monty.forward(100)` | Moves 100 steps forward, drawing a line |
| `monty.right(90)` | Turns 90 degrees clockwise (one corner of a square) |

!!! mascot-warning "Common Mistake: Wrong Turn Angle"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    If you change `right(90)` to `right(100)` the corners won't close and you won't get a square!
    A square needs *exactly* 90-degree turns. Try it and see what shape you get instead.

## Learning Check

!!! mascot-thinking "Your Turn — Complete the Triangle"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A triangle has 3 sides. Each corner of an equilateral triangle turns 120 degrees.
    The program below is missing **one line**. Add it so Monty draws a complete triangle!

<div id="skulpt-lab-2">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">import turtle
monty = turtle.Turtle()
monty.shape('turtle')

# Draw a triangle - each turn is 120 degrees
monty.forward(100)
monty.right(120)

monty.forward(100)
# Add the missing line here!

monty.forward(100)
monty.right(120)
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

## Experiments

Try these changes to the square code above. Predict what will happen first, then run it to check!

1. Change `100` to `150` in all four `forward` calls.
   **You'll know it worked when** the square is noticeably larger than before.

2. Change all four `right(90)` calls to `right(120)` and remove one `forward`/`right` pair (leaving only three).
   **You'll know it worked when** you see a triangle instead of a square.

3. Add `monty.color('red')` on the line just before the first `forward`.
   **You'll know it worked when** all four sides of the square are red instead of black.

4. Add `monty.speed(1)` after `monty.shape('turtle')` to slow Monty way down.
   **You'll know it worked when** you can watch him draw each side one at a time.

5. Try drawing two squares side by side: after the four pairs, add
   `monty.penup()`, then `monty.forward(150)`, then `monty.pendown()`,
   then repeat the four `forward`/`right` pairs again.
   **You'll know it worked when** you see two separate squares on the canvas.

!!! mascot-celebration "Great Work!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You just wrote your first turtle drawing program — and it works!
    In the next lesson you'll learn how to use a `for` loop so you don't have to
    repeat those four lines over and over. Let's code it together!
