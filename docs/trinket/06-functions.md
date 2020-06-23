## Functions

Now we will create a new function that will draw each side.

## Sample Code
```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
angle = 90

def side():
   # if event then red 2, 4 etc.
   if i % 2:
      dan.color('red')
   # else if odd then draw blue 1, 3 etc.
   else:
      dan.color('blue')
   dan.forward(distance)
   dan.right(angle)
   
# repeat the forward/right functions four times
for i in range(4):
   side()
   
dan.write('done with square')
```

[Function](https://trinket.io/library/trinkets/e3a8279a76)



## Experiments
Can you change the name of the function to be "petal"?