# Flower using Petal Function on Repl.it

```python
import turtle
dan = turtle.Turtle()
dan.shape('turtle')

distance = 100
angle = 120

def petal():
   if i % 2:
      dan.color('green')
   else:
      dan.color('lightgreen')
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

# start off 45 right
dan.right(45)
# repeat the forward/right functions four times
for i in range(4):
   petal()
# now draw the stem
dan.pensize(10)
dan.right(45)
dan.forward(200)
```

[Sample Square Program on Repl.it](https://repl.it/@DanMcCreary/Flower)