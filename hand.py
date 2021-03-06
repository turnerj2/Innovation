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

    def __init__(self, num=0, cards=0):
        """
        Hand belongs to player num and contains cards.
        """

        self.num = num
        self.cards = cards if cards else []

    def __str__(self):
        """
        Prints the name of the cards in the hand.
        """
        str_1 = ''
        str_2 = ''

        if self.cards:
            str_1 = "The contents of Player {}'s hand:\n".format(self.num)

            for card in self.cards:
                str_2 += '{}\n'.format(card.name)

        elif not self.cards:
            str_1 = "Player {} has no cards!".format(self.num)

        return (str_1 + str_2)