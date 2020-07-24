# Reading and Writing Files in Python
At this point you should now have python installed on your computer and no longer be using trinket.io. We recommend [installing Anaconda](https://www.anaconda.com/products/individual) and using the Spyder integrated development environment (IDE). 

Python makes it easy to read and write text files. The general syntax for opening a file is as follows:

```file = open('/file/path/filename.txt', 'mode')```

The first argument is the path the file on your computer. If the file you're trying to open is in the same folder as your python script you can just input the filename, if not you'll need the path to file. For example, let's say you're using a Mac, your username is Bella, and you're trying to open a file called "myfile.txt" in your downloads folder. The path to that file would be: ```/Users/Bella/Downloads/myfile.txt```

Valid arguments for the mode parameter are:

* 'w': writing to a file, this will overwrite a file if it already exists.
* 'a': append to a file, you can add new lines to a file that already exists, otherwise it will create the file.
* 'r': to read a file.

### Reading Files

For our example we're going to [download](https://www.gutenberg.org/files/2701/old/moby10b.txt) Herman Melville's _Moby-Dick_ from the Gutenberg Project to read.

```python
    f = open("/Users/Bella/Downloads/moby10b.txt","r")

    ### Let's take all the lines in Moby-Dick and store them in a list!

    lines = f.readlines()

    ### Close the file

    f.close()
```

Calling the ```.readlines()``` method on a file is very useful. If we wanted to do this manually, we would iterate over the lines in the file and add them one by one to a list.

```python

    f = open("/Users/Bella/Downloads/moby10b.txt","r")

    lines = [] #define empty list

    for line in f:
        lines.append(line) #we can use the .append() method to add new items to a list!

    f.close()
```

Let's say we needed to know exactly how many times each word appears in _Moby-Dick_: how might we do that? We'd have to account for things like punctuation, captalization and newline characters ('\n'). We'd also need to get every word by itself.

```python
from string import punctuation #punctuation from the string library is a string that contains all punctuation marks
#you can run print(punctuation) to see what this looks like

punctuation_list = list(punctuation) #convert string of punctuation marks to list


f = open("/Users/Bella/Downloads/moby10b.txt", "r") #open Moby-Dick file
lines = f.readlines() #put all lines from Moby-Dick into a list
f.close() #close the file

clean_lines = [] #empty list for lines stripped of newline characters and all characters converted to lowercase

for line in lines: #go through every line in the file
    clean_line = line.strip("\n") #get rid of new-line characters
    clean_line = clean_line.lower() #convert everything to lowercase
    clean_lines.append(clean_line) #add cleaned line to clean_lines

words={} #create empty dictionary for words

for line in clean_lines: #go through every line in the file
    for mark in punctuation_list: #go through every punctuation mark 
        line=line.replace(mark,"") #use replace method to replace each possible punctuation mark with an empty string
    line_words=line.split(" ") #we're using the string split() method to separate each line by space character
    #this converts the line to a list
    #for example: "This is a sentence.".split(" ") --> ['This', 'is', 'a', 'sentence.']
    for word in line_words: #iterate over every word in the line
        if word not in words: # if we haven't seen this word yet
            words[word]=1 #add it to the words dictionary, and mark the count as 1
        else:
            words[word]+=1 #we've already seen this word, so increment the count by 1
```

The method we used above to remove punctuation characters from the lines is not the most computationally efficent. We're going to learn a better way to do this in the section on Regex expressions.

One thing we left out from the mapping section is that you can iterate over a dictionary using the .items() method. Here's what that looks like:

```python

my_dict = {1:"one",2:"two",3:"three"}

for key, value in my_dict.items():
    print(key, value)
#this prints:
#1 one
#2 two
#3 three
```

### You Try It!
If you recall, a dictionary is an unordered data structure. Use what we learned about iterating over items in a dictionary to determine what word occurs the most frequently in _Moby-Dick_!

### Writing Files

Let's say we wanted to write out _Moby-Dick_ with no capital letters. Here's how we could approach that:

```python

f = open("/Users/Bella/Downloads/moby10b.txt", "r") #open Moby-Dick file
lines = f.readlines() #put all lines from Moby-Dick into a list
f.close() #close the file

new_file = open("/Users/Bella/Documents/moby-dick_lowercase.txt", "w") #write new file to Documents folder

for line in lines:
    new_file.write(line.lower())

new_file.close()

```