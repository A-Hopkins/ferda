"""
Dice Rolling game

Created by Chace
"""
# Most of the things for random numbers in python will be imported from the 'random' package
import random

class Player:

    def __init__(self, name, diceroll):
        self.name = name
        self.diceroll = diceroll
        self.wins = 0

    def changename(self, namechange):
        self.name = namechange


def roll(min_num, max_num):

    rolled = random.randint(min_num, max_num)

    return rolled


playlist = []

print("Type start\n")

while input() == "start":
        print("Welcome to my Dice Game")
        maxbet = input("Enter your max bet\n")
        mbet = int(maxbet)
        players = input("Enter amount of players\n")
        tp = int(players)

        x = 0
        if tp == 0:
            break
        while x < tp:
            print("Enter Player " + str(x+1) + " name:\n")
            playlist.append(Player(input(), mbet))
            x += 1

        hpoints = 1
        score = 0
        player = 0
        total = 0

        while hpoints != 0:
            y = 0
            z = 0
            p = 0
            while z < tp:

                dice1 = roll(1,6)
                dice2 = roll(1,6)
                total = dice1+dice2
                print(playlist[y].name + " Rolled " + str(total))
                playlist[y].diceroll = total
                y += 1
                z += 1

                if y >= tp:
                    y = 0
            player = 0
            hs = 0

            for i in range(0, len(playlist)):
                if hs < playlist[i].diceroll:
                    hs = playlist[i].diceroll
                    player = i

            playlist[player].wins += 1
            print(playlist[player].name + " Has won Round " + str(hpoints) + " and has " + str(playlist[player].wins) + " Wins")
            hpoints += 1

            for i in range(0, len(playlist)):
                if mbet <= playlist[i].wins:
                    hpoints = mbet
                    print("\n" + playlist[player].name + " WINS")
                    print("\nThe game is over \n")
                    hpoints = 0