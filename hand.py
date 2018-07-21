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
        str_1 = ''
        str_2 = ''

        if self.cards:
            str_1 = "The contents of Player {}'s hand:\n".format(self.num)

            for card in self.cards:
                str_2 += '{}\n'.format(card.name)

        elif not self.cards:
            str_1 = "Player {} has no cards!".format(self.num)

        return (str_1 + str_2)

    def meld(self, card_name, player):
        """
        Melds a card onto a player's board.
        """

        card_dict = {}

        for card in self.cards:
            card_dict[card.name] = card

        card_dict[card_name].meld(player)

        del card_dict[card_name]

        self.cards = card_dict.values()


    def score_card(self, card_name, player):
        """
        Score a card from your hand.
        """

        card_dict = {}

        for card in self.cards:
            card_dict[card.name] = card

        card_dict[card_name].score_card(player)

        self.cards.remove(card_dict[card.name])

        str_1 = "Player {} has scored {}. Their score is now {}.\n".format(
            player.num, card_name, player.score)

        print(str_1)
