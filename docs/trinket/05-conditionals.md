## Conditionals

In this example program we will make the turtle draw
different sides of the square using different colors.

There are two things we do with equations in Python.  The first is to use the equal sign to **assign values** on the left side of the equal sign to the values on the right side.  The second thing we do is to **compare** values to the left and right of an operator.  The result of a comparison is always TRUE or FALSE.

Here is the basic syntax of the Python conditional operator.

```py
if (i > 2):
   # do something if i is greater than 2
   else:
   # do something else when i is exactly 2 or less than 2
```

## Simple Conditionals
Here is a program that 

```py
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 100
angle = 90

for i in range(1, 5):
   # i modulo 2 is the remainer after we divide by 2
   dan.write(i, font=("arial", 16, "normal"))
   if i > 2: # true if i greater than 2
      dan.color('red')
      dan.pensize(5)
   else: # if i is exactly 2 or less than 2
      dan.color('blue')
      dan.pensize(3)
   dan.forward(distance)
   dan.right(angle)
```

[Link to Trinket with Simple Conditional](https://trinket.io/python/db5978a312)

## Changing Odd and Even Edge Colors
We would like every other side to change color.  To do this we will add an if-then-else block of code to our example program.  This block of code is called a conditional block.  The condition is an expression that evaluates to be either TRUE for FALSE.  In our example we will test to see if the index of our loop (the letter "i") is ODD or EVEN.  We can do this by looking at the remainder after we divide by 2.  Python has a handy operator called the modulo operator that uses the percent character which is above the number five on your keyboard.  The test for ODD or EVEN is this:

```py
i % 2
```

In our previous loop lesson, we created an index that started at 1 and then changed to 2, 3 and finally 4.  For 1 and 3, the first and third edges the result of divid by 2 will return 1 which is the same as TRUE.  For 2 and 4 (the vertical sides of the square), the expression will evaluate to 0 since the remainder of 2/2 and 4/2 is zero. 

```py
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 50
angle = 90

# repeat the forward/right functions four times
for i in range(4):
   if i % 2:  # This is equivalent to if (i % 2) == 0: (true for odd numbers)
      dan.color('red')
   else: # if i is even
      dan.color('blue')
   dan.forward(distance)
   dan.right(angle)
   
dan.write('done with square')
```

[Conditinal Sqare](https://trinket.io/library/trinkets/5b18dc55c6)

Can you make the turtle use a larger pen size?  Try dan.pensize(10) for the red and dan.pensize(3) for the blue.

## Experiments
Can you change the width of the pen with the dan.penwidth(20) function?
