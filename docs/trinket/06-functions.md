## Functions

Now we will create a new function that will draw each side.

## Sample Code
```
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
angle = 90

def side():
   if i % 2:
      dan.color('red')
   else:
      dan.color('blue')
   dan.forward(distance)
   dan.right(angle)
   
# repeat the forward/right functions four times
for i in range(4):
   side()
   
dan.write('done with square')
```

[Function](https://trinket.io/python/00e2353a96)



## Experiments
Can you change the name of the function to be "petal"?