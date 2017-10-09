from lib.models.exceptions import InvalidHandType, InvalidPlay, InvalidAction
from lib.enums.PlayerStatus import PlayerStatus
from lib.enums.gameStatus import GameStatus

class Game(object):
    def __init__(self, id, card_stack=[], players=[], game_state=GameStatus.NEW_GAME):
        self.id = id
        self.card_stack = card_stack
        self.players = players
        self.game_state = game_state

    def play_cards(self, player, cards):
        if not cards:
            raise InvalidPlay("Invalid Play: You must play cards")
        try:
            player.remove_cards(cards)
            self.card_stack.append(cards)
        except KeyError:
            raise InvalidPlay("Invalid Play: Player doesn't have played cards")

        return self

    def player_pass(self, player):
        player.set_round_status(PlayerStatus.PASSED)

    def reset_round(self):
        for player in self.players:
            if player.is_playing():
                player.set_round_status(PlayerStatus.PLAYING)

    def add_player(self, player):
        if self.game_state != GameStatus.NEW_GAME:
            raise InvalidAction("Invalid Action: cannot add a player to a game already started")

        if len(self.players) >= 4:
            raise InvalidAction("Invalid Action: cannot have more than 4 players in a game")

        if player in self.players:
            raise InvalidAction("Invalid Action: player already in game")

        self.players.append(player)

    def create(self):
        # persist to db
        pass

    def start(self):
        pass

    # def __str__(self):
    #     return self.__dict__
    #
    # def __repr__(self):
    #     return self.__str__()