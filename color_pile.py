"""
Colors piles to be used on a player's board.
"""

"""
Imports necessary packages, classes, variables, etc.
"""

from collections import Counter

from card import Card

"""
Defines the color pile class.
"""


class Color_Pile:
    """
    A collection of cards of a single color, and tallies up the icons based on the splay.
    """

    def __init__(self, color='', cards=None, splay='', icons_dict=None):
        """
        A color pile has a color, cards, splay, and number of icons.
        """

        self.color = color
        self.cards = cards if cards is not None else []
        self.splay = splay

        top_card = self.cards[0] if cards else None
        if top_card:
            top_icons = top_card.up[:]
            top_icons.append(top_card.right[0])

            if not splay:
                self.icons_dict = Counter(top_icons)

            elif splay == 'left':
                icons = top_icons[:]
                for card in self.cards:
                    icons.extend(card.left)
                    self.icons_dict = Counter(icons)

            elif splay == 'right':
                icons = top_icons[:]
                for card in self.cards:
                    icons.extend(card.right)
                    self.icons_dict = Counter(icons)

            elif splay == 'up':
                icons = top_icons[:]
                for card in self.cards:
                    icons.extend(card.up)
                    self.icons_dict = Counter(icons)

        elif not top_card:
            self.icons_dict = {} if not icons_dict else icons_dict

    def __str__(self):
        """
        Prints the color of the pile, number of cards, top card, splay, and icons.
        """


        if not self.splay:
            str_1 = "The {} color pile contains {} cards " \
                    "and is not splayed.\n".format(
                self.color, len(self.cards), self.splay if self.splay else 'not')
        elif self.cards and self.splay:
            str_1 = "The {} color pile contains {} card(s) " \
                    "and is splayed {}.\n".format(
                self.color, len(self.cards), self.splay)

        str_2 = ''
        str_3 = ''

        if self.cards:
            str_2 = "The top card is {}, and the pile provides " \
                "the following icons:\n".format(self.cards[0].name)
            for key in sorted(filter(None, self.icons_dict.keys())):
                str_3 += "{} : {}\n".format(str(key).title(), self.icons_dict[key])

        return (str_1 + str_2 + str_3)

    def update_icons(self):
        """
        Updates icons provided by the pile.
        """

        direction = self.splay

        if self.cards:
            top_card = self.cards[0]
            top_icons = top_card.up[:]
            top_icons.append(top_card.right[0])

            if not direction:
                self.icons_dict = Counter(top_icons)

            elif direction == 'left':
                icons = top_icons[:]
                for card in self.cards:
                    icons.extend(card.left)
                    self.icons_dict = Counter(icons)

            elif direction == 'right':
                icons = top_icons[:]
                for card in self.cards:
                    icons.extend(card.right)
                    self.icons_dict = Counter(icons)

            elif direction == 'up':
                icons = top_icons[:]
                for card in self.cards:
                    icons.extend(card.up)
                    self.icons_dict = Counter(icons)

        elif not self.cards:
            self.icons_dict = {}

    def splay_direction(self, direction=''):
        """
        Splays the color pile so that it has no splay, or is splayed left, right, or up.
        """

        self.splay = direction

        self.update_icons()