import turtle
import time

t = turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.begin_fill()
t.color('green')
for i in range(4):
   t.forward(100)
   t.right(90)
t.end_fill()
t.begin_fill()
for i in range(3):
   t.forward(100)
   t.left(120)
t.end_fill()

turtle.getscreen()._root.mainloop()