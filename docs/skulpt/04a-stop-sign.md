# Python Turtle Graphics Stop Sign

In this lesson we use variables and a `for` loop to draw a stop sign.
We will also use `penup`, `pendown`, `color`, `begin_fill`, `end_fill`, and `write`.
The `write` function changes font size with the `font=("Arial", 30, "normal")` parameter.

## Sample Code

```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
sides = 8
# The angle we turn is related to the number of sides by this formula
angle = 360 / sides
my_color = "red"

dan.penup()
dan.goto(-50, 100)
dan.pendown()
dan.color(my_color)
dan.begin_fill()
# repeat the forward/right functions for each side
for i in range(sides):
   dan.forward(distance)
   dan.right(angle)

dan.end_fill()
dan.hideturtle()

dan.penup()
dan.right(110)
dan.forward(80)
dan.color('white')
dan.write('STOP', font=("Arial", 30, "normal"))
```

## Try It Now

Edit the code below and click **Run** to draw the stop sign right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
sides = 8
# The angle we turn is related to the number of sides
angle = 360 / sides
my_color = "red"

dan.penup()
dan.goto(-50, 100)
dan.pendown()
dan.color(my_color)
dan.begin_fill()
for i in range(sides):
   dan.forward(distance)
   dan.right(angle)

dan.end_fill()
dan.hideturtle()

dan.penup()
dan.right(110)
dan.forward(80)
dan.color('white')
dan.write('STOP', font=("Arial", 30, "normal"))
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

## How It Works

The stop sign is an **octagon** (8 sides). The turn angle is calculated from the number of sides:

```
angle = 360 / 8 = 45 degrees
```

`begin_fill()` and `end_fill()` tell the turtle to fill the shape with the current color.
`goto(-50, 100)` moves the turtle to the starting corner without drawing.
`hideturtle()` hides the turtle icon after drawing is complete.
`write('STOP', font=...)` places text at the turtle's current position.

## Explanation

| Line | What it does |
|------|-------------|
| `distance = 50` | length of each side in pixels |
| `sides = 8` | number of sides (octagon) |
| `angle = 360 / sides` | exterior turn angle — works for any regular polygon |
| `my_color = "red"` | store the color in a variable so it's easy to change |
| `penup() / goto() / pendown()` | move to start position without drawing a line |
| `begin_fill() / end_fill()` | fill the shape with the current color |
| `hideturtle()` | hide the turtle cursor when done |
| `write('STOP', font=...)` | write text at the current position |

## Experiments

1. Change `my_color = "red"` to `"blue"` or `"green"` — what happens?
2. Change `distance = 50` to `80` — does the sign get bigger?
3. Change `sides = 8` to `6` — do you get a hexagon instead?
4. Change `'STOP'` to your own word — does it appear on the sign?
5. Try changing `"white"` to another color for the text — can you read it?
