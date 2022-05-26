# J.E. Tannenbaum
# Released: 11/10/2021 - Initial release
# 11/10/2021 - Cleaned up and added comments
# https://trinket.io/python/94326b4743

import turtle		      # Load the library
jet = turtle.Turtle()	# Create the turtle object and name it
jet.shape("turtle")	  # Set the shape

def drawIt(color, distance, angle):
  jet.color(color)
  jet.begin_fill()
  jet.forward(distance)
  jet.right(angle)
  jet.forward(distance)
  jet.right(angle)
  jet.forward(distance)
  jet.right(angle)
  jet.forward(distance)
  jet.end_fill()
  
# Set the distance and angle variables
distance = 40
angle = 90

colors = []
for i in range(4):
  color = input("Enter a color:")
  colors = colors + [color]

for color in colors:
  drawIt(color, distance, angle)

# We are done, so hide the turtle
jet.hideturtle()

