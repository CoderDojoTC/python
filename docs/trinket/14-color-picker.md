## Color Picker

You are not limited to the colors by name [Trinket Colors](https://trinket.io/docs/colors).
You can use Hex and RGB values and let your imagination run wild.

[Color Picker](https://projects.raspberrypi.org/en/projects/colourful-creations/1)

#Example code
```py

import turtle

#turtle.setup(400,500)
wn = turtle.Screen()
wn.setup(400,500)
#turtle.title("Tess becomes a traffic light!")
wn.bgcolor("A7E30E")
tess = turtle.Turtle()
tess.color('#FA057F')
style = ('Arial', 40, 'bold')
tess.write('Hello', font=style, align='Center')
tess.hideturtle()

```

## Experiments
Can you try different colors? 
Can you change font properties in style object?

The font name can as 'Arial', 'Courier', or 'Times New Roman'
The font size in pixels.
The font type, which can be 'normal', 'bold', or 'italic'