# Repl Shape Function

```py
import turtle
t = turtle.Turtle()
colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']


def shape(color, x, y, dist, edges):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(color)
  t.begin_fill()
  angle = 360 / edges
  for i in range(edges):
    t.fd(dist)
    t.rt(angle)
  t.end_fill()


shape('red', -100, 100, 50, 4)
shape('green', 50, 50, 50, 6)
shape('blue', 50, -50, 40, 8)
```
