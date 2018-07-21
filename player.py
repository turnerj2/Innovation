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
        str_3 = "-------"
        return(str_1 + str_2 + str_3)

    def draw(self, clock):
        """
        Performs a draw action.
        """

        player = self

        red_age, yellow_age, green_age, blue_age, purple_age = 1, 1, 1, 1, 1

        if self.board.red.cards:
            red_age = self.board.red.cards[0].age
        if self.board.yellow.cards:
            yellow_age = self.board.yellow.cards[0].age
        if self.board.green.cards:
            green_age = self.board.green.cards[0].age
        if self.board.blue.cards:
            blue_age = self.board.blue.cards[0].age
        if self.board.purple.cards:
            purple_age = self.board.purple.cards[0].age

        board_age = max(red_age, yellow_age, green_age, blue_age, purple_age)

        clock.draw(player, age=board_age, n=1)

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