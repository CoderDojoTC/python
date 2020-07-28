# Introduction to Intermediate Python

# Modules
Modules are a way to store and install reusable Python code. You can create your own modules by defining a set of functions that may be useful to other developers, and packaging these functions in a specific way so the other developers can download and easily integrate your code into their projects.

To define a module, lets create a new file called ```fibo.py``` in your current directory. Lets add the following code:

```python
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

Now that we have some functions defined, how do we access them? Let's open the Python shell (or create a new file), and run/create:

```python
import fibo

fibo.fib(10)

res = fibo.fib2(10)
print(res)
```

Now we have created and called our very own Python module! We can also import specific functions instead of the whole module, like this:

```python
from fibo import fib

fib(10)
```

In further labs, we will see how you can view the contents of a given module using the dir() functionality.


* Lab heavily inspired (code credited to): [https://docs.python.org/3/tutorial/modules.html](https://docs.python.org/3/tutorial/modules.html)