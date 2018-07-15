"""
A list of all of the cards in the game.
"""

"""
Import necessary packages and classes.
"""

from card import Card

"""
All of the cards.
"""

code_of_laws = Card(name='Code of Laws', age=1, color='purple',
                    dogma=None, left=['leaf'], right=[None, 'crown'],
                    up=['crown', 'crown', 'leaf'])

mysticism = Card(name='Mysticism', age=1, color='purple',
                    dogma=None, left=['castle'], right=[None, 'castle'],
                    up=['castle', 'castle', 'castle'])

city_states = Card(name='City States', age=1, color='purple',
                    dogma=None, left=['castle'], right=[None, 'crown'],
                    up=['crown', 'crown', 'castle'])

writing = Card(name='Writing', age=1, color='blue',
                    dogma=None, left=['crown'], right=[None, 'bulb'],
                    up=['bulb', 'bulb', 'crown'])

tools = Card(name='Tools', age=1, color='blue',
                    dogma=None, left=['castle'], right=[None, 'bulb'],
                    up=['bulb', 'bulb', 'castle'])

pottery = Card(name='Pottery', age=1, color='blue',
                    dogma=None, left=['leaf'], right=[None, 'leaf'],
                    up=['leaf', 'leaf', 'leaf'])

sailing = Card(name='Sailing', age=1, color='green',
                    dogma=None, left=['crown'], right=['crown', 'crown'],
                    up=['crown', None, 'leaf'])

the_wheel = Card(name='The Wheel', age=1, color='green',
                    dogma=None, left=['castle'], right=[None, 'castle'],
                    up=['castle', 'castle', 'castle'])

clothing = Card(name='Clothing', age=1, color='green',
                    dogma=None, left=['leaf'], right=[None, 'crown'],
                    up=['crown', 'leaf', 'leaf'])

agriculture = Card(name='Agriculture', age=1, color='yellow',
                    dogma=None, left=['leaf'], right=[None, 'leaf'],
                    up=['leaf', 'leaf', 'leaf'])

domestication = Card(name='Domestication', age=1, color='yellow',
                    dogma=None, left=['castle'], right=['castle', 'crown'],
                    up=['crown', None, 'castle'])

masonry = Card(name='Masonry', age=1, color='yellow',
                    dogma=None, left=['castle'], right=['castle', None],
                    up=[None, 'castle', 'castle'])

metalworking = Card(name='Metalworking', age=1, color='red',
                    dogma=None, left=['castle'], right=['castle', 'castle'],
                    up=['castle', None, 'castle'])

oars = Card(name='Oars', age=1, color='red',
                    dogma=None, left=['castle'], right=['castle', 'crown'],
                    up=['crown', None, 'castle'])

archery = Card(name='Archery', age=1, color='red',
                    dogma=None, left=['castle'], right=['castle', 'bulb'],
                    up=['bulb', None, 'castle'])

age_1_cards = [code_of_laws, mysticism, city_states, writing, tools, pottery,
               sailing, the_wheel, clothing, agriculture, domestication,
               masonry, metalworking, oars, archery]

philosophy = Card(name='Philosophy', age=2, color='purple',
                    dogma=None, left=['bulb'], right=[None, 'bulb'],
                    up=['bulb', 'bulb', 'bulb'])

monotheism = Card(name='Monotheism', age=2, color='purple',
                    dogma=None, left=['castle'], right=[None, 'castle'],
                    up=['castle', 'castle', 'castle'])

calendar = Card(name='Calendar', age=2, color='blue',
                    dogma=None, left=['bulb'], right=[None, 'leaf'],
                    up=['leaf', 'leaf', 'bulb'])

mathematics = Card(name='Mathematics', age=2, color='blue',
                    dogma=None, left=['bulb'], right=[None, 'bulb'],
                    up=['bulb', 'crown', 'bulb'])

currency = Card(name='Currency', age=2, color='green',
                    dogma=None, left=['crown'], right=['leaf', 'crown'],
                    up=['crown', None, 'crown'])

mapmaking = Card(name='Mapmaking', age=2, color='green',
                    dogma=None, left=['castle'], right=[None, 'crown'],
                    up=['crown', 'crown', 'castle'])

fermenting = Card(name='Fermenting', age=2, color='yellow',
                    dogma=None, left=['castle'], right=['leaf', 'leaf'],
                    up=['leaf', None, 'castle'])

canal_building = Card(name='Canal Building', age=2, color='yellow',
                    dogma=None, left=['crown'], right=[None, 'crown'],
                    up=['crown', 'leaf', 'crown'])

road_building = Card(name='Road Building', age=2, color='red',
                    dogma=None, left=['castle'], right=['castle', 'castle'],
                    up=['castle', None, 'castle'])

construction = Card(name='Construction', age=2, color='red',
                    dogma=None, left=['castle'], right=['castle', None],
                    up=[None, 'castle', 'castle'])

age_2_cards = [philosophy, monotheism, calendar, mathematics, currency,
               mapmaking, fermenting, canal_building, road_building,
               construction]