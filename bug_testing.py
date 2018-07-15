"""
Executable program to test functionality of the other programs.
"""

"""
Import necessary packages, classes, and variables.
"""

from random import shuffle

from card import Card
from supply_pile import Supply_Pile
from hand import Hand
from clock import Clock

from card_list import *

"""
Bug-testing.
"""

if __name__ == '__main__':

    prehistory = Supply_Pile(age=1, cards=age_1_cards)
    classical = Supply_Pile(age=2, cards = age_2_cards)

    prehistory.shuffle()
    classical.shuffle()

    hand_0 = Hand(num=0)

    clock = Clock(supply_piles = [prehistory, classical])

    print(clock)

    prehistory.draw(hand_0, 5)

    print(clock)

    '''b = Board()

    d_p = []

    from string import ascii_lowercase
    names = list(ascii_lowercase)

    for i in range(5):
        deck = Deck(i, [Card(names[colors.index(color)], i, color) for color in colors])
        d_p.append(deck)

    coll = Collection(d_p)

    hand = Deck()

    coll.draw(1, hand, 5)

    hand.re_turn(coll, 'b') # Working on this

    print(hand)'''