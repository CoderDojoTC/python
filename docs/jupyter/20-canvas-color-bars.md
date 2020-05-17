## Canvas Color Bars
We can draw directly into the Jupyter Lab canvas by using the Canvas drawing component.

The following draws several horizontal bars of different color.

```python
from ipycanvas import Canvas

canvas = Canvas(width=400, height=170)

# draw a some lines of different colors and widths

canvas.translate(10,10)

canvas.fill_style = 'red';
canvas.fill_rect(0, 0, 400, 10)

canvas.fill_style = 'orange';
canvas.fill_rect(0, 25, 400, 10)

canvas.fill_style = 'yellow';
canvas.fill_rect(0, 50, 400, 10)

canvas.fill_style = 'green';
canvas.fill_rect(0, 75, 400, 10)

canvas.fill_style = 'blue';
canvas.fill_rect(0, 100, 400, 10)

canvas.fill_style = 'purple';
canvas.fill_rect(0, 125, 400, 10)

canvas.fill_style = 'pink';
canvas.fill_rect(0, 150, 400, 10)

canvas
```
# Experiments
Can you modify the above to use a list of colors and a for loop?
The color list might be:

## Using Lists
```
from ipycanvas import Canvas
canvas = Canvas(width=400, height=250)

colors =['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown',
         'cyan', 'lightgreen', 'lightblue']
canvas.font = '16px serif'

# draw some boxes of different colors

canvas.translate(10,10)
for i in range(len(colors)):
   canvas.fill_style = colors[i];
   canvas.fill_text(colors[i], 0, 25*i + 10)
   canvas.fill_rect(70, i*25, 400, 15)

canvas
```