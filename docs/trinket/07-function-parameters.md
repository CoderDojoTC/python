## Function= Parameters

Now we will create a new function that draw a square with a specific color at a specific x and y point.  The function will take three inputs:
- the color
- the horizontal x position on the grid
- the vertical y position on the grid

## Sample Code
```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

size = 40

def square(myColor, x, y):
   dan.color(myColor)
   dan.penup()
   dan.goto(x, y)
   dan.pendown()
   for i in range(4):
      dan.forward(size)
      dan.right(90)
   
   
square('red', -50, -80)
square('orange', -30, -70)
square('green', 50, 20)
square('blue', 100, -90)
```
## Drawing
![](../img/four-squares.png)

[Function](https://trinket.io/python/00e2353a96)



## Experiments
Can you change the name of the function to be "petal"?