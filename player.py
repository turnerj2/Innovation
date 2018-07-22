"""
Defines a class for the player.
"""

"""
Import necessary packages and classes.
"""

from dogma import Dogma
from card import Card
from hand import Hand
from color_pile import Color_Pile
from board import Board
from score_pile import Score_Pile

"""
Defines the player class.
"""


class Player:
    """
    Class to represent the player.
    """

    def __init__(self, num=0, board=None, hand=None, score_pile=None):
        """
        Players will have a number, board, hand,
        scored cards, and achievements.
        """

        self.num = num
        self.board = board if board else Board(num=self.num)
        self.hand = hand if hand else Hand(num=self.num)
        self.score_pile = score_pile if score_pile else Score_Pile(num=self.num)
        self.score = self.score_pile.score if self.score_pile else 0

    def __str__(self):
        """
        Prints the player's number, board, and hand.
        """

        str_1 = "Player {} has {} point(s), and their board is:\n".format(self.num, self.score) + str(self.board)
        str_2 = "Player {}'s hand:\n".format(self.num) + str(self.hand)
        str_3 = "-------"
        return(str_1 + str_2 + str_3)

    def draw(self, clock):
        """
        Performs a draw action.
        """

        player = self

        red_age, yellow_age, green_age, blue_age, purple_age = 1, 1, 1, 1, 1

        if self.board.red.cards:
            red_age = self.board.red.cards[0].age
        if self.board.yellow.cards:
            yellow_age = self.board.yellow.cards[0].age
        if self.board.green.cards:
            green_age = self.board.green.cards[0].age
        if self.board.blue.cards:
            blue_age = self.board.blue.cards[0].age
        if self.board.purple.cards:
            purple_age = self.board.purple.cards[0].age

        board_age = max(red_age, yellow_age, green_age, blue_age, purple_age)

        clock.draw(player, age=board_age, n=1)

    def return_card(self, card_name, clock):
        """
        Returns a card to the appropriate supply pile.
        """

        supply_piles = {}

        for supply_pile in clock.supply_piles:
            supply_piles[supply_pile.age] = supply_pile

        hand_cards = {}

        for card in self.hand.cards:
            hand_cards[card.name] = card

        to_return_card = hand_cards[card_name]

        to_return_supply_pile = supply_piles[to_return_card.age]
        to_return_supply_pile.cards.append(to_return_card)

        self.hand.cards.remove(to_return_card)

        str_1 = "Returned {} to the clock.\n".format(to_return_card.name)

        print(str_1)

    def meld(self, card_name):
        """
        Melds a card from a player's hand.
        """

        card_dict = {}

        for card in self.hand.cards:
            card_dict[card.name] = card

        to_meld = card_dict[card_name]

        color = to_meld.color
        if color == 'red':
            self.board.red.cards.insert(0, to_meld)
        elif color == 'yellow':
            self.board.yellow.cards.insert(0, to_meld)
        elif color == 'green':
            self.board.green.cards.insert(0, to_meld)
        elif color == 'blue':
            self.board.blue.cards.insert(0, to_meld)
        elif color == 'purple':
            self.board.purple.cards.insert(0, to_meld)

        self.board.update_icons()

        str_1 = "Player {} has melded {}.\n".format(self.num, to_meld.name)

        print(str_1)

        del to_meld

        self.hand.cards = card_dict.values()

    def score_card(self, card_name):
        """
        Scores a card from a player's hand.
        """

        card_dict = {}

        for card in self.hand.cards:
            card_dict[card.name] = card

        to_score = card_dict[card_name]

        self.score_pile.score_dict.setdefault(to_score.age, []).append(to_score)
        self.score_pile.score += to_score.age
        self.score += to_score.age

        self.hand.cards.remove(to_score)

        str_1 = "Player {} has scored {}. Their score is now {}.\n".format(
            self.num, card_name, self.score)

        print(str_1)