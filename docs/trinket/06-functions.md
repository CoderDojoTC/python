## Functions

In this example program we will make the turtle go forward 40 steps and then make a right turn of 90 degrees.  We will repeat this four times to complete a square.

```
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
angle = 90

# repeat the forward/right functions four times
for i in range(4):
   if i % 2:
      dan.color('red')
   else:
      dan.color('blue')
   dan.forward(distance)
   dan.right(angle)
   
dan.write('done with square')
```

[Conditinal Sqare](https://trinket.io/python/00e2353a96)

Can you make the turtle use a larger pen size?  Try dan.pensize(10) for the red and dan.pensize(3) for the blue.

## Experiments
Can you change the width of the pen with the dan.penwidth(20) function?
