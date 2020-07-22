## Variables
If you've made it this far, you know a variable is a container for data in Python. Let's dive a little deeper into the world of variables!

### Naming conventions
In the [Python community](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names), the general accepted format for variable and function names is all lower case, with multiple words separated by underscores. For example:

variable = 0

my_variable = 0

my_function_name()

### Giving variables and functions meaningful names
Variable names should be meaningful to you as the programmer, to any other developers that may be collaborating with you and any developers that may look at your code in the future. Below are two instances of the same code using different variable and function names. Which is easier to read?

```python
def my_first_function(arg):
  variable1 = arg + 2
  return variable1

def my_second_function(arg):
  variable = arg * 5
  return variable

print(my_first_function(my_second_function(5)))
```


```python
def plus_two(num):
  two_more = num + 2
  return two_more

def times_five(num):
  five_times = num * 5
  return five_times

print(plus_two(times_five(5)))
```

### Variable Scope
A variable's scope refers to where in your code you can access that variable. The scope of a variable defined within a function is limited to the function in which it is defined. This is an example of a local variable.  For example, using the more legible code above: 

```python
def plus_two(num):
  two_more = num + 2
  return two_more

def times_five(num):
  five_times = num * 5
  return five_times

print(plus_two(times_five(5)))

print(five_times) 
```

Attempting to print the value of five_times within the global scope of the code will result in a NameError, because the scope of the variable five_times is limited to the times_five function. Conversely, a global variable is a variable that can be accessed anywhere within your code. Global variables are usually created within the main body of your code, that is outside of functions, as demonstrated below. You can see the my_name variable is accessible within the who_is_awesome function.

```python

my_name = "Zack"
def who_is_awesome():
    print(my_name + " is awesome!")

```

You can make a variable used within a function globally accessible by using the 'global' keyword. For example,

```python
def who_is_awesome(name):
    global awesome_statement
    awesome_statement = name + " is awesome!"
    print("Variable Reference Within Function: " + awesome_statement)

who_is_awesome("Zack")
print("Global Variable Use: " + awesome_statement)
```

## Food for Thought
When would it make sense to use the global keyword within a function to make a variable globally accessible, instead of returning the variable from the function? 