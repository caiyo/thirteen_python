from baseEnum import BaseEnum


class GameStatus(BaseEnum):
    PLAYER_ONE_TURN = 0
    PLAYER_TWO_TURN = 1
    PLAYER_THREE_TURN = 2
    PLAYER_FOUR_TURN = 3

    PLAYER_ONE_WIN = 4
    PLAYER_TWO_WIN = 5
    PLAYER_THREE_WIN = 6
    PLAYER_FOUR_WIN = 7

    NEW_GAME = 8