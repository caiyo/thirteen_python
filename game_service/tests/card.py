import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest2 as unittest
from lib.enums.rank import Rank
from lib.enums.suit import Suit
from lib.models.card import Card

class CardTest(unittest.TestCase):
    def test_creation(self):
        card = Card(Suit.SPADE, Rank.THREE)
        self.assertIs(card.suit, Suit.SPADE)
        self.assertIs(card.rank, Rank.THREE)

    def test_equiv(self):
        card_1 = Card(Suit.SPADE, Rank.THREE)
        card_2 = Card(Suit.SPADE, Rank.FOUR)
        card_3 = Card(Suit.DIAMOND, Rank.FOUR)

        self.assertTrue(card_1 < card_2)
        self.assertTrue(card_3 > card_1)
        self.assertFalse(card_2 > card_3)
        self.assertTrue(card_2.rank == card_3.rank)

    def test_sort(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()