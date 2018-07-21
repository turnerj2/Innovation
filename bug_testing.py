"""
Executable program to test functionality of the other programs.
"""

"""
Import necessary packages, classes, and variables.
"""

from random import shuffle
from collections import Counter

from card import Card
from supply_pile import Supply_Pile
from hand import Hand
from clock import Clock
from color_pile import Color_Pile
from board import Board
from player import Player

from card_list import *

"""
Bug-testing.
"""

if __name__ == '__main__':

    prehistory = Supply_Pile(age=1, cards=age_1_cards)
    classical = Supply_Pile(age=2, cards=age_2_cards)

    prehistory.shuffle()
    # classical.shuffle()

    red_cards = []
    for card in prehistory.cards:
        if card.color == 'red':
            red_cards.append(card)

    yellow_cards = []
    for card in prehistory.cards:
        if card.color == 'yellow':
            yellow_cards.append(card)

    hand_0 = Hand(num=0)

    clock = Clock(supply_piles=[prehistory, classical])

    red_color_pile = Color_Pile(color='red',
                                 cards=red_cards, splay='')

    yellow_color_pile = Color_Pile(color='yellow',
                                cards=yellow_cards, splay='')

    board = Board(num=0, red=red_color_pile, yellow=yellow_color_pile)

    board.splay_color_pile(color='red', direction='up')

    player = Player(num=0, board=board)

    print(player)