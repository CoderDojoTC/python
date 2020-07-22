# Maps in Python

-Dictionary: _dict_ — an unordered data type consisting of key, value pairs

  Creating a dictionary

  A dictionary is demarcated by curly braces around key:value pairs that are separated by commas.

```python
  my_dict = {"dictionary" : "a book or electronic resource that lists the words of a language", "int" : "short for integer. A whole number; a number that is not a fraction", "float" : "for our purposes this means a decimal number— a number that consists of a whole number and a fractional part", "bool" : "short for boolean; a binary, True or False value"}
```

Retrieving the value of a key from a dictionary: remember a dictionary consists of key, value pairs. To get a value for a given key we reference the key:

```python
print(my_dict['integer'])
```

If we try to reference a key that does not exist in a dictionary a KeyError will be thrown.

```python 
print(my_dict['tuple'])
```

A quick way to avoid the KeyError is by using the _.get()_ method for dictionaries: 

```python
print(my_dict.get('tuple')) # this will print None because the key 'tuple' does not exist in my_dict. 

```



Another way to avoid the KeyError and determine if a key exists in a dictionary is to use the ```in``` keyword.

```python

if 'tuple' in my_dict:
  print("'tuple' is a key in my_dict")
else:
  print("'tuple' is NOT a key in my_dict")
  
if 'int' in my_dict:
  print("'int' is a key in my_dict")
else:
  print("'int' is NOT a key in my_dict")


```

Adding or updating a key / value pair to a dictionary:

```python

my_dict['str']= "short for string; a text data type in Python defined using a pair of double or single quotes around the data"

```




## You try it!

Using your knowledge of how dictionaries and conditional statements work, create a function that takes a key and a value as arguments and will either add the key/value pair and print "This key / value pair has been added to the dictionary" if the key does not exist in the dictionary, or prints "This key is already in the dictionary!" if the key already exists. Also important to keep in mind when doing this is what we just learned about variable scopes!

```
  my_dict = {"dictionary" : "a book or electronic resource that lists the words of a language", "int" : "short for integer. A whole number; a number that is not a fraction", "float" : "for our purposes this means a decimal number— a number that consists of a whole number and a fractional part", "bool" : "short for boolean; a binary, True or False value"}

  def add_to_dict(key, value):
    #Implement the function here!
  
  add_to_dict("int","an integer")
  #This should print "This key is already in the dictionary!"

  add_to_dict("tuple","an ordered, immutable list of data / objects")
  #This should add the key/value pair to the my_dict dictionary and print "This key / value pair has been added to the dictionary"

```