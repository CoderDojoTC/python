# Reading Output and Error Messages

By the end of this lesson you'll be able to:

- Tell the difference between normal output and an error message just by its color
- Read what an error message says to figure out where your program went wrong
- Use `print()` checkpoints to narrow down exactly which line caused a crash

When your Python program runs, two kinds of text can appear in the output box.
**Normal output** — anything printed with `print()` — appears in black.
**Error messages** — produced when Python finds a problem — appear in red.
The color makes it easy to see at a glance whether your program finished successfully or crashed.

!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every programmer sees error messages — even professional ones!
    Learning to read them calmly is one of the most useful skills you'll build.
    Let's code it together!

## Normal Output: Everything Goes Right

When a program runs without any problems, every `print()` call produces a line of black text in the output box.
Run the program below and look at the output — all black, no red.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<div id="skulpt-lab" class="skulpt-text-only">
  <div id="editor-container">
    <textarea id="code" spellcheck="false">name = "Alex"
score = 42
bonus = 8
total = score + bonus

print("Player:", name)
print("Score:", score)
print("Bonus:", bonus)
print("Total:", total)
print("Program finished successfully!")
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

All five lines print in black — the program ran from top to bottom without any problems.

## Error Output: Something Went Wrong

Now look at what happens when Python hits a problem partway through a program.
The program below prints two lines successfully, then tries to use a variable called `high_score` that was never created.
Python cannot continue, so it stops and reports the error.

!!! mascot-thinking "What Will the Output Look Like?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, count the `print()` calls in the program below.
    How many lines of output do you think will appear — and what color will each one be?
    Make your prediction, then click Run!

<div id="skulpt-lab-2" class="skulpt-text-only">
  <div id="editor-container-2">
    <textarea id="code-2" spellcheck="false">name = "Alex"
score = 42

print("Player:", name)
print("Score:", score)

# Oops — high_score was never created!
print("High score:", high_score)

print("This line never runs.")
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

Were you right?
Two black lines appeared for the two successful `print()` calls.
Then a red error message appeared — Python stopped when it hit the broken line.
The last `print()` never ran at all because the program crashed before it got there.

## How to Read a NameError

The red message says something like:

```
NameError: name 'high_score' is not defined on line 8
```

Here is what each part means:

| Part | Meaning |
|------|---------|
| `NameError` | The type of error — Python found a name it doesn't recognise |
| `'high_score'` | The exact variable name Python couldn't find |
| `on line 8` | The line number where the crash happened |

To fix this error you have two choices:

1. **Create the variable before you use it** — add `high_score = 100` somewhere above line 8.
2. **Remove or fix the broken line** — if `high_score` shouldn't be there, delete it.

!!! mascot-tip "The Black Lines Are Your Clues"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    When a program crashes, look at the last black line in the output — that tells you the most recent thing that worked. The error happened somewhere between that line and the next `print()` you expected. Use this as your starting point when hunting for the bug!

## Using Print Checkpoints to Find Bugs

Professional programmers often add temporary `print()` calls to trace exactly where a program stops.
Each one says "I made it this far."
When you see the last black checkpoint and then a red error, you know the crash happened between those two points.

Here is the same broken program with checkpoints added.
Notice how the checkpoints help you pinpoint the problem line more precisely:

<div id="skulpt-lab-3" class="skulpt-text-only">
  <div id="editor-container-3">
    <textarea id="code-3" spellcheck="false">print("Checkpoint 1: program started")

name = "Alex"
score = 42
print("Checkpoint 2: variables created")

total = score + 10
print("Checkpoint 3: total calculated:", total)

# Remove the # below to introduce an error and watch where the checkpoints stop:
# print("High score:", high_score)

print("Checkpoint 4: all done!")
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

All four checkpoints print in black — the program is healthy.
Now remove the `#` from in front of `print("High score:", high_score)` and run it again.
Checkpoint 3 will be the last black line, and the red error will appear right after it —
telling you the crash happened between Checkpoint 3 and Checkpoint 4.

!!! mascot-warning "Red Doesn't Mean Failure — It Means Information"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    A red error message is not a sign that you are bad at coding. It is Python telling you exactly what went wrong and where. Read it carefully — it almost always contains the line number and the name of whatever Python couldn't find. The message is your friend!

## Experiments

Try these changes. For each one, predict the output color pattern before you run!

1. In Lab 2, add `high_score = 500` on a new line above `print("High score:", high_score)`.
   **You'll know it worked when** all output is black and "High score: 500" appears.

2. In Lab 2, change `score = 42` to `score = "forty-two"` (a word instead of a number).
   Then change `print("Score:", score)` to `print("Score + 1:", score + 1)`.
   **You'll know it worked when** you see a red `TypeError` — Python can't add a word and a number.

3. In Lab 3, remove the `#` from the broken line and run it.
   Count the black checkpoint lines in the output.
   **You'll know it worked when** you can identify which checkpoint was last and explain why Checkpoint 4 never appeared.

4. In Lab 1, rename `total` to `final_total` in the calculation but leave `print("Total:", total)` unchanged.
   **You'll know it worked when** a red `NameError` for `total` appears after the first three black lines.

!!! mascot-celebration "You Can Read Error Messages!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Black means success, red means "look here." You now know how to read both — and how to use print checkpoints to hunt down a bug. That's real debugging skill! Let's code it together!
