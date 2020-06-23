## Python List

How would we create and access a list of colors in Python?
Here is a list of colors:

```python
colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
```
To access any color you can reference the index of the color by using a number.  For example to get the third
color you would use:

```python
colorList[2]
```

## Sample Code to Draw A Circle with a Color Index
```python
import turtle
import random
dan = turtle.Turtle()
dan.shape('turtle')

colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']

dan.begin_fill()
dan.color(colorList[3])
dan.circle(20)
dan.end_fill()
```

## Drawing
![](../img/green-circle.png)

## Run Sample Program on Trinket
[Draw a Green Circle Using List](https://trinket.io/python/6b93c1711f)

## Experiments
Can you change the name of the function to be "petal"?