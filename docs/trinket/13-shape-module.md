## Shape Module

In this lab we will create a set of drawing function and put them together into a new file.  We will then import this file into our main.py file.

Example code to import the module in main.py
``` py
import turtle
from shape import *
dan = turtle.Turtle()
dan.shape('turtle')

draw_triangle(dan, 'red', 5, 20, 30)
  
draw_circle(dan, 'orange', 10, 0, 30)

draw_square(dan, 'orange', 15, -20, 30)
```


## Sample Codeimited t
```py
# This is a custom module we've made.  
# Modules are files full of code that you can import into your programs.
# This one teaches our turtle to draw various shapes.

import turtle

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
    
def draw_triangle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(size*3)
    turtle.left(120)
  turtle.end_fill()
  turtle.setheading(0)
    
def draw_square(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (4):
    turtle.forward(size*2)
    turtle.left(90)
  turtle.end_fill()
  turtle.setheading(0)
  
def draw_star(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(144)
  for i in range(5):
    turtle.forward(size*2)
    turtle.right(144)
    turtle.forward(size*2)
  turtle.end_fill()
  turtle.setheading(0)
```

## Sample Program
[Sample](https://trinket.io/python/890e7026e5)

## Experiments
Can you add a new shape called "flower"?