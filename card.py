import inspect
import random

values = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# face = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Card:
    """
underscores in the name mean it is private and shouldnt be used but it is not
enforced in python
    """
    def __init__(self, face, suit):
        self._face = face
        self._suit = suit

        self._value = values[self._face]

    def __setattr__(self, *args):
        if inspect.stack()[1][3] == "__init__":
            object.__setattr__(self, *args)
        else:
            raise TypeError("cannot modify object")
        # the __setattr__ function makes the cards unable to be changed like
        # you would want cards to be

    def show(self):
        face = "{} of {}".format(self._face, self._suit)
        return face

    def __add__(self, other):
        return self._value + other._value

    def __eg__(self, other):
        return self._value == other._value

    def __lt__(self, other):
        return self._value < self._value

    def __gt__(self, other):
        return self._value > self._value


class Deck:
    """
The deck of cards used
    """
    def __init__(self):
        self.cards = []

    def deal(self):
        if len(self.cards) >= 0:
            return self.cards.pop(0)
        return None

    def shuffle(self):
        for face in values:
            for suit in suits:
                self.cards.append(Card(face, suit))
            random.shuffle(self.cards)

    """
could use a hand class to calculate the hand or whatever you think of

    """


# class Player:
#     """
#
#     """
#     def __init__(self):
#         pass


