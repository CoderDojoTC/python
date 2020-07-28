# The dir() function

As you know some date types and objects have their own methods. For example, a dictionary object has the ```.items()``` method. So how do you know what methods are available to you? That's where the dir function comes in! Just pass whatever data or object you want to know about as an argument. 

```python3

my_list=[1,2,3,4]

dir(my_list)

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

You can see this returns a list of methods, a lot of which begin and end with ```__```, those are special methods that we won't worry about for the purposes of this lab. But the rest of them are methods we can use on a list object. For example, ```.pop()```.

```python

my_list=[1,2,3,4]

last=my_list.pop()

print(last) #prints 4

print(my_list) #prints [1,2,3]

```

The pop() method will remove and return the last element from the list, that is if you call pop without passing in an argument, as we just did. Pop will accept one optional argument, that is index...you can pass the index of the item you want to remove from the list and return. With lists we start counting indices from 0. So in the list below 1 is at the 0th index and 6 is at the 5th index. 

```python

my_list=[1,2,3,4,5,6]

print(my_list[0]) #prints 1

print(my_list[5]) #prints 6

print(my_list.pop(2)) #prints 3

print(my_list) #prints [1,2,4,5,6]
```