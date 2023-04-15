# Installing a Local Desktop Python

The next few labs are labs that must be run on your local computer because the will interact with the local operating system and local file system.  You will not be able to use Trinket to run these programs.

The main site for Python is here:
[https://www.python.org/](https://www.python.org/)

If you go to that site there will be pages for Downloads and Documentation for each version of your desktop or PC.

The best way to get detailed instructions or hints is to do a web search for a phrase such as:

1. *"How do I install Python on my Windows 10 PC"*
2. *"How do I install Python on my Mac"*
2. *"How do I install Python on my Raspberry Pi"*

You can also give a precise version of Python and your operating system such as:

*"How to install Python 3 on MacOS Mojhave"*

These tools usually give you command line access to Python using "Terminal" or "Shell".  To use Python you will need to open a command line and type "python --version" to verify that Python is installed correctly.

Here is an example of what this looks like from a command line:

```sh
$ python --version
Python 2.7.16
```

This indicates that python 

## You System Path
The system path is a key list that holds a set of sequential places that Python looks for functions.
```sys.path``` is a list of places to look for code and it will execute the first function that it matches in this path.

```py
import sys
# The system path is a key list that holds a set of sequential places that Python
# looks for functions.
# sys.path returns a list of places to look for code and it will execute the
# first function that it matches
myPath = sys.path
for step in range(0, len(myPath)):
    print(step+1, myPath[step])
```

## Using Conda Environments
We use conda to keep all our Python projects separate.

```sh
conda create -n coderdojo python=3
conda activate coderdojo
```

## Installing Python in an Integrated Development Environment (IDE)

## Dealing with Python Environments
If you are new to Python and you run into problems getting Python running on your desktop, you are not alone!  This challenges was well captured by cartoon, XKCD:

![Python XKCD](../img/python_environment.png)

The root cause of this complexity is that there the Python community is a large sprawling mass of free-thinking developers that don't always play nicely together.  They are always improving their own libraries and releasing new versions.  They often depend on old libraries that conflict with the newer libraries on your local system.  They use Python for many different things on different operating systems and to solve different types of problems.  Some of them care deeply about compatibility with past version of Python and some of them need the latest version to be productive.

Here are a few simple rules:

1. Always be aware of the version of Python you are using.  Use the ```python --version``` tool to see this.
2. Use different "environments" for different projects tasks that may need different version of different libraries.  Be familiar with tools like ```conda``` to manage these environments.  If you do use conda, make sure to activate these environments before you start.
3. Know how to see where Python is looking for it's libraries and know how to use the ```sys.path``` function
4. Use tools such as ```pyenv``` to control what Python environment you are using.
5. Beware of using the default Python environments.  They are often out of date.