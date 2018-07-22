"""
Defines a class for all cards in the game.
"""

"""
Import necessary packages, classes, variables, etc.
"""

from dogma import Dogma

"""
Defines the Card class.
"""


class Card:
    """
    Class to represent cards.
    """

    def __init__(self, name='', age=0, color='', dogma=Dogma(),
                 left=None, right=None, up=None):
        """
        Cards have a name, age, color, dogma,
        left-splay icons, right-splay icons, and up-splay icons.
        """

        self.name = name
        self.age = age
        self.color = color
        self.dogma = dogma
        self.left = left if left is not None else []
        self.right = right if right is not None else []
        self.up = up if up is not None else []

    def __str__(self):
        """
        Prints [name, age, color]\n[left, right, up].
        """

        str_1 = "[{}, {}, {}]\n".format(self.name, self.age,
                                      self.color.title())
        str_2 = "[{}, {}, {}]".format(self.left, self.right, self.up)
        return (str_1 + str_2)