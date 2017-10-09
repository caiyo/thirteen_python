from lib.enums.hand import HandType
from lib.models.exceptions import InvalidHandType, InvalidPlay, InvalidAction
from lib.models.deck import Deck
from lib.models.card import Card
from lib.models.game import Game
from lib.models.player import Player
from lib.enums.suit import Suit
from lib.enums.rank import Rank
from lib.enums.gameStatus import GameStatus

import uuid


class ThirteenService(object):

    @classmethod
    def create_new_game(cls, player_id):
        player = Player(player_id)
        game = Game(uuid.uuid4(), players=[player])
        game.create()
        return game

    @classmethod
    def start_game(cls, game):
        if game.game_state != GameStatus.NEW_GAME:
            raise InvalidAction("Invalid Action: game has already been started")

        if len(game.players) < 2:
            raise InvalidAction("Invalid Action: cannot start game with less than 2 players")

        hands = cls._create_player_hands(len(game.players))
        start_card = Card(Suit.SPADE, Rank.THREE)
        for i, player in enumerate(game.players):
            player_hand = hands.pop()
            player.hand = player_hand

            # If player hand has three of spades, set game status to be that players turn
            if start_card in player_hand:
                game.game_state = GameStatus(i)

        return game

    @classmethod
    def add_player(cls, game, player_id):
        player = Player(player_id)
        game.add_player(player)
        return player

    @classmethod
    def is_valid_play(cls, prev_played_cards, played_cards):
        """
            For a move to be valid, the same amount of cards needs to be played as the previous
            player. The hand type must also be the same and the newly played cards must be greater
            than the previous
        """
        played_hand_type = cls.get_hand_type(played_cards)
        prev_hand_type = cls.get_hand_type(prev_played_cards)

        if not played_hand_type:
            return False

        # If no previous played cards and played cards has a type, return True
        if not prev_hand_type and played_hand_type:
            return True

        # Bomb beats any previously played cards
        if played_hand_type == HandType.BOMB:
            return True

        # played cards must be the same hand type as previously played
        if len(prev_played_cards) != len(played_cards) or \
                played_hand_type != prev_hand_type:
            return False

        return played_cards[-1] > prev_played_cards[-1]
    
    @classmethod
    def get_hand_type(cls, cards):
        if not cards:
            return None
        
        cards.sort()
        if cls._is_single(cards):
            return HandType.SINGLE
        if cls._is_pair(cards):
            return HandType.PAIR
        if cls._is_triple(cards):
            return HandType.TRIPLE
        if cls._is_straight(cards):
            return HandType.STRAIGHT
        if cls._is_bomb(cards):
            return HandType.BOMB
        
        raise InvalidHandType("Invalid Hand: {0} is not a valid hand".format(cards))

    @classmethod
    def _create_player_hands(cls, total_hands):
        deck = Deck()
        hands = [set() for _ in xrange(total_hands)]
        cards_in_deck = 52
        cards_per_hand = cards_in_deck // total_hands

        for i in xrange(0, cards_per_hand*total_hands):
            hands[i%total_hands].add(deck.cards.pop())

        # if only creating 3 hands, there will be 1 left over card
        # The hand with the 3 of spades should get it
        if total_hands == 3:
            card = Card(Suit.SPADE, Rank.THREE)
            for hand in hands:
                if card in hand:
                    hand.add(deck.cards.pop())
        return hands

    @classmethod
    def _is_single(cls, cards):
        if cards and len(cards) == 1:
            return True
        return False
    
    @classmethod
    def _is_pair(cls, cards):
        if cards and len(cards) == 2 and cards[0].rank == cards[1].rank:
            return True
        return False
    @classmethod
    def _is_triple(cls, cards):
        if cards and len(cards) == 3 and cards[0].rank == cards[1].rank and cards[1].rank == cards[2].rank:
            return True
        return False
    
    @classmethod
    def _is_straight(cls, cards):
        if not cards or len(cards) < 3:
            return False
        for c_1, c_2 in zip(cards, cards[1:]):
            if c_1.rank.value != c_2.rank.value-1:
                return False
        return True

    @classmethod
    def _is_bomb(self, cards):
        # TODO implement
        return False