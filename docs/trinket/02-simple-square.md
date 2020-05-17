## Drawing a Square
The following code is an example of drawing a square using turtle graphics.  In this example the turtle moves foward 100 units and then turns right.  The angle for the right turn is 90 degrees.  It repeats these two functions four times to make a square.

## Sample Code
```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)

dan.forward(100)
dan.right(90)
```
## Drawing
![](../img/simple-square.png)

## Explaination
The first three lines will be the same for all our programs.  They import the turtle library into our program, create a new turtle object and then assign the turtle a shape icon.

Note that at the start, the turtle is facing to the right.  After the last instruction, it is also facing to the right.

## Experiments
Can you change the distance and angle the turtle moves?  What happens when you change the numbers for the forward and right functions?  Can you go left as well as right?

Can you add more motion commands using copy and paste?