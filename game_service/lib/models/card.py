class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} {1}".format(self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

    # Since there could only be 1 of each card, you cant have less / greater than or equal too
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return True if self.rank < other.rank else self.rank == other.rank and self.suit < other.suit

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return True if self.rank > other.rank else self.rank == other.rank and self.suit > other.suit

    def __eq__(self, other):
            return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash(str(self))