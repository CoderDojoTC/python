# Trinket Account

Before you begin, we would like you to go to the [Trinket web site](https://trinket.io/) and create your own account.  This will allow you to save your programs and come back later and continue working on them.

Here is the link to the Trinket web site:

  [https://trinket.io/](https://trinket.io/)

Be sure to bookmark this site for future reference.

## What is the turtle graphics library?
Turtle graphs have been around for almost [50 years](https://en.wikipedia.org/wiki/Turtle_graphics).  A turtle is a drawing object that has position, direction, and a pen to draw as it moves around a grid.  Turtle graphics are the preferred way to teach many concepts in computer science because they give you fast feedback.  Fast feedback allows you to quickly see the errors in your code and correct them.

For many of our introductory python labs, we will use the turtle python library.  Although there are many different versions of the turtle library, most of the commands are similar.  What you learn with the trinket python system will be useful in other systems also.

## Initialization commands
There are three lines that will appear at the top of these labs:

```python
import turtle
t = turtle.Turtle()
t.shape('turtle')
```
The first line loads the turtle library into our program.  The second creates a new turtle object called "t".  The third line sets the shape to be a turtle.  You don't have to use the name "t".  You can set your turtle's name to be whatever you want.  For example you can call your turtle "sue".  

```python
import turtle
sue = turtle.Turtle()
sue.shape('turtle')
```
Just make sure you change all the names in the file to reference your new name.

## Moving the Turtle
There are five ways to move your turtle around the screen.  Our screen is around 400 points wide and 400 points high.  The point (0,0) is at the center of our screen.  The first four are relative movement commands.  The last one will move the turtle to the absolute x and y location.

- t.forward(40)
- t.back(40)
- t.left(90)
- t.right(90)
- t.goto(x,y)

## Drawing
There are several ways to draw virtual "ink" on the screen.  The most common way is to just move your turtle around.  It will draw a thin black line by default, but you can also change the pen color and the width of drawing.

- t.penup() - no drawing will happen when the pen is up
- t.pendown() - drawing will occur on the screen when the turtle moves
- t.color('red') - set the pen to a specific color
- t.pensize(5) - set the width of the pen from 1 to 20.  5 is a good size.
- t.begin_fill() - begin filling a region you draw around
- t.end_fill() - end the fill region

## Shapes
There are also a few built-in drawing functions.  The circle function that takes a single radius is an example of this.
- t.circle(10)

## Misc
There are also a few other miscellaneous things you can do.  You can do some drawing and then clear the screen.

- t.clear() - clears the screen of all drawing
- t.hideturtle() - hides the turtle on the screen

You can see a full list of the turtle commands [here](https://trinket.io/docs/python).  Just click on the turtle area and scroll down.

## Generating a random number
In addition to these drawing commands some of the exercises use random numbers.  Here is how we do this:

```python
import random
# get a random number between -200 and 200
myNumber = random.randint(-200, 200)
```
This will generate a random number from -200 to 200.  You can use this number to randomly place items on the drawing canvas.

Now, let's get started doing some fun drawing!