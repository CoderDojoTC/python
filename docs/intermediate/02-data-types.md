## Data Types

![Data GIF](https://media.giphy.com/media/4FQMuOKR6zQRO/giphy.gif)

So we know that data is a piece of information, but there are of course different types of data! Let's illustrate the importance of data types...

```python

three_string = "3"
three_integer = 3

print(three_string*3)

print(three_integer*3)
```

Notice the difference in the output when multiplying three_string and three_int by three. three_string * 3 returned 333, whereas three_integer * 3 returned 9. This is because the three_string variable is a string datatype. 

### What are the different data types

**Text**

  - string: _str_
    - example: ```my_string = "this is a string"```

**Numeric**

  - integer: _int_
    - example: ```my_int = 3```
  - float: _float_
    - example: ```my_float = 3.14```

  Both integers and floats can be negative. For example: ```my_negative_int = -3```

**Sequence**

  - List: _list_ — an unordered list of data / objects. 
    - example: ```my_list = [1, 2, my_float, 4, "Bananas"]```
  - Tuple: _tuple_ — an ordered and immutable list of of data / objects. Immutable means _unchangeable_, once you have defined a tuple you cannot change, remove or reorder elements— for any of these operations, use a list. 
    - example: ```my_tuple = (1, 2, my_float, 4, "Bananas")```

As you can see, elements in lists and tuples do not have to be the same data type. There are three integers, a variable and a string in both the list and tuple shown above.

**Boolean**

- Boolean: _bool_ — a binary data type that is either True or False
  - example: ```my_bool = True```


**None**

-None: _NoneType_ — ```None``` is a keyword in Python used to indicate a null value. None differs from False or an empty string (```""```). A function that does not specify a return value will always return None.

```python
def no_return():
  print("This function does not return anything.")

no_return_response=no_return()

print(no_return_response == None)
print(type(no_return_response))
```

As you can see from the code above, when we assign the result of the _no_return()_ function call to the _no_return_response_ variable, the print statement in the function is executed. However, the value of _no_return_response_ is None, since there was no return statement in the _no_return_ function.

**Mapping**

-Dictionary: _dict_ — an unordered data type consisting of key, value pairs

  Creating a dictionary

  A dictionary is demarcated by curly braces around key:value pairs that are separated by commas. Keys and values do not need to be the same data types. 

  ```python 
  my_dict = {"dictionary" : "a book or electronic resource that lists the words of a language", "int" : "short for integer. A whole number; a number that is not a fraction", "float" : "for our purposes this means a decimal number— a number that consists of a whole number and a fractional part", "bool" : "short for boolean; a binary, True or False value"}
  ```

  We'll learn more about dictionaries in the [maps section](04-maps.md)

#### Type Casting
Strings consisting of digits can easily be converted to floats or integers

```python
#ask the user to input a number
number=input("Type a number here and press 'enter' to proceed>>>")

#side note: '\n' tells python to print a newline
#side note: we can use the the type keyword to determine what datatype a variable is
print("\nthe number variable is currently the " + str(type(number)) + " data type\n")

#as you can see the number the user entered belongs to the str data type, that's because input always returns a string.

#so if we wanted to see what two times the number the user entered is how would we do it?
print(number * 2)

#that didn't do what we wanted, did it?

#let's convert the number variable to the int data type:
number_as_int = int(number)

print("\nthe number_as_int variable is currently the " + str(type(number_as_int)) + " data type")

#okay now our number is an int!

#as you know, division operation always returns a float, even if there is no remainder

my_float= 8 / 4

print("\nmy_float is " + str(my_float))


```

## You Try It!

We know what type casting is and how to convert a string to an integer. We also know that a division operation in Python will always return a float, regardless of whether or not there's a remainder. Finally, we know using the modulo operator (_%_) in place of the division operator will return only the remainder—for example, ```7 % 4``` will return 3. Using these pieces of knowledge, implement a function that will convert a float to an int, but only if there is no remainder. Complete the function definition for float_converter below! We've put some test conditions below to check your function.

```python
def float_converter(some_float):
  #if some_float has a remainder return the original float
  #else return the some_float as an int

#test our function:
expecting_float = float_converter(7/3)
expecting_int = float_converter(4/2)

test1 = expecting_float == 7/3 
test2 = expecting_int == 2 and type(expecting_int) == int
test3 = expecting_float != 2

if test1 and test2:
  print("Congrats! You've properly implemented the float_converter function!")
elif test1:
  print("It looks like you've properly returned the original float, but didn't return some_float as an integer when there's no remainder.")
elif test2 and test3:
    print("It looks like you've properly type returned some_float as an integer when there's no remainder! But you still need to return the original float when there is a remainder.")
elif test2 and not test3:
  print("It looks It looks like you may always be returning my_float as an integer regardless of whether or not there's a remainder.")
else: 
  print("It looks like you haven't properly implemented either of the requirements for float_converter.")

```

## Food for Thought
When learning about the dictionary data type, we created _my_dict_, which contained data types and their definitions. Let's say in addition to the definitions of each data type, I wanted to add part of speech and store an example of each data type. How might we do this? Hint: it involves more dictionaries!