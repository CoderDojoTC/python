# Regular Expressions in Python

A regular expression is a shorthand notation for describing a search pattern.  Regular expressions are handy whenever you have one ore more strings and you want to detect if a specific patten of characters appears in that string.  Regular expressions are mostly standardized so that if you use them other developers will quickly be able to read this the patten notation and understand the function of the pattern.

## Finding four digits in an input string
Let's take a simple example.  What if you want an input to to a function to contain four digits.  The string ```\d``` matches a single digit.  Here is the python program to check to see if there are four consecutive digits in an input string:

```python
import re
my_input = '1234'

# check to see if there are four consecutive digits somewhere in the input
digits_test = re.search('\d\d\d\d', my_input)

if digits_test:
  print("We have four digits!")
else:
  print("Invalid data")
```

[Run the regex-01 program on Trinket.io](https://trinket.io/python3/780b1810ad)

If you run the program as-is, it will tell you that the string **'1234'** will pass the test and the string **We have four digits**, but if you change the my_input to be **123x** then the **Invalid data** will be returned.

The name of the regular expression module is just "re".  We must have an import this line with the "re" module at the start of our program.  The key line has **re.search()** function with two parameters.  The first parameter is the regular expression and the second is the string to be tested.

The exact way to read this line is:

   check to see if there are four consecutive digits somewhere in the input

Note that if you put letters or spaces before or after the four digits the test will still pass.

## Finding exactly four digits
What if you wanted **exactly** four digits? For example say you have a phone system that has exactly four-digit extensions. To do this you would need to also specify two additional characters: the start expression **"^"** and the end character **"$"**.

Here is what that program would look like:

```python
import re
my_input = '1234'

# check to for exactly four digits
digits_test = re.search('^\d\d\d\d$', my_input)

if digits_test:
  print("We have exactly four digits!")
else:
  print("Invalid data")
```

[Run the regex-02 program on Trinket.io](https://trinket.io/library/trinkets/ef0666e0d3)

## Checking for one or more digits
Sometimes we don't know exactly how many digits an input field should contain.  We might just want to say "look for one or more digits".  We can do this by using the **'+'** expression which says "look for one or more of the previous expression".  Here is a program that will check for one or more digits:

```python
import re
my_input = '1'

# check for one or more digits
digits_test = re.search('^\d+', my_input)

if digits_test:
  print("We have one or more digits!")
else:
  print("Invalid data")
```

## Common regular expression characters for validating inputs
Now that you have seen several examples of regular expressions, lets list some of the most common ones we use to validate input data.:

|Expression|Meaning|Example|
|---|---|---|
|\d|A single digit in the range 0 to 9|**'\d\d\d'** for validating **'123'**| 
|^|The start of a string|**'^hello'**|
|$|The end of a string|**'hello'$**|
|[a-z]|Any lowercase character in the range of **'a'** to **'z'**|**'[a-z]\d\d'** will match **'x12'**|
|[A-Z]|Any uppercase character in the range **'A'** to **'Z'**|**'\d\d[A-Z]** will match **'47N'**|
|**.**|Zero or more occurrences of the previous expression|**'\d.'** would match an empty string, '1' or '12'|
|**+**|One or more occurrences of the previous expression|**'\d+'** would match '1' or '12' but would not match an empty string|
|**|**|Or|**'a|b|c\d'** will match **'a1'** or **'ab2'**|
|**\w**|Characters that typically make up words. This includes upper and lowercase charcters [a-z], [A-Z] and digits as well as the underscore|**\w** would match **'hello_world123'**|

Note that there is an important difference between using the "dot" (period) and the "plus" characters.  We use the dot when we want to check for an optional integer.  We use the plus sign when we require an integer.  When we are gathering information from users in a form, we often must be careful to specify what fields should require an integer input for the field to be valid.


## Combining Regular Expressions: Checking E-mail Address

We can combine regular expressions to make more complicated expressions.  For example here are some rules that form a simple e-mail address:

1. a string of word characters
2. the ampersand character **'@'**
3. a string of additional word characters
4. the period character **'.'**
5. some additional characters such as 'com', 'edu'

Here is a regular expression that does this:

```python
re.search('^\w+@\w+\.\w+$', my_input)
```

Recall that the \w+ character looks for one or more word characters.
Note that we had to use a backslash in from of the period so it takes it as a literal period and not as a regular expression for zero-or-more of prior expression.

Here is a program that prompts the user to input a valid e-mail:

```python
import re
my_input = 'a@myco.com'

# check for one or more digits
if re.search('^\w+@\w+\.\w+$', my_input):
  print("E-mail address valid")
else:
  print("Error: Invalid email address!")
```

## Finding The Right Regular Expression

You often are confronted with validating complex fields like phone numbers, zip codes, and postal addresses.  The good news is that many other people have also needed to do this and with a bit of searching you can probably find a regular expression that meets your needs.  One of the best places to look for regular expressions is [RegExLib](ttps://www.regexlib.com/).  You can not only search for a regular expression but you can test it on common patterns.  Other users have also voted on which regular expressions are their favorites.  There are also categories of regular expressions such as:

1. E-mails
2. Dates and times
3. Strings
4. Numbers
5. URI
6. Addresses/Phone
7. Markup
8. Miscellaneous

## From Search to 

The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string


## Python Regular Expression References

[Python RegEx Cheat Sheet](https://www.debuggex.com/cheatsheet/regex/python)
[Python Regular Expressions HOWTO](https://docs.python.org/3/howto/regex.html#regex-howto)

