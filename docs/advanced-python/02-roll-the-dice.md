# Roll the Dice
In this game the program generates two random numbers between 1 and 6.  The program then asks the user if they want to roll the dice again.  If they answer y or yes then the pair of
dice are rolled again.

```py
import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice.  The values are:")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Roll the dices again?")
```

```sh
Rolling the dice.  The values are:
4
4
Roll the dices again?
```