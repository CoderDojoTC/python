# Drawing a Stop Sign

By the end of this lesson you'll be able to:

- Use variables to store the color, size, and number of sides of a shape
- Use a `for` loop to draw any regular polygon without repeating code
- Fill a shape with color using `begin_fill()` and `end_fill()`

A stop sign is an octagon — a regular 8-sided polygon. Instead of writing eight
`forward`/`right` pairs by hand, you'll use a loop and a formula to draw it in just
a few lines.

!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ready to level up? In this lesson we're going to draw a real stop sign —
    red fill, white STOP text, and everything. A `for` loop is going to do all the
    heavy lifting for us. Let's code it together!

## Using Variables for Shape Properties

When you store the size and color in **variables**, changing the whole drawing is as easy
as editing one line. A **variable** is a named box that holds a value — give it a
descriptive name so the code is easy to read.

```python
distance = 50   # length of each side
sides = 8       # number of sides (8 = octagon)
my_color = "red"
```

The turn angle for any regular polygon follows a simple formula: divide 360 by the number
of sides. For an octagon: 360 ÷ 8 = 45 degrees.

!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch you used **variables** in the Variables drawer — `set [distance] to 50`.
    In Python, `distance = 50` does exactly the same thing: it creates a variable named
    `distance` and stores the value 50 in it.

## Filling a Shape with Color

Two commands work as a pair to paint the inside of any shape:

- `begin_fill()` — tells the turtle "start remembering the path"
- `end_fill()` — tells the turtle "now fill in everything inside that path"

Everything drawn between those two calls gets filled with the current color. If you
forget either one, the fill won't appear.

## Sample Code

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 50
sides = 8
angle = 360 / sides  # works for any regular polygon
my_color = "red"

monty.penup()
monty.goto(-50, 100)
monty.pendown()
monty.color(my_color)
monty.begin_fill()

for i in range(sides):
    monty.forward(distance)
    monty.right(angle)

monty.end_fill()
monty.hideturtle()

monty.penup()
monty.right(110)
monty.forward(80)
monty.color('white')
monty.write('STOP', font=("Arial", 30, "normal"))
```

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Look at the line `for i in range(sides):` — and remember that `sides = 8`.
    How many times will the loop repeat? And what color will the inside of the shape be?
    Make your guesses — then click Run!

## Try It Now

Edit the code below and click **Run** to draw the stop sign right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 50
sides = 8
angle = 360 / sides  # works for any regular polygon
my_color = "red"

monty.penup()
monty.goto(-50, 100)
monty.pendown()
monty.color(my_color)
monty.begin_fill()

for i in range(sides):
    monty.forward(distance)
    monty.right(angle)

monty.end_fill()
monty.hideturtle()

monty.penup()
monty.right(110)
monty.forward(80)
monty.color('white')
monty.write('STOP', font=("Arial", 30, "normal"))
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

Were you right? The loop runs **8 times** (once for each side of the octagon) and the
inside fills with red because `my_color = "red"` was set before `begin_fill()`.

## How It Works

The turn angle formula `360 / sides` is the secret: the exterior angles of any regular
polygon always add up to exactly 360 degrees. Divide by the number of sides and you get
the angle for one corner.

`goto(-50, 100)` moves the turtle to a starting corner without drawing — `penup()` lifts
the pen first so no line appears. `pendown()` lowers it again before drawing begins.

`hideturtle()` removes the turtle icon when drawing is finished so it doesn't cover the artwork.

`write('STOP', font=...)` places text at the turtle's current position using the
specified font family, size, and style.

## Explanation Table

| Line | What it does |
|------|-------------|
| `distance = 50` | Length of each side in pixels |
| `sides = 8` | Number of sides — change this to get a different polygon |
| `angle = 360 / sides` | Turn angle — the formula works for any regular polygon |
| `my_color = "red"` | Stores the color in a variable so it's easy to change |
| `penup() / goto() / pendown()` | Move to start position without drawing a line |
| `begin_fill() / end_fill()` | Fill everything drawn between them with the current color |
| `for i in range(sides):` | Repeat the loop body once for each side |
| `hideturtle()` | Hides the turtle cursor when drawing is done |
| `write('STOP', font=...)` | Writes text at the turtle's current position |

## Learning Check

!!! mascot-warning "Spot the Bug!"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    The program below should draw a filled red octagon, but when you run it the shape
    has no fill — just an outline. One line is in the wrong place. Can you find it and
    fix it?

<div id="skulpt-lab-2">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 50
sides = 8
angle = 360 / sides
my_color = "red"

monty.penup()
monty.goto(-50, 100)
monty.pendown()
monty.color(my_color)

for i in range(sides):
    monty.forward(distance)
    monty.right(angle)

monty.begin_fill()  # bug: this is in the wrong place!
monty.end_fill()
monty.hideturtle()
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

Try these changes to the stop sign code above. Predict what will happen first, then run it!

1. Change `my_color = "red"` to `"blue"`.
   **You'll know it worked when** the octagon fills with blue instead of red.

2. Change `distance = 50` to `80`.
   **You'll know it worked when** the stop sign is noticeably larger.

3. Change `sides = 8` to `6` — and also update `angle = 360 / sides` stays the same (it recalculates automatically).
   **You'll know it worked when** you see a filled hexagon instead of an octagon.

4. Change `'STOP'` to your own word.
   **You'll know it worked when** your word appears on the sign in white.

5. Change `monty.color('white')` (the text color) to `'yellow'`.
   **You'll know it worked when** the text on the sign turns yellow. Can you still read it easily?

!!! mascot-celebration "Great Work!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You drew a stop sign using variables, a loop, and fill commands — that's serious Python!
    Try changing `sides` to 3 or 5 and see what signs you can invent.
    Let's code it together!
