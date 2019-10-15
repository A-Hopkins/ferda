"""
This is the first example. Dice rolling example. I know how much you love random numbers boys. Today you'll see how to
do random numbers in python. This example will be how to roll a dice.

Created by alex
modified by Chace
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



while input() == "start game":
        print("Welcome to my Dice Game\n First player to 100 wins")
        hpoints = 0;
        pone = 0;
        ptwo = 0;

        while hpoints <= 100:
                dice1 = roll(1, 6)
                print("Player ONE Rolled a ")
                print(dice1)
                print("\n")
                pone = pone + dice1
                if(pone > hpoints):
                    hpoints = pone
                print (pone)
                if(hpoints >= 100):
                    break
                dice2 = roll(1,6)
                print("Player TWO Rolled a ")
                print(dice2)
                ptwo = ptwo + dice2
                if(ptwo > hpoints):
                    hpoints = ptwo
                print(ptwo)

        print("\nThe game is over \n")
        if (pone > ptwo):
            print("Player ONE Won")
        else:
            print("Player TWO One")

"""number = roll(1, 6)
    print(number)"""

"""
Here I have created a function called roll. It takes two parameters explained in the function. There is a loop that runs
until you input anything other than roll. Shown in this small program is random integers, wile loops, print statements,
and simple functions that return a value.

Here's the challenge.

Extend this idea of rolling a random number into a dice game. Roll two dice and the highest number wins.
Extra credit:
add a money tracker to see who wins the gamble.
"""
