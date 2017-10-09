from baseEnum import BaseEnum


class Rank(BaseEnum):
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12
    TWO = 13
    
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