import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest2 as unittest
from lib.models.deck import Deck
from lib.enums.rank import Rank
from lib.enums.suit import Suit
class DeckTest(unittest.TestCase):
    def test_creation(self):
        deck = Deck()
        self.assertIsNotNone(deck.cards)
        

    def test_cards(self):
        deck = Deck()
        suit_count = {}
        rank_count = {}
        self.assertEqual(len(deck.cards), 52)
        for card in deck.cards:
            suit_count[card.suit.name] = suit_count.get(card.suit.name, 0) + 1
            rank_count[card.rank.name] = rank_count.get(card.rank.name, 0) + 1
        for rank in Rank:
            """
                There should be 4 of each Rank in a deck of cards
            """
            self.assertIsNotNone(rank_count.get(rank.name,None))
            self.assertEqual(rank_count[rank.name], 4)
        for suit in Suit:
            """
                There should be 13 of each Suit in a deck of cards
            """
            self.assertIsNotNone(suit_count.get(suit.name,None))
            self.assertEqual(suit_count[suit.name], 13)
if __name__ == '__main__':
    unittest.main()