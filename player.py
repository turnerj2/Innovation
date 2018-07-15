"""
Defines a class for the player.
"""

"""
Import necessary packages and classes.
"""

from board import Board
from deck import Deck

"""
Defines the player class.
"""


class Player:
    """
    Class to represent the player.
    """

    def __init__(self, num=0, board=Board(num=0), hand=Deck(num=0)):
        """
        Players will have a number, a hand, and a board.
        """

        self.num = num
        self.board = board
        self.hand = hand

    def __str__(self):
        """
        Prints the player's number, board, and hand.
        """

        print("Player {}'s board:".format(self.num))
        print(self.board)
        print("Player {}'s hand:".format(self.num))
        print(self.hand)

        return('-------')