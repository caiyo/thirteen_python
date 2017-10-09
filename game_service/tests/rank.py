import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest2 as unittest
from lib.enums.rank import Rank

class RankTest(unittest.TestCase):
    def test_equiv(self):
        rank_1 = Rank.THREE
        rank_2 = Rank.FOUR
        rank_3 = Rank.FOUR
        print "TEST {0}".format(rank_1)

        self.assertTrue(rank_1 < rank_2)
        self.assertTrue(rank_2 > rank_1)
        self.assertEqual(rank_3, rank_2)

if __name__ == '__main__':
    unittest.main()