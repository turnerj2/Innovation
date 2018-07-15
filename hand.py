"""
Defines a class for each player's hand.
"""

"""
Import necessary packages.
"""

"""
Defines the Hand class.
"""


class Hand:
    """
    Class to represent players' hands.
    """

    def __init__(self, num=0, cards=None):
        """
        Hand belongs to player num and contains cards.
        """

        self.num = num
        self.cards = cards if cards is not None else []

    def __str__(self):
        """
        Prints the name of the cards in the hand.
        """

        str_1 = "The contents of Player {}'s hand:".format(self.num)
        str_2 = ''
        for card in self.cards:
            str_2 += '{}\n'.format(card.name)
        return (str_1 + '\n' + str_2)
