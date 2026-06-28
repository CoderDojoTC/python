---
title: Text-Only Skulpt Example
description: Demonstrates the text-only Skulpt lab layout where the drawing area is hidden and the editor fills the full content width.
---

# Text-Only Skulpt Example

This page demonstrates the **text-only** Skulpt lab template.
No turtle drawing area appears — the code editor and output panel fill the entire content width.
Use this template for programs that only use `print()` and text output, with no turtle graphics.

## How It Works

Add `class="skulpt-text-only"` to the outer `skulpt-lab` div.
The canvas container is hidden by CSS, but the `turtle-target` element remains in the DOM
so `runSkulpt()` can still initialise without errors.

## Example 1 — Print Statements

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">name = "Python"
version = 3
print("Hello from", name, version)
print("No turtle needed!")
for i in range(1, 6):
    print(i, "squared =", i * i)
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

## Example 2 — User-Defined Function

<div id="skulpt-lab-2" class="skulpt-text-only">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">def greet(first_name, last_name):
    full_name = first_name + " " + last_name
    print("Hello,", full_name + "!")

greet("Ada", "Lovelace")
greet("Grace", "Hopper")
greet("Alan", "Turing")
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

## HTML Template

Copy this block and replace the code inside the `<textarea>` for any text-only lab:

```html
<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">
# your Python code here
print("Hello!")
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

For a second lab on the same page, use the `-2` suffix on all IDs and `runSkulpt('-2')` / `resetSkulpt('-2')` on the buttons (same convention as the drawing labs).

## Contrast: Drawing Lab Template

For programs that use turtle graphics, omit the `skulpt-text-only` class and the canvas appears as normal:

```html
<div id="skulpt-lab">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">
import turtle
t = turtle.Turtle()
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
```
