import turtle

colorList = ['red', 'orange', 'green', 'blue', 'indigo', 'violet', 'brown']

def draw_branch(turtle, color, size, level):
  if level > 1:
    turtle.pendown()
    turtle.color(color)
    turtle.forward(size)
    turtle.right(20)
    # draw three branches at half length with a branch on the tip of each branch 
    for i in range(0, 3):
       turtle.forward(size/2)
       draw_branch(turtle, colorList[i], size/2, level - 1)
       turtle.backward(size/2)
       turtle.left(20)
    turtle.right(40)
    turtle.backward(size)
    
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(50)

length = 150
numberPetals = 6
myTurtle.penup()
# move to the bottom center
myTurtle.goto(0, -200)
myTurtle.left(90)

draw_branch(myTurtle, colorList[0], length, 4)
