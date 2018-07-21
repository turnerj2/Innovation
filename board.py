"""
Defines a class for a player's board.
"""

"""
Import necessary packages, classes, variables.
"""

from collections import Counter

from card import Card
from color_pile import Color_Pile

"""
Defines a class Board to represent a player's board.
"""


class Board:
    """
    Class for a player's board.
    """

    def __init__(self, num=0, red=Color_Pile(color='red'),
                 yellow=Color_Pile(color='yellow'), green=Color_Pile(color='green'),
                 blue=Color_Pile(color='blue'), purple=Color_Pile(color='purple'),
                 icons_dict=None):
        """
        A board is made up of five color piles, one for each color.
        The num is to distinguish boards.
        """

        self.num = num
        self.red = red
        self.yellow = yellow
        self.green = green
        self.blue = blue
        self.purple = purple
        self.icons_dict = Counter(self.red.icons_dict) + \
            Counter(self.yellow.icons_dict) + Counter(self.green.icons_dict) + \
            Counter(self.blue.icons_dict) + Counter(self.purple.icons_dict)

    def __str__(self):
        """
        Color piles on board will be printed in ROYGBV order.
        """

        str_1 = "-------\nBoard {} has the following icons:\n".format(self.num)
        str_2 = ''
        for key in sorted(filter(None, self.icons_dict.keys())):
            str_2 += "{} : {}\n".format(str(key).title(), self.icons_dict[key])

        str_3 = "-------\n" + "Red Pile: " + str(self.red)
        str_3 += "-------\n" + "Yellow Pile: " + str(self.yellow)
        str_3 += "-------\n" + "Green Pile: " + str(self.green)
        str_3 += "-------\n" + "Blue Pile: " + str(self.blue)
        str_3 += "-------\n" + "Purple Pile: " + str(self.purple) + "-------\n"

        return (str_1 + str_2 + str_3)

    def update_icons(self):
        """
        Updates the icons provided by the color piles.
        """

        self.red.update_icons()
        self.yellow.update_icons()
        self.green.update_icons()
        self.blue.update_icons()
        self.purple.update_icons()

        self.icons_dict = Counter(self.red.icons_dict) + \
                          Counter(self.yellow.icons_dict) + Counter(self.green.icons_dict) + \
                          Counter(self.blue.icons_dict) + Counter(self.purple.icons_dict)

    def splay_color_pile(self, color='', direction=''):
        """
        Splays a specified color pile.
        """

        to_splay = color.lower()
        to_direction = direction.lower()
        if to_splay == 'red':
            self.red.splay_direction(to_direction)
        if to_splay == 'yellow':
            self.yellow.splay_direction(to_direction)
        if to_splay == 'green':
            self.green.splay_direction(to_direction)
        if to_splay == 'blue':
            self.blue.splay_direction(to_direction)
        if to_splay == 'purple':
            self.purple.splay_direction(to_direction)

        self.icons_dict = Counter(self.red.icons_dict) + \
            Counter(self.yellow.icons_dict) + Counter(self.green.icons_dict) + \
            Counter(self.blue.icons_dict) + Counter(self.purple.icons_dict)