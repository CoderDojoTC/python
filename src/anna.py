# Author: Anna Pederse
# Date: 9 April 2016
# License: CC BY-SA
# For CoderDojo WA

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle
anumber = 20
bnumber = 10

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window




    turtle.pencolor("yellow");
    
    turtle.forward(bnumber)
    turtle.right(90)
    turtle.forward(anumber)
    turtle.right(90)
    turtle.forward(bnumber)
    turtle.right(90)
    turtle.forward(anumber)

    turtle.left(90)
    turtle.pencolor("black");
    
    turtle.forward(bnumber)
    turtle.left(90)
    turtle.forward(anumber)
    turtle.left(90)
    turtle.forward(bnumber)
    turtle.left(90)
    turtle.forward(anumber)

    turtle.left(90)
    
    turtle.pencolor("yellow");
    turtle.forward(bnumber*2)
    turtle.left(90)
    turtle.forward(anumber)
    turtle.left(90)
    turtle.forward(bnumber)
    turtle.left(90)
    turtle.forward(anumber)
    
    turtle.left(90)
    turtle.pencolor("black");
    turtle.forward(bnumber*2)
    turtle.left(90)
    turtle.forward(anumber)
    turtle.left(90)
    turtle.forward(bnumber)
    turtle.left(90)
    turtle.forward(anumber)
    
   

    turtle.update(); # draws the screen

    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window

# Library reference: http://docs.python.org/2/library/turtle.html