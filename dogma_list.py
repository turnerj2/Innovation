"""
A list of all Dogma functions in the game.
"""

"""
Import necessary packages and classes.
"""

"""
Define the non-demand share snippet.
"""


def non_demand_share(player, share_flag=0):
    """
    Returns if non-demand Dogma is shared.
    """

    if type(share_flag) == bool and not share_flag:  # Opponents doing Dogma will input Bool share_flag.
        share_flag = True
        str_1 = "Share flag is now {}.\n".format(share_flag)
    elif type(share_flag) == bool and share_flag:
        str_1 = "Share flag remains True.\n"
    elif type(share_flag) == int:
        str_1 = "Share flag remains False.\n"
    
    print('{}'.format(str_1))

    return (share_flag)

"""
Define default Dogma function.
"""

def default_demand_dogma(player, opponent, clock, share_flag=0):
    """
    Default Dogma, to be used when the actual Dogma has not been implemented.
    """

    str_1 = "Player {} has done the default demand dogma for player {}.".format(opponent.num, player.num)
    print(str_1)

def default_non_demand_dogma(player, clock, share_flag=0):
    """
    Default Dogma, to be used when the actual Dogma has not been implemented.
    """

    str_1 = "Player {} has done the default non-demand dogma.".format(player.num)
    print(str_1)

    return(non_demand_share(player, share_flag))

"""
All of the Dogmas.
"""

def the_wheel_dogma(player, clock, share_flag=0):
    """
    Draw two 1.
    """

    clock.draw(player, age=1, n=2)
    return(non_demand_share(player, share_flag))
