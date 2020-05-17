## Turtle Graphics
Turtle graphs have been around for almost [50 years](https://en.wikipedia.org/wiki/Turtle_graphics).  A turtle is a drawing object that has position, direction and a pen to draw as it moves around a grid.  They are a great way to teach students about the concepts of programming.

## Initializaton commands
There are three lines that will appear at the top of these labs:

```python
import turtle
t = turtle.Turtle()
t.shape('turtle')
```
The first line loads the turtle library into our program.  The second creates a new turtle object called "t".  The third line sets the shape to be a turtle.  You don't have to use the name "t".  You can set your turtle's name to be whatever you want.  For example you can call your turtle "sue".

```
import turtle
sue = turtle.Turtle()
t.shape('turtle')
```

## Moving the Turtle
There a five basic ways to move your turtle around the screen.  Our screen is approximatly 300 points wide and 400 points high.  The point (0,0) is at the center of our screen.  The first four are relative commands.  The last one will move the turtle to the absolute x and y location.

- t.forward(40)
- t.back(40)
- t.left(90)
- t.right(90)
- t.goto(x,y)

## Drawing
There are several ways to draw virtual "ink" on the screen.  The most common way is to just move your turtle around.  It will draw a thin black line by default.

- t.penup()
- t.pendown()
- t.color('red')
- t.pensize(5)
- t.begin_fill() - begin filling a region you draw around
- t.end_fill() - end the fill region

## Shapes
There are also a few built-in drawing functions.
-t.circle(10)

## Misc
There are also a few other miscellanious things you can do.  You can do some drawing and then clear the screen.

- t.clear()

You can see a full list of the turtle commands [here](https://trinket.io/docs/python).  Just click on the turtle area and scroll down.

In addition to these drawing commands some of the exercises use random numbers.

import random
