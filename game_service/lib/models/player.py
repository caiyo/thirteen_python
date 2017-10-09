from lib.enums.PlayerStatus import PlayerStatus
import json


class Player(object):

    def __init__(self, id, hand=[], round_status=PlayerStatus.PLAYING):
        self.id = id
        self.hand = set(hand)
        self.round_status = round_status

    def remove_cards(self, cards):
        for card in cards:
            self.hand.remove(card)
        if len(self.hand) == 0:
            self.set_round_status(PlayerStatus.OUT)

    def set_round_status(self, status):
        self.round_status = status

    def is_playing(self):
        if self.round_status == PlayerStatus.PASSED or self.round_status == PlayerStatus.PLAYING:
            return True
        return False

    def __eq__(self, other):
            return self.id == other.id

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.__str__()