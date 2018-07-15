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

        return (str_1 + str_2)
