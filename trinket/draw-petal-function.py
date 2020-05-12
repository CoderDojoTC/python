import turtle

colorList = ['red', 'orange', 'green', 'blue', 'indigo', 'violet', 'brown']

def draw_petal(turtle, color, size):
    turtle.pendown()
    turtle.color(color)
    turtle.left(80)
    turtle.forward(size*3)
    for i in range(0, 17):
       turtle.left(15)
       turtle.forward(size/2)
    turtle.forward(size)

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(50)

space = 20
tommy.penup()
# move to the upper left
tommy.goto(-50, 100)

# draw a five petal flower
for i in range(0, 5):
   draw_petal(tommy, colorList[i], space)
   tommy.forward(space)
   tommy.right(47)
