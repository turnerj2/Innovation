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

    clock = Clock(supply_piles=[prehistory, classical])

    player_0 = Player(num=0)
    player_1 = Player(num=1)

    clock.draw(player_0, age=1, n=2)
    clock.draw(player_1, age=1, n=2)

    player_0.draw(clock)

    print(player_0.hand)

    player_0.return_card('Code of Laws', clock)

    print(player_0)

    print("DONE!")