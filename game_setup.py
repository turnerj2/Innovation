"""
Sets up the game board. Default is with four players.
"""

"""
Import necessary packages.
"""

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

"""
Executed code.
"""

prehistory = Supply_Pile(age=1, cards=age_1_cards)
classical = Supply_Pile(age=2, cards=age_2_cards)

clock = Clock(supply_piles=[prehistory, classical])

board_0 = Board(num=0)
board_1 = Board(num=1)
board_2 = Board(num=2)
board_3 = Board(num=3)

player_0 = Player(num=0, board=board_0)
player_1 = Player(num=1, board=board_1)
player_2 = Player(num=2, board=board_2)
player_3 = Player(num=3, board=board_3)

player_list = (player_0, player_1, player_2, player_3)