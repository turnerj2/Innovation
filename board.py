"""
Defines a class for a player's board.
"""

"""
Import necessary packages.
"""

from deck import Deck

"""
Defines a class Board to represent a player's board.
"""


class Board:
    """
    Class for a player's board.
    """

    def __init__(self, num=0, red=Deck(num=0), yellow=Deck(num=1),
                 green=Deck(num=2), blue=Deck(num=3), purple=Deck(num=4)):
        """
        A board is made up of five decks, one for each color. The num is to distinguish boards.
        """

        self.num = num
        self.red = red
        self.yellow = yellow
        self.green = green
        self.blue = blue
        self.purple = purple

    def __str__(self):
        """
        Decks in board will be printed in ROYGBV order.
        """

        print("-------\n" + "The piles on board {}:\n".format(self.num) + "Red Pile: ")
        print(self.red)

        print("-------\n" + "Yellow Pile: ")
        print(self.yellow)

        print("-------\n" + "Green Pile: ")
        print(self.green)

        print("-------\n" + "Blue Pile: ")
        print(self.blue)

        print("-------\n" + "Purple Pile: ")
        print(self.purple)

        return ("-------")
