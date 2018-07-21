"""
Defines a class for the collection of supply piles.
"""

"""
Import necessary packages.
"""

"""
Defines the Clock class.
"""


class Clock:
    """
    Class for the collection of supply piles
    """

    def __init__(self, supply_piles):
        """
        A collection is a list of decks.
        """

        self.supply_piles = supply_piles

    def __str__(self):
        """
        The age and size of supply piles will be printed.
        """

        str_1 = "There are {} supply piles in play:\n".format(len(self.supply_piles))
        str_2 = ''
        for supply_pile in self.supply_piles:
            str_2 += "The age {} supply pile contains {} cards.\n".format(
                supply_pile.age, len(supply_pile.cards))

        return(str_1 + str_2)

    def draw(self, player, age, n):
        """
        Attempts to draw n cards from the age age supply pile. Will move up naturally.
        """

        supply_pile_dict = {}
        for supply_pile in self.supply_piles:
            supply_pile_dict.setdefault(supply_pile.age, supply_pile)

        if age > max(supply_pile_dict.keys()):
            print("Attempted to draw from Age 11. Game Over.")

        else:
            to_draw_supply_pile = supply_pile_dict[age]
            num_cards = len(to_draw_supply_pile.cards)
            if n > num_cards:
                to_draw_supply_pile.draw(player, num_cards)
                self.draw(player, age + 1, n - num_cards)
            elif n <= num_cards:
                to_draw_supply_pile.draw(player, n)