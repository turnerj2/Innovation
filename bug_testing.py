"""
Executable program to test functionality of the other programs.
"""

"""
Import necessary packages, classes, and variables.
"""

from random import shuffle
from collections import Counter

from dogma import Dogma
from card import Card
from supply_pile import Supply_Pile
from hand import Hand
from clock import Clock
from color_pile import Color_Pile
from board import Board
from player import Player

from card_list import *
from dogma_list import *

from game_setup import *

"""
Bug-testing.
"""

if __name__ == '__main__':

    for player in player_list:
        clock.draw(player, age=1, n=3)

    print(player_2.hand)

    player_2.meld("The Wheel")

    player_2.activate_dogma(player_list, "The Wheel", clock)

    print(player_2.hand)

    print("DONE!")