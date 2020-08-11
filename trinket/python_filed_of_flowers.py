
import turtle
import random
dan = turtle.Turtle()
dan.shape('turtle')
 

colorList = ['red', 'orange', 'yellow', 'blue', 'purple', 'pink', 'gold','green','brown', 'gray']

# draw first flower
dan.color(colorList[random.randint(0,6)])
def petal():
   distance = 30
   angle =120
   dan.left(30)
   # draw a triangle and fill in the color
   dan.begin_fill()
   dan.forward(distance)
   dan.right(angle)
   dan.forward(distance)
   dan.right(angle)
   dan.forward(distance)
   dan.end_fill()
   dan.left(angle)
# start off 45 right
dan.right(45)
# repeat the forward/right functions four times
for i in range(4):
   petal()

# draw  on the screen 25 nore flowers
for i in range(25):
   x = random.randint(-150, 150)
   y = random.randint(-150, 150)
   dan.color(colorList[random.randint(0,6)])
   dan.penup()
   dan.goto(x,y)
   dan.pendown()
# draw a new flower
   for i in range(4):
    petal()

   
dan.penup()  
dan.goto(0,0)


 