from random import choice

places = ["McDonalds", "KFC", "Burger King", "Taco Bell",
          "Wendys", "Arbys", "Pizza Hut"]

def pick(): # see the docstring below?
    """Return random fast food place"""
    return choice(places)
