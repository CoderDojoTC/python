# Change the Turtle Shape

With the turtle shape() method we can change your turtle shape to be any of the following shapes

1. arrow
2. turtle
3. circle
4. square
5. triangle
6. classic

```py
import turtle
dan = turtle.Turtle()
dan.shape('square')
```

The ```classic``` shape is a small arrow.

## Using a List of Shapes
What if we want to use a list of shapes?

```py
import turtle, time
dan = turtle.Turtle()

myList = ["square", "circle", 'triangle', 'arrow', 'classic', 'turtle']

for index in range(0, len(myList)):
  dan.shape(myList[index])
  time.sleep(1)
```

```py
import turtle, time
dan = turtle.Turtle()

myList = ["square", "circle", 'triangle', 'arrow', 'classic', 'turtle']

for myShape in myList:
  dan.shape(myShape)
  time.sleep(1)
```


##Sample program
[Sample](https://trinket.io/library/trinkets/c9924a123a)

## Experiments
Can you use the new shapes to draw a star or any other shape of your chosing