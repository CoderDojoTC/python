import turtle
import random
# this is a list of colors
colorList = ['red', 'orange', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
dan = turtle.Turtle()
dan.shape('turtle')
dan.delay(1)
dan.clear()
dan.penup()

max_distance = 160

# draw an eight sided star
def star(x, y, size, color):
  dan.goto(x, y)
  dan.color(colorList[random.randint(0,len(colorList)-1)])
  dan.pendown()
  dan.begin_fill()
  for i in range(1,8):
     dan.forward(size)
     dan.right(150)
     dan.forward(size)
     dan.left(100)
  dan.end_fill()
  dan.right(10)
  dan.penup()
  
# draw a pattern at a random location on the screen
for i in range(5):
   x = random.randint(-max_distance, max_distance)
   y = random.randint(-max_distance, max_distance)
   size = random.randint(15, 30)
   color_index = random.randint(0,8)
   # draw a star with size and color
   star(x,y,size, color_index)

# hide so we have a nice drawing
dan.hideturtle()