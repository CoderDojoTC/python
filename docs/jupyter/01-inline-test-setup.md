## Test of Jupyter Lab Inline Setup

[Rumor this work](https://github.com/takluyver/mobilechelonian)

```python
from ipyturtle import Turtle
t = turtle.Turtle()
t.clear()
t.resetscreen()
t.color('blue')
t.pensize(5)
for i in range(8):
    t.fd(50)
    t.rt(45)
t
```