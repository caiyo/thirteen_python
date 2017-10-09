import sys, os
sys.path.insert(0, os.path.abspath('..'))

from lib.enums.suit import Suit
import unittest2 as unittest
class SuitTest(unittest.TestCase):
    def test_equiv(self):
        suit_1 = Suit.SPADE
        suit_2 = Suit.DIAMOND
        suit_3 = Suit.DIAMOND

        self.assertTrue(suit_1 < suit_2)
        self.assertTrue(suit_2 > suit_1)
        self.assertEqual(suit_3, suit_2)

if __name__ == '__main__':
    unittest.main()