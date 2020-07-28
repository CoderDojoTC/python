# Debugging in Python

Uncaught errors in a Python script will cause it to abruptley hault. Utilizing the error output, also known as a stack trace will help us determine the root cause. The code below throws an error.

```python

import random

my_list=[] #create empty list

#get a random item from a list
def choose_random(some_list):
    return random.choice(some_list)


for i in range(1,10): #(produces 1,2,3,4,5,6,7,8,9 over the 9 iterations of the loop)
    my_list.append(i) #add the number to my_list
    if i==1: #if the number of the current iteration of the loop is 1
        my_list.pop(0) #remove the first element from the list
    random.choice(my_list) #randomly chose an element from the list

```

This code throws an error and produces the following stack trace:

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-24-593f65711788> in <module>()
      7     if i==1:
      8         my_list.pop(0)
----> 9     random.choice(my_list)

~/anaconda3/lib/python3.7/random.py in choice(self, seq)
    259             i = self._randbelow(len(seq))
    260         except ValueError:
--> 261             raise IndexError('Cannot choose from an empty sequence') from None
    262         return seq[i]
    263 

IndexError: Cannot choose from an empty sequence
```

You can see the actual error, an IndexError is being thrown in the code for the random module (line 261 in random.py). The output text is helpful, it's saying it can't choose a random item from an empty list. So why is our list empty? We now need to determine where in our code the error is occurring, if you look up line 9, that's referring to line 9 in our code. So we know that line's causing the error, so we then have to ask in what case we're passing an empty list into random.choice(). If we go through each iteration of the loop, we can see that it's on the first iteration when i==1, that we remove the first element from my_list, doing this leaves an empty list and passing it into random.choice() causes the error. 

The first step in debugging should always be to read the stack trace, if the source of the error is not self-evident, StackOverflow and Google are your next best bet. 