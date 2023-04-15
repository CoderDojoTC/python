# Python Turtle Graphics Stop Sign

![](../img/stop-sign.png)

In this lesson, we will use variables and for loop to draw a stop sign.
We will also show how to use the penup, pendown, color, begin_fill, end_fill and write functions.
Our write function will also change the font size using the ```font=("Arial", 30, "normal")``` parameter.

## Sample Code

```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
sides = 8
# The angle we turn is related to the number of sides by this formula
angle = 360 / sides
my_color = "red"

dan.penup()
dan.goto(-50, 100)
dan.pendown()
dan.color(my_color)
dan.begin_fill()
# repeat the forward/right functions for each side
for i in range(sides):
   dan.forward(distance)
   dan.right(angle)

dan.end_fill()
dan.hideturtle()

dan.penup()
dan.right(110)
dan.forward(80)
dan.color('white')
dan.write('STOP', font=("Arial", 30, "normal"))
```

## Link to Trinket

[Draw a Stop Sign on Trinket](https://trinket.io/python/7f9eee8b80)