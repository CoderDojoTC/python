## Flower

Now we will create a new function that will draw a triangle for
each side.  It will do this by going forward and right three times
at an angle of 120 degrees.

## Sample Code
```
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 100
angle = 120

def petal():
   if i % 2:
      dan.color('red')
   else:
      dan.color('blue')
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
   
   
# repeat the forward/right functions four times
for i in range(4):
   petal()
   
dan.write('done with flower')
```

[Function](https://trinket.io/python/00e2353a96)



## Experiments
Can you change the name of the function to be "petal"?