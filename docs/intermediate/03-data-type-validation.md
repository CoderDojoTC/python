# Checking Data Types of Function Parameters
In the beginning course we learned how to pass arguments to functions.  Now we learn how to make sure our functions get the data that they expect!

We saw in the data types lab we can use the type keyword to get the type of a variable (e.g. ```type(my_var)```). We can use this in combination with the _is equal to_ operator (```==```) to make sure a variable passed to a function is the right data type. 


```python

def validateType(expecting_string):
  if type(expecting_string)==str:
    print("You passed a string!")
  else:
    print("You passed something that wasn't a string!")

```

As you may recall, during the data type labs we used the input function to solicit user input. The response from input is always a string! So if we ask the user to input a number, how do we confirm the input is in fact a number before type casting int on the user input? Remember type casting int on an alphabetic string will throw an error. Let's check it out.

```python
def cast_to_int():
  user_input=input("Enter an int\n>")
  user_input_as_int=int(user_input)
  return user_input_as_int
  
some_int=cast_to_int()
print(some_int)

```

Let's try [running this on trinket.io](https://trinket.io/python/51fabe7c6c) and when asked to enter an int, let's enter a word!

As you can see we get a type error, because we're trying to convert an alphabetic string to an integer:

```python
ValueError: invalid literal for int
```

So what's the work around? Strings have some very useful methods (methods are functions that belong to objects. We'll take about objects in the advanced section), among them ```.isdigit()```! Let's see it in action!

```python
def cast_to_int():
  user_input=input("Enter an int\n>")
  if user_input.isdigit():
    user_input_as_int=int(user_input)
    return user_input_as_int
  else:
    return "You did not input an integer!"
  
some_int=cast_to_int()
print(some_int)

```

Let's say the user input was critical to the program we're building and if the user does not input an integer we want to throw an error to the user. We can use the ```assert``` keyword to achieve this. The syntax for the assert keyword is as follows: ```assert some_conditional_statement, "Error message to output."``` Let's see it in action below! 

```python
def cast_to_int():
  user_input=input("Enter an int\n>")
  assert user_input.isdigit(), "You did not input an integer!"
  user_input_as_int=int(user_input)
  return user_input_as_int
  
some_int=cast_to_int()
print(some_int)

```

## You try it!
Let's say we want to continously bug a user until they input an integer. How might we achieve this using the lesson above + what we know about while loops?