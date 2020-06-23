## Input

We can prompt the user to supply a number using the input() function.

```python
import turtle
import random
dan = turtle.Turtle()
dan.shape('turtle')

colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']

colorIndexInt = 0

while colorIndexInt > -1:
   colorIndexString = input("Enter a number from 0 to 9 to set the new color:")
   colorIndexInt = int(colorIndexString)
   dan.begin_fill()
   dan.color(colorList[colorIndexInt])
   dan.circle(20)
   dan.end_fill()

dan.write('done!')
```

# Example on Trinket
[Run Example](https://trinket.io/python/a4a951eeab)