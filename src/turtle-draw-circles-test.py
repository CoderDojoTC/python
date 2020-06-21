# Author: Ewan Williams
# Date: 9 04 2016

# Python Intro Turtle Graphics

# Python has a rich "library" of functions.
# We are going to use "turtle" to do some simple graphics.
import turtle
from random import randint

if __name__ == "__main__":
    # Setup our drawning surface
    turtle.setup(800,600)     # Sets up the size of the window
    turtle.Screen()           # Turns on the graphics window

    width = 50                # Create a variable called "width"

    turtle.tracer(0,0);
    turtle.pencolor("white")
    turtle.goto(0,300)
          # and make it equal to 10
                              
    # Do some turtle graphics commands
    # Notice all commands from the turtle library is prefixed by "turtle."
    for x in range(0, 1000):
        turtle.pencolor((randint(0, 255)/255.0,
                         randint(0, 255)/255.0,
                         randint(0, 255)/255.0))
        for y in range(0, 360):
            turtle.forward((x+5)/10)
            turtle.right(1)
            
    turtle.update();
    ret = input("Press enter to exit.")
    turtle.Screen().bye()     # Turn off the graphics window
 
# Library reference: http://docs.python.org/2/library/turtle.html