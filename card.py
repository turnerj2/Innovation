"""
Defines a class for all cards in the game.
"""

"""
Import necessary packages.
"""

"""
Defines the Card class.
"""


class Card:
    """
    Class to represent cards.
    """

    def __init__(self, name='', age=0, color='', dogma=None,
                 left=None, right=None, up=None):
        """
        Cards have a name, age, color, dogma,
        left-splay icons, right-splay icons, and up-splay icons.
        """

        self.name = name
        self.age = age
        self.color = color
        self.dogma = dogma if dogma is not None else None
        self.left = left if left is not None else []
        self.right = right if right is not None else []
        self.up = up if up is not None else []

    def __str__(self):
        """
        Prints [name, age, color]\n[left, right, up].
        """

        str_1 = "[{}, {}, {}]".format(self.name, self.age,
                                      self.color.title())
        str_2 = "[{}, {}, {}]".format(self.left, self.right, self.up)
        return (str_1 + '\n' + str_2)

    def meld(self, player):
        """
        Melds a card onto a player's board.
        """

        color = self.color
        if color == 'red':
            player.board.red.cards.insert(0, self)
        elif color == 'yellow':
            player.board.yellow.cards.insert(0, self)
        elif color == 'green':
            player.board.green.cards.insert(0, self)
        elif color == 'blue':
            player.board.blue.cards.insert(0, self)
        elif color == 'purple':
            player.board.purple.cards.insert(0, self)

        player.board.update_icons()

        str_1 = "Player {} has melded {}.\n".format(player.num, self.name)

        print(str_1)

    def score_card(self, player):
        """
        Adds a score to a given player.
        """

        player.score_pile.score_dict.setdefault(self.age, []).append(self)
        player.score_pile.score += self.age
        player.score += self.age
