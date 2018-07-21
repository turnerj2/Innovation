"""
Score piles to be used for a player's.
"""

"""
Imports necessary packages, classes, variables, etc.
"""

from collections import Counter

from card import Card

"""
Defines the score pile class.
"""


class Score_Pile:
    """
    A collection of cards and tallies up the score based on the age.
    """

    def __init__(self, num=0, cards=None, score_dict=None, score=0):
        """
        A score pile has a number, cards, score_dict, and score.
        """

        self.num = num
        self.cards = cards if cards is not None else []
        self.score_dict = {}
        self.score = 0
        if self.cards:
            self.score_dict = {}
            for card in self.cards:
                self.score_dict.setdefault(card.age, []).append(card)
            self.score = 0
            for key in self.score_dict.keys():
                self.score += key * len(self.score_dict[key])


    def __str__(self):
        """
        Prints the player's score, and how many cards have each score.
        """

        str_1 = "Player {} has {} points total. They have:\n".format(self.num, self.score)
        str_2 = ''
        for key in self.score_dict.keys():
            str_2 += "{} card(s) from age {}.\n".format(len(self.score_dict[key]), key)

        return(str_1 + str_2)