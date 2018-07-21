"""
Defines a class to represent the supply piles.
"""

"""
Import necessary packages.
"""

from random import shuffle

"""
Defines the Supply_Pile class.
"""


class Supply_Pile:
    """
    Class to represent a deck of cards.
    """

    def __init__(self, age=0, cards=None):
        """
        Each supply pile has an age and a list of cards which are in it.
        """

        self.age = age
        self.cards = cards if cards is not None else []

    def __str__(self):
        """
        Cards in supply pile will be printed in order.
        """

        str_1 = "The contents of the age {} supply pile are:\n".format(self.age)

        card_names = ''
        for card in self.cards:
            card_names += card.name + '\n'

        return(str_1 + card_names)

    def shuffle(self):
        """
        Shuffles the cards in the deck.
        """

        cards = self.cards[:]
        shuffle(cards)
        self.cards = cards

    def draw(self, player, n):
        """
        Draw n cards from the supply pile and add them to hand.
        """

        deck_cards = self.cards[:]
        hand_cards = player.hand.cards[:]

        for i in range(n):
            drawn_card = deck_cards[0]
            del deck_cards[0]
            hand_cards.append(drawn_card)
            i += 1

        self.cards = deck_cards
        player.hand.cards = hand_cards

        print("Player {} drew {} card(s) from age {}.\n".format(player.num, n, self.age))