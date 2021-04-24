# Object Classes in Python

In the mid 1960s the term Object-Oriented Programming” (OOP) was coined by Alan Kay, one of the pioneers in computer science.  Alan's idea was to group data structures and the functions that manipulate that data together in a unit called an object class.  Although many Python programmers can be productive just writing simple functions, because there are many Python libraries that use objects, we think you should be familiar with these terms, even if you decide you don't want to deal with the complexities of building your own Python object classes.

Python also has features that allow you dynamically probe the structure of object classes, even if you can't find the original source code used to create the object classes.  If you can't recall how to do something with an object class these tools can provide you a quick reminder.

## The dir() function

```py
my_list=[1,2,3,4]

dir(my_list)
```

returns:
```py
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
```