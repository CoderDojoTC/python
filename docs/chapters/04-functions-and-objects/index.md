---
title: Functions and Objects
description: Learn how to define and call functions using def, add positional parameters, return values, document code with docstrings, and get a first look at the Standard Library and Python objects.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 09:19:38
version: 0.09
---

# Functions and Objects

By the end of this lesson you'll be able to:

- Define a function in Python using `def` and call it by name
- Add **parameters** so a function can work with different values each time you call it
- Use a `return` statement to send a result back from a function

Imagine you have a task you need to do over and over — say hello to each person on a list, calculate the area of many different rectangles, or draw the same shape in ten different colors.
You could write out every step every single time.
Or you could give those steps a name, write them once, and use that name whenever you need the job done.
That is exactly what a **function** does in Python.

!!! mascot-welcome "Welcome to Chapter 4!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Functions are one of the biggest ideas in all of programming — they save you from writing the same code twice, keep your programs neat, and let you build bigger things from smaller pieces. You have already used functions every single lesson — `print()` is a function! Today you learn how to build your own. Let's code it together!

## What Is a Function?

You have been calling functions since Chapter 1.
Every time you write `print("Hello")` you are calling a function called `print`.
Someone wrote the steps that make `print` work — you just call it by name and hand it a value.

A **function** is a named group of steps that you can run any time by writing its name.

In this chapter you learn to create your own functions — not just use the ones Python provides.
The keyword that starts a function definition is `def`, which is short for "define."

!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, you used **"Make a Block"** to create a custom block — a group of blocks you could snap in anywhere you needed that action. Python's `def` does exactly the same thing. You write the steps once under a name, then call that name wherever you need it. Same idea, just written as text instead of snapped together as blocks!

## Defining a Function with `def`

To create your own function, you write:

1. The keyword `def`
2. The function's name (use snake_case, just like variable names from Chapter 3)
3. A pair of parentheses `()`
4. A colon `:`
5. Indented lines that contain the steps to run

Here is the simplest possible function:

```python
def greet():
    print("Hello, coder!")
    print("Let's code it together!")
```

The colon at the end of the `def` line is required — just like the colons you will see later with loops and conditionals.
Everything indented below the `def` line belongs to the function body.
When Python reads this, it **remembers** the function but does not run the steps yet.
Think of it like writing a recipe on a card: writing the card is not the same as actually cooking the meal.

## Calling a Function

Defining a function and calling a function are two separate actions.

- **Defining** writes the recipe under a name.
- **Calling** says "run the recipe right now."

You call a function by writing its name followed by parentheses:

```python
greet()
```

That one line triggers all the steps inside `greet`.
You can call the same function as many times as you like — Python runs the entire body each time.

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below defines `greet()` and then calls it three times. How many lines of text do you think will appear in the output? Make your prediction — then click Run to find out!

## Try It Now

Edit the code below and click **Run** to see the result right on this page.
No account needed — everything runs in your browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">def greet():
    print("Hello, coder!")
    print("Let's code it together!")

greet()
greet()
greet()
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
Calling `greet()` three times printed six lines — two per call.
That is the power of functions: write the steps once, run them as many times as you need.

**If you see a red error message:** The two most common causes are a missing colon after `def greet()` or wrong indentation inside the function body.
Python requires that every line inside the function body be indented by exactly four spaces.
If the `print` lines start at the left edge instead of being indented, Python will give you an `IndentationError`.

## How It Works

Python reads your program from top to bottom, but it does not run the function the moment it sees `def`.
It reads and remembers the function, then keeps going.
When it finally reaches `greet()`, that is the signal — only then does it jump into the function body and run both `print` lines.
After the function body finishes, Python returns to where it left off and runs the next line.

The table below traces each line of the program:

| Line | What it does |
|------|-------------|
| `def greet():` | Defines a new function named `greet` — Python remembers it but does not run it yet |
| `    print("Hello, coder!")` | Step 1 inside the function body — indented 4 spaces |
| `    print("Let's code it together!")` | Step 2 inside the function body — indented 4 spaces |
| `greet()` | Calls the function — Python jumps in, runs both steps, then comes back |

## Positional Parameters

A function that always does the exact same thing is useful, but limited.
To make a function flexible — able to work with different values each time — you give it **parameters**.

A **parameter** is a variable that lives inside the function and receives a value when you call it.
Think of it like a fill-in-the-blank sentence: "Hello, ______!" is the template, and the blank gets filled in with a different name every time.

You declare parameters inside the parentheses of `def`:

```python
def greet(name):
    print("Hello, " + name + "!")
```

The word `name` between the parentheses is the parameter.
Inside the function body, `name` works just like any variable from Chapter 3.

When you call this function, you supply a value:

```python
greet("Monty")
greet("Python")
```

The values `"Monty"` and `"Python"` are called **arguments** — the real values you pass in at call time.
Python copies the first argument into the first parameter before running the function body.
Because the arguments line up by position (first argument goes to first parameter), they are called **positional parameters**.

Before you click Run on the lab below, predict what you will see.
Which names will appear, and in what order?

## Try It Now — Parameters

<div id="skulpt-lab-2" class="skulpt-text-only">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">def greet(name):
    print("Hello, " + name + "!")

greet("Monty")
greet("Python")
greet("World")
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

Each call to `greet` used the same template — `"Hello, " + name + "!"` — but filled in a different name.
One function, three different outputs.
Try changing the names in the three call lines to greet your friends or family!

## The `return` Statement

So far, every function has done its work by calling `print()` directly.
But sometimes you want a function to **calculate a result and hand it back**, so the rest of your program can use that result.

The keyword `return` sends a value back to the caller.

Here is a function that adds two numbers and returns the sum:

```python
def add(a, b):
    result = a + b
    return result
```

Notice that this function does **not** call `print`.
Instead it hands the result back.
You capture that returned value by storing it in a variable:

```python
total = add(5, 3)
print(total)
```

When Python runs `add(5, 3)`, it copies `5` into `a` and `3` into `b`, calculates `result = 8`, and then `return result` sends `8` back.
That `8` becomes the value of `total`, which is then printed.

The table below shows what each piece does:

| Code | What it does |
|------|-------------|
| `def add(a, b):` | Defines a function with two parameters |
| `    result = a + b` | Adds the two parameters; stores in a local variable |
| `    return result` | Sends the sum back to whoever called `add` |
| `total = add(5, 3)` | Calls the function; the returned value `8` is stored in `total` |
| `print(total)` | Prints `8` |

## Functions Returning None

What happens if a function never uses `return`?

Python still needs to hand something back to the caller.
In that case, it automatically returns a special value from Chapter 3: **None**.

You can see this happen:

```python
def greet():
    print("Hello, coder!")

result = greet()
print(result)
```

The output will be:
```
Hello, coder!
None
```

`greet()` printed a line, then Python returned `None` automatically.
When you stored that in `result` and printed it, you saw `None`.

This is the concept called **functions returning None**: any function that finishes without a `return` statement gives back `None`.
You will not always notice this because most programs do not bother storing the return value of a `print`-only function — but it is good to know it is happening.

!!! mascot-warning "Don't Forget `return`!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A very common beginner bug: you write a function to calculate a value, but you forget to add `return` at the end. The function runs the calculation — but the answer disappears! The calling code gets `None` back instead of the number it expected. If you ever see `None` somewhere you expected a real number, check whether your function is missing a `return` statement.

## Docstrings

Professional Python programmers always document their functions with a **docstring** — a string of text that explains what the function does.

A docstring is written on the first line inside the function body, surrounded by triple quotes (`"""`):

```python
def add(a, b):
    """Add two numbers together and return the sum."""
    result = a + b
    return result
```

The triple quotes can span multiple lines if you need a longer explanation:

```python
def greet(name):
    """
    Print a friendly greeting to the given name.
    
    Parameters:
        name (str): The person's name to greet.
    """
    print("Hello, " + name + "!")
```

Docstrings serve two purposes.
First, they help the next person who reads your code — including future you — understand what the function does without reading every line.
Second, Python tools can read docstrings automatically and display them as help text.
If you type `help(add)` in a Python environment, Python shows the docstring you wrote.

Writing docstrings is a habit worth building from the start.
In this course, every function you write from now on should have at least a one-line docstring.

## The Standard Library: Python's Built-in Toolbox

You have already used one piece of Python's built-in toolbox: the `print()` function.
Python ships with hundreds more pre-written functions organized into **modules** — files full of related functions that you can load into your program with the `import` keyword.

