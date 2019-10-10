"""
This is the first example. Dice rolling example. I know how much you love random numbers boys. Today you'll see how to
do random numbers in python. This example will be how to roll a dice.

Created by alex
"""
# Most of the things for random numbers in python will be imported from the 'random' package
import random


def roll(min_num, max_num):
    """
    This function rolls a random number between the parameters min and max.

    :param min_num: int minimum number to roll
    :param max_num: int maximum number to roll

    :return rolled: int rolled number
    """
    rolled = random.randint(min_num, max_num)
    return rolled


while input() == "roll":
    number = roll(1, 6)
    print(number)

"""
Here I have created a function called roll. It takes two parameters explained in the function. There is a loop that runs
until you input anything other than roll. Shown in this small program is random integers, wile loops, print statements,
and simple functions that return a value.

Here's the challenge.

Extend this idea of rolling a random number into a dice game. Roll two dice and the highest number wins.
Extra credit:
add a money tracker to see who wins the gamble.
"""
