"""
Defines a class for the player.
"""

"""
Import necessary packages and classes.
"""

from card import Card
from hand import Hand
from color_pile import Color_Pile
from board import Board
from score_pile import Score_Pile

"""
Defines the player class.
"""


class Player:
    """
    Class to represent the player.
    """

    def __init__(self, num=0, board=None, hand=None, score_pile=None):
        """
        Players will have a number, board, hand,
        scored cards, and achievements.
        """

        self.num = num
        self.board = board if board else Board(num=self.num)
        self.hand = hand if hand else Hand(num=self.num)
        self.score_pile = score_pile if score_pile else Score_Pile(num=self.num)
        self.score = self.score_pile.score if self.score_pile else 0

    def __str__(self):
        """
        Prints the player's number, board, and hand.
        """

        str_1 = "Player {}'s board:\n".format(self.num) + str(self.board)
        str_2 = "Player {}'s hand:\n".format(self.num) + str(self.hand)
        str_3 = "\n-------"
        return(str_1 + str_2 + str_3)

    def meld(self, card_name):
        """
        Melds a card from a player's hand.
        """

        self.hand.meld(card_name, self)

    def score_card(self, card_name):
        """
        Scores a card from a player's hand.
        """

        self.hand.score_card(card_name, self)