from baseEnum import BaseEnum


class Suit(BaseEnum):
    SPADE = 1
    CLUB = 2
    DIAMOND = 3
    HEART = 4
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value <= other.value
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value >= other.value