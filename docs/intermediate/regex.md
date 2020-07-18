# Regular Expressions in Python

A regular expression is a shorthand notation for describing a search pattern.  Regular expressions are handy whenever you have one ore more strings and you want to detect if a specific patten of characters appears in that string.  Regular expressions are mostly standardized so that if you use them other developers will quickly be able to read this the patten notation and understand the function of the pattern.

Let's take a simple example.  What if you want an input to to a function to contain four digits.  The string ```\d``` matches a single digit.  Here is the python program to check to see if there are four consecutive digits in an input string:

```python
import re

# Check if the string has four digits in a 
my_input = '1234'
digits_test = re.search('\d\d\d\d', my_input)

if digits_test:
  print("We have four digits")
else:
  print("Invalid data")
```
The name of the regular expression module is just "re".  We must import this line first.  The key line has re.search() function with two parameters.  The first parameter is the regular expression and the second is the string to be tested.

[Run on Trinket.io](https://trinket.io/python3/780b1810ad)



