"""
Defines a class for all Dogmas in the game.
"""

"""
Import necessary packages.
"""

from dogma_list import *

"""
Defines the Dogma class.
"""

class Dogma:
    """
    Class to represent dogma.
    """

    def __init__(self, icon=None, demand=False, function=0):
        """
        Dogmas have an icon, may be demand, and have a function.
        """

        self.icon = icon
        self.demand = demand
        if self.demand and not function:
            self.function = default_demand_dogma
        elif not self.demand and not function:
            self.function = default_non_demand_dogma
        elif function:
            self.function = function

    def __str__(self):
        """
        Prints the icon, whether it is demand, and the docstring for the function.
        """

        if self.demand:
            demand = 'Demand'
        elif not self.demand:
            demand = 'Non-Demand'

        str_1 = "[{}, {}]".format(self.icon, demand)
        str_2 = self.function.__doc__
        return (str_1 + str_2)