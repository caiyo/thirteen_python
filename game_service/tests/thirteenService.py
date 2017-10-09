import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest2 as unittest
from lib.models.card import Card
from lib.models.exceptions import InvalidHandType, InvalidAction
from lib.models.player import Player
from lib.enums.rank import Rank
from lib.enums.suit import Suit
from lib.enums.hand import HandType
from lib.enums.gameStatus import GameStatus
from lib.controllers.thirteenService import ThirteenService


class ThirteenServiceTest(unittest.TestCase):
    def test_create_game(self):
        player_id = '12345'
        game = ThirteenService.create_new_game(player_id)

        # Check that game is created
        self.assertIsNotNone(game)

        # Check that there is 1 player in the game
        self.assertEqual(len(game.players), 1)

        # Check that player has correct id
        self.assertEqual(game.players[0].id, player_id)

        # Check that game has status "NEW_GAME"
        self.assertEqual(game.game_state, GameStatus.NEW_GAME)

    def test_add_player(self):
        player_ids = ['1', '2', '3', '4', '5']
        game = ThirteenService.create_new_game(player_ids[0])

        player2 = ThirteenService.add_player(game, player_ids[1])
        # Check that player2 Player object is returned
        self.assertTrue(isinstance(player2, Player))
        # Check that player2 was created with correct id
        self.assertEqual(player2.id, '2')
        # Check that player2 was added to the game
        self.assertEqual(len(game.players), 2)
        # Check that player cannot be added again to the game
        self.assertRaises(InvalidAction, ThirteenService.add_player, game, player_ids[1])

        player3 = ThirteenService.add_player(game, player_ids[2])

        # Check that player3 was added to the game
        self.assertEqual(len(game.players), 3)

        player4 = ThirteenService.add_player(game, player_ids[3])

        # Check that player4 was added to the game
        self.assertEqual(len(game.players), 4)

        # Check that error is raised if too many players are added
        self.assertRaises(InvalidAction, ThirteenService.add_player, game, player_ids[4])




    def test_start_game(self):
        game1 = ThirteenService.create_new_game('1')

        # Check that game cant be started with 1 person
        self.assertRaises(InvalidAction, ThirteenService.start_game, game1)

        ThirteenService.add_player(game1, '2')
        ThirteenService.start_game(game1)

        # Check that game status is no longer NEW_GAME
        self.assertNotEqual(game1.game_state, GameStatus.NEW_GAME)
        # Check that game cant be add more players after its started
        self.assertRaises(InvalidAction, ThirteenService.add_player, game1, '3')

        game2 = ThirteenService.create_new_game('1')
        ThirteenService.add_player(game2, '2')
        ThirteenService.add_player(game2, '3')
        ThirteenService.start_game(game2)

        # Check that game status is no longer NEW_GAME
        self.assertNotEqual(game2.game_state, GameStatus.NEW_GAME)

        game3 = ThirteenService.create_new_game('1')
        ThirteenService.add_player(game3, '2')
        ThirteenService.add_player(game3, '3')
        ThirteenService.add_player(game3, '4')
        ThirteenService.start_game(game3)
        start_card = Card(Suit.SPADE, Rank.THREE)
        start_player_index = None
        for i,player in enumerate(game3.players):
            if start_card in player.hand:
                start_player_index = i

        # Check that game status is set to player who has starting card
        self.assertEqual(game3.game_state, GameStatus(start_player_index))


    def test_get_hand_type(self):
        three_spades = Card(Suit.SPADE, Rank.THREE)
        three_hearts = Card(Suit.HEART, Rank.THREE)

        four_spades = Card(Suit.SPADE, Rank.FOUR)
        four_clubs = Card(Suit.CLUB, Rank.FOUR)
        four_diamonds = Card(Suit.DIAMOND, Rank.FOUR)
        four_hearts = Card(Suit.HEART, Rank.FOUR)
        five_spades = Card(Suit.SPADE, Rank.FIVE)
        five_clubs = Card(Suit.CLUB, Rank.FIVE)
        six_hearts = Card(Suit.HEART, Rank.SIX)

        # SINGLE 
        self.assertEqual(ThirteenService.get_hand_type([three_spades]), HandType.SINGLE)
        # PAIR 
        self.assertEqual(ThirteenService.get_hand_type([three_spades, three_hearts]), HandType.PAIR)
        self.assertNotEqual(ThirteenService.get_hand_type([three_spades, three_hearts]), HandType.SINGLE)
        self.assertNotEqual(ThirteenService.get_hand_type([three_spades, three_hearts]), HandType.STRAIGHT)
        self.assertNotEqual(ThirteenService.get_hand_type([three_spades, three_hearts]), HandType.TRIPLE)

        self.assertRaises(InvalidHandType, ThirteenService.get_hand_type, [three_spades, four_hearts])
        # TRIPLE
        self.assertEqual(ThirteenService.get_hand_type([four_hearts, four_spades, four_clubs]), HandType.TRIPLE)
        self.assertNotEqual(ThirteenService.get_hand_type([four_hearts, four_spades, four_clubs]), HandType.SINGLE)
        self.assertNotEqual(ThirteenService.get_hand_type([four_hearts, four_spades, four_clubs]), HandType.STRAIGHT)
        self.assertNotEqual(ThirteenService.get_hand_type([four_hearts, four_spades, four_clubs]), HandType.PAIR)

        self.assertRaises(InvalidHandType, ThirteenService.get_hand_type, [four_hearts, three_spades, four_clubs])

        # STRAIGHT
        self.assertEqual(ThirteenService.get_hand_type([three_hearts, four_clubs, five_spades]), HandType.STRAIGHT)
        self.assertEqual(ThirteenService.get_hand_type([three_hearts, four_clubs, five_spades, six_hearts]), HandType.STRAIGHT)
        self.assertNotEqual(ThirteenService.get_hand_type([three_hearts, four_clubs, five_spades]), HandType.SINGLE)
        self.assertNotEqual(ThirteenService.get_hand_type([three_hearts, four_clubs, five_spades]), HandType.PAIR)
        self.assertNotEqual(ThirteenService.get_hand_type([three_hearts, four_clubs, five_spades]), HandType.TRIPLE)

        self.assertRaises(InvalidHandType, ThirteenService.get_hand_type, [three_hearts, four_clubs, six_hearts])

    def test_valid_play(self):
        three_spades = Card(Suit.SPADE, Rank.THREE)
        three_hearts = Card(Suit.HEART, Rank.THREE)
        four_spades = Card(Suit.SPADE, Rank.FOUR)
        four_clubs = Card(Suit.CLUB, Rank.FOUR)
        four_diamonds = Card(Suit.DIAMOND, Rank.FOUR)
        four_hearts = Card(Suit.HEART, Rank.FOUR)
        five_spades = Card(Suit.SPADE, Rank.FIVE)
        five_clubs = Card(Suit.CLUB, Rank.FIVE)
        six_hearts = Card(Suit.HEART, Rank.SIX)

        """

        """
        self.assertFalse(ThirteenService.is_valid_play(None, None))

        self.assertRaises(InvalidHandType, ThirteenService.is_valid_play, None, [three_spades, four_spades])
        
        self.assertTrue(ThirteenService.is_valid_play(None, [three_spades]))
        self.assertTrue(ThirteenService.is_valid_play([three_spades], [three_hearts]))
        self.assertFalse(ThirteenService.is_valid_play([three_hearts], [three_spades]))
        self.assertTrue(ThirteenService.is_valid_play([three_hearts], [four_spades]))
        self.assertFalse(ThirteenService.is_valid_play([four_spades], [three_hearts]))

        self.assertTrue(ThirteenService.is_valid_play(None, [three_spades, three_hearts]))
        self.assertTrue(ThirteenService.is_valid_play([four_spades, four_clubs], [four_diamonds, four_hearts]))
        self.assertFalse(ThirteenService.is_valid_play([four_hearts, four_spades], [four_clubs, four_diamonds]))
        self.assertTrue(ThirteenService.is_valid_play([three_hearts, three_spades], [four_spades, four_clubs]))
        self.assertFalse(ThirteenService.is_valid_play([four_spades, four_clubs], [three_hearts, three_spades]))

        self.assertRaises(InvalidHandType, ThirteenService.is_valid_play, [three_hearts, three_spades], [four_spades, five_spades])

        self.assertTrue(ThirteenService.is_valid_play(None, [three_spades, four_spades, five_spades]))
        self.assertFalse(ThirteenService.is_valid_play([three_spades, four_spades, five_clubs], [three_spades, four_spades, five_spades]))
        self.assertTrue(ThirteenService.is_valid_play([three_spades, four_spades, five_spades], [three_spades, four_spades, five_clubs]))
        self.assertTrue(ThirteenService.is_valid_play([three_spades, four_spades, five_spades], [four_spades, five_clubs, six_hearts]))
        self.assertFalse(ThirteenService.is_valid_play([four_spades, five_clubs, six_hearts], [three_spades, four_spades, five_spades]))

        self.assertRaises(InvalidHandType, ThirteenService.is_valid_play, [four_spades, five_clubs, six_hearts], [three_spades, three_hearts, five_spades])


if __name__ == '__main__':
    unittest.main()