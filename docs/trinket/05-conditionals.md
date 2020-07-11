## Conditionals

In this example program we will make the turtle draw
different sides of the square using different colors.

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
   if i % 2:
      dan.color('red')
   else:
      dan.color('blue')
   dan.forward(distance)
   dan.right(angle)
   
dan.write('done with square')
```

[Conditinal Sqare](https://trinket.io/library/trinkets/5b18dc55c6)

Can you make the turtle use a larger pen size?  Try dan.pensize(10) for the red and dan.pensize(3) for the blue.

## Experiments
Can you change the width of the pen with the dan.penwidth(20) function?
