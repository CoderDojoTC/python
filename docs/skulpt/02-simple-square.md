# Drawing a Square

The following program draws a square using Python turtle graphics.
The turtle moves forward 100 units and turns right 90 degrees — four times — to complete the square.

## Sample Code

```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)
```

## Try It Now

Edit the code below and click **Run** to see the turtle draw your square right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">import turtle
dan = turtle.Turtle()
dan.shape('turtle')

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)
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

The turtle starts in the **center** of the canvas facing right.

Each `forward(100)` moves it 100 units in the direction it is facing.
Each `right(90)` rotates it 90 degrees clockwise.
After four forward+turn pairs the turtle is back where it started — a perfect square.

## Explanation

| Line | What it does |
|------|-------------|
| `import turtle` | loads the turtle graphics library |
| `dan = turtle.Turtle()` | creates a turtle named `dan` |
| `dan.shape('turtle')` | shows the turtle icon instead of an arrow |
| `dan.forward(100)` | moves 100 units forward |
| `dan.right(90)` | turns 90 degrees clockwise |

## Experiments

Try changing these values and clicking **Run** to see what happens:

1. Change `100` to `150` — does the square get bigger?
2. Change `90` to `120` — what shape do you get with 3 repeats instead of 4?
3. Add `dan.color('red')` before the first `forward` — does the line turn red?
4. Can you draw two squares of different sizes?
