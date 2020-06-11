## Using a Loop

In this example program we will make the turtle go forward 40 steps and then make a right turn of 90 degrees.  
We will repeat this four times to complete a square.


## Sample Code
```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
angle = 90

# repeat the forward/right functions four times
for i in range(4):
   dan.forward(distance)
   dan.right(angle)
   
dan.write('done with square')
```

## Running the Demo
[Run Square With Loop](https://trinket.io/python/6cadd3c046)

## Experiments
Can you make the turtle draw a larger square?  Hint: change the distance to be 80.  How big can you make the square before the turtle goes off the screen?
