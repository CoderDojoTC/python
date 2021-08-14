# Reading Images in Python

Opening and displaying images in Python is pretty straightforward. It's a bit different than opening text files though. To open an image, let's use Python's built-in pil library.

```python
from PIL import Image
my_image = Image.open("/path/to/image.jpg")
my_image.show()
```

The CoderDojo AI Racing League will explore more around working with image data.