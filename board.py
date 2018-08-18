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

    def __init__(self, num=0, icons_dict=0):
        """
        A board is made up of five color piles, one for each color.
        The num is to distinguish boards.
        """

        self.num = num
        self.red = Color_Pile(color='red')
        self.yellow = Color_Pile(color='yellow')
        self.green = Color_Pile(color='green')
        self.blue = Color_Pile(color='blue')
        self.purple = Color_Pile(color='purple')
        self.icons_dict = Counter(self.red.icons_dict) + \
            Counter(self.yellow.icons_dict) + Counter(self.green.icons_dict) + \
            Counter(self.blue.icons_dict) + Counter(self.purple.icons_dict)

    def __str__(self):
        """
        Color piles on board will be printed in ROYGBV order.
        """

        str_spc = "-------\n"

        str_1 = "{}Board {} has the following icons:\n".format(str_spc, self.num)
        str_2 = ''
        for key in sorted(filter(None, self.icons_dict.keys())):
            str_2 += "{} : {}\n".format(str(key).title(), self.icons_dict[key])
        
        str_3 =  '{}Red Pile: {}'.format(str_spc, str(self.red))
        str_3 += '{}Yellow Pile: {}'.format(str_spc, str(self.yellow))
        str_3 += '{}Green Pile: {}'.format(str_spc, str(self.green))
        str_3 += '{}Blue Pile: {}'.format(str_spc, str(self.blue))
        str_3 += '{}Purple Pile: {}{}'.format(str_spc, str(self.purple), str_spc)

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

    def get_colors(self):
        """
        Checks what colors player has on the board.
        """

        colors = []
        if self.red.cards:
            colors.append('red')
        if self.yellow.cards:
            colors.append('yellow')
        if self.green.cards:
            colors.append('green')
        if self.blue.cards:
            colors.append('blue')
        if self.purple.cards:
            colors.append('purple')

        return(colors)

    def splay_color_pile(self, color='', direction=''):
        """
        Splays a specified color pile.
        """

        to_splay = color.lower()
        to_direction = direction.lower()
        
        if to_splay == 'red':
            self.red.splay_direction(to_direction)
        elif to_splay == 'yellow':
            self.yellow.splay_direction(to_direction)
        elif to_splay == 'green':
            self.green.splay_direction(to_direction)
        elif to_splay == 'blue':
            self.blue.splay_direction(to_direction)
        elif to_splay == 'purple':
            self.purple.splay_direction(to_direction)

        self.icons_dict = Counter(self.red.icons_dict) + \
            Counter(self.yellow.icons_dict) + Counter(self.green.icons_dict) + \
            Counter(self.blue.icons_dict) + Counter(self.purple.icons_dict)