import random
from card import Card
from lib.enums.rank import Rank
from lib.enums.suit import Suit
class Deck(object):
    def __init__(self):
        self.cards = self._create_cards()
        self.shuffle()

    def _create_cards(self):
        cards = []
        for rank in Rank:
            for suit in Suit:
                cards.append(Card(suit, rank))
        return cards

    def shuffle(self):
        random.shuffle(self.cards)