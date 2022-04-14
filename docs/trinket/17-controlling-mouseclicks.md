## Getting a handle of the mouse clicks

We can use trinkets to change the background and control mouse clicks.
Also we have access to the exact position where the mouse was clicked. That creates a lot of possibilities 
for creating different interactions with the screen. 

Code to change screen color

Code to get co-ordinates of mouse click
```py
        x=turtle.xcor()
        y=turtle.ycor()
```

Here is an example of setting the screen color. We then draw a square in the center of the screen. 
When the user clicks a circle is drawn within the circle. On next click the circle increases in diameter. When the circle touches the square, it stops increaing in size. 

If the user clicks the screen outside the square the screen is refreshed 

```py


#import packages
import turtle
import random

# global colors
col = [ 'yellow', 'green', 'blue',
       'white', 'orange', 'pink']
circlecol =   [ 'red', 'magenta', 'purple',
       'black', 'brown', 'turqouise' ]
# method to call on screen click
tina = turtle.Turtle()  
circlediameter=10
squaresize = 200

def drawCircleOnMouseClick(x, y):
    global circlecol
    global circlediameter
    print(" x={}, y={}".format(x,y)) 

    ##If mouse is clicked within square increase size, if mouse clicked outside reset screen
    if (isMouseClickWithinSquare(x,y)) :
    ## Check if diameter is same size as square
      if (circlediameter <= squaresize/2):
          print(" circlediameter={}, squaresize={}".format(circlediameter,squaresize))
    ##If yes do not increase the size else increase the size
          circlediameter += 10
##If mouse is clicked outside the square, reset the screen - draw a new square  
    else:
        screenreset()
  

    draw_circle(tina, circlediameter, getCircleColor() )

def getBgColor():
    ind = random.randint(0, 5)
    return col[ind] 

def getCircleColor():
    ind = random.randint(0, 5)
    return circlecol[ind]

def drawsquare(turtle, size, color, startx, starty):
    turtle.penup()
    turtle.goto(startx, starty)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill() 

def draw_circle(turtle, diameter, color):
    turtle.penup()
    turtle.goto(0, -diameter)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(diameter)
    turtle.end_fill() 

def screenreset():
    tina.reset()
    drawsquare(tina, squaresize, getBgColor(), -100, -100 )

def isMouseClickWithinSquare(x, y):
  return (x >= -100 and x <= 100 and y >= -100 and y <= 100)
# set screen
sc = turtle.Screen()
sc.setup(400, 400)
sc.bgcolor('skyblue')
screenreset()

##Screen can respond to mouseclick and we can tell it what action to take i.e. method to call


# call method on screen click
sc.onscreenclick(drawCircleOnMouseClick)
```

##Sample Program
[Sample](https://trinket.io/library/trinkets/0c79d0d02a)

## Experiments
1. Can you draw different shapes
2. Can you add some more colors in the arrays
3. Can you change background color of the screen
4. Can you try some other [events](https://docs.python.org/2.7/library/turtle.html#methods-of-turtlescreen-screen)