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

def code_of_laws_dogma(player, clock, share_flag=0):
    """
    You may tuck a card from your hand of the same color as any
    card on your board. If you do, you may splay that color of
    your cards left.
    """

    colors = player.board.get_colors()

    str_1 = "Player {} has the following colors on their board:\n".format(player.num)
    str_2 = "".join(["{:>6}".format(color.title()) for color in colors])
    str_2 += '\n'

    tuckable = list(filter(lambda x : x.color in colors,
                            player.hand.cards))

    if tuckable:

        str_3 = "Player {} may tuck one of the following cards from " \
                "their hand:\n".format(player.num)

        str_4 = "".join(["{}".format(card.name) for card in tuckable])
        str_4 += '\n'

        print(str_1 + str_2 + str_3 + str_4)

        str_in_1 = "Would you like to tuck a card? (y/n)\n"

        tuck = input(str_in_1)

        if tuck[0].lower() == 'y':
            tuck = True

            str_in_2 = "What card would you like to tuck? ('q' to cancel)\n"

            wait_flag = True

            while wait_flag:
                to_tuck = input(str_in_2).title()

                tuckable_names = [card.name for card in tuckable]

                if to_tuck in tuckable_names:
                    player.tuck(to_tuck)

                    tucked = list(filter(lambda x : x.name == to_tuck,
                                tuckable))[0]

                    wait_flag = False

                elif to_tuck.lower() == 'q':
                    str_exit_1 = 'The tucking has been canceled.'

                    print(str_exit_1)
                    tuck = False
                    wait_flag = False

                else:
                    str_err_1 = "{} is not tuckable, please choose a different " \
                                "card.\n The tuckable cards are:\n".format(to_tuck)

                    print(str_err_1 + str_4)

        elif tuck[0].lower() == 'n':
            tuck = False

        if tuck:

            tucked_color = tucked.color

            if tucked_color == 'red':
                print(player.board.red)
            elif tucked_color == 'yellow':
                print(player.board.yellow)
            elif tucked_color == 'green':
                print(player.board.green)
            elif tucked_color == 'blue':
                print(player.board.blue)
            elif tucked_color == 'purple':
                print(player.board.purple)

            str_in_3 = "Would you like to splay your {} " \
                       "cards left? (y/n)\n".format(tucked_color)

            splay = input(str_in_3).lower()

            if splay == 'y':
                if tucked_color == 'red':
                    player.board.red.splay_direction('left')
                elif tucked_color == 'yellow':
                    player.board.yellow.splay_direction('left')
                elif tucked_color == 'green':
                    player.board.green.splay_direction('left')
                elif tucked_color == 'blue':
                    player.board.blue.splay_direction('left')
                elif tucked_color == 'purple':
                    player.board.purple.splay_direction('left')

        if tuck:
            return(non_demand_share(player, share_flag))

    elif not tuckable:
        str_3 = "Player {} has no cards to tuck!\n".format(player.num)

        print(str_3)

def the_wheel_dogma(player, clock, share_flag=0):
    """
    Draw two 1.
    """

    clock.draw(player, age=1, n=2)
    return(non_demand_share(player, share_flag))