Together, all of these modules make up the **Standard Library** — a collection of tools that comes with every Python installation, completely free.

Here are four modules you will use throughout this course:

| Module | What it contains | Example |
|--------|-----------------|---------|
| `math` | Mathematical functions and constants | `math.sqrt(25)` → `5.0` |
| `random` | Functions for generating random numbers | `random.randint(1, 6)` → rolls a die |
| `time` | Functions for working with time and delays | `time.sleep(1)` → pauses for 1 second |
| `turtle` | Functions and objects for drawing on screen | `turtle.forward(100)` → draws a line |

You import a module by writing `import` followed by the module's name at the top of your program.
After that, you access its functions using dot notation — the module name, a dot, then the function name:

```python
import math
print(math.sqrt(16))
```

That prints `4.0`.
The dot connects the module (`math`) to the function inside it (`sqrt`).
You will use this pattern constantly throughout the rest of the course.

You will meet the `turtle` module in Chapter 5, `random` in Chapter 17, `math` in Chapter 18, and many others as the course progresses.
For now, just know that the Standard Library exists and that `import` is how you unlock it.

## Objects and Classes: A First Look

You are almost ready to meet the `turtle` module.
Before you do, there is one more idea to preview — not fully explain, just introduce — because you will see it the moment you start drawing.

Python organizes many things as **objects**.
An **object** is a package that bundles together two kinds of things:

- **Data** (called attributes) — information the object knows about itself
- **Actions** (called methods) — things the object can do

The classic example is a turtle on screen.
A turtle object knows its current position, its direction, its pen color, and whether its pen is up or down (those are its attributes).
A turtle object can move forward, turn, change color, and lift or lower its pen (those are its methods).

When you write code like this in Chapter 5:

```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)
```

`turtle.Turtle()` creates a new turtle object and stores it in the variable `t`.
`t.forward(100)` calls the `forward` method on that object — same dot notation you just saw with modules.

A **class** is the blueprint that describes what attributes and methods an object has.
`turtle.Turtle` is a class; `t` is one individual object (called an **instance**) made from that blueprint.

You do not need to memorize all of this right now.
The important takeaway is that objects come with built-in actions — and you call those actions by writing the object's name, a dot, and the method name.
You will build the mental model step by step starting in Chapter 5, and you will write your own classes in Chapter 25.

## Learning Check

!!! mascot-thinking "Your Turn — Add the Missing Line"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The function below is supposed to multiply two numbers and give the result back — but it is missing one key line. Right now, if you run the code, `product` gets `None` instead of `15`. Add **one line** inside the function so that `print(product)` shows `15`!

<div id="skulpt-lab-3" class="skulpt-text-only">
  <div id="editor-container-3">
    <textarea id="code-3" spellcheck="false">def multiply(a, b):
    """Multiply two numbers and return the result."""
    result = a * b
    # Add one line below to send the result back

product = multiply(3, 5)
print(product)
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

If your output shows `15`, you got it!
The missing line was `return result`.
Without it, Python silently returned `None` — and `None` is not the number you wanted.

## Experiments

Try these changes in the labs above.
For each one, predict what will happen first — then run the code to check!

1. In Lab 1, change `greet()` so it prints only one line: `"Python is awesome!"`. Call it five times. **You'll know it worked when** the output shows five identical lines.
2. In Lab 2, add a fourth call: `greet("your name here")` but replace `your name here` with your actual first name. **You'll know it worked when** the output greets you personally on the fourth line.
3. In Lab 2, add a second parameter called `language` to the function so it prints `"Hello, Monty! You are learning Python."` Hint: you will need to update the `def` line and the `print` line inside the function. **You'll know it worked when** the output includes the language name.
4. In the Learning Check lab, change the call to `multiply(7, 6)`. **You'll know it worked when** the output shows `42`.
5. Write a brand-new function called `square(n)` that returns `n * n`. Call it with a few different numbers and print each result. **You'll know it worked when** `square(4)` prints `16` and `square(10)` prints `100`.

!!! mascot-celebration "Functions Unlocked!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You just learned one of the most important skills in all of programming! `def`, parameters, `return`, `None`, docstrings, the Standard Library, and a first look at objects — that is a full chapter's worth of big ideas. In Chapter 5 you put functions to work immediately, using the `turtle` module to draw on screen. See you there! Let's code it together!
