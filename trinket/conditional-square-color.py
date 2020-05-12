import turtle
dan = turtle.Turtle()
dan.shape('turtle')

# penup, forward, right, left, backward, color
# is modulo for remainder
for i in range(1,5):
   if i % 2:
        dan.color('red')
   else:
        dan.color('blue')
   dan.forward(40)
   dan.right(90)
   
dan.write('done')