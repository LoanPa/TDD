import pytest

import sys
sys.path.append('../')
from main.Game import *



@pytest.fixture()
def setup() -> Game:
    return Game("Toni", "Carla")

@pytest.fixture()
def teardown():
    pass

@pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Deuce"),
    (4, 4, "Deuce"),
    (1, 0, "Fifteen-Love"),
    (0, 1, "Love-Fifteen"),
    (2, 0, "Thirty-Love"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for player1"),
    (0, 4, "Win for player2"),
    (2, 1, "Thirty-Fifteen"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for player1"),
    (1, 4, "Win for player2"),
    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for player1"),
    (2, 4, "Win for player2"),
    (4, 3, "Advantage player1"),
    (3, 4, "Advantage player2"),
    (5, 4, "Advantage player1"),
    (4, 5, "Advantage player2"),
    (15, 14, "Advantage player1"),
    (14, 15, "Advantage player2"),
    (6, 4, "Win for player1"),
    (4, 6, "Win for player2"),
    (16, 14, "Win for player1"),
    (14, 16, "Win for player2")
])
def test_game_score(score_player_1: int, score_player_2: int, expected_result: str):
    pass

def test_whenGameStart_thenLoveAll(setup, teardown):
    # ARRANGE
    game = setup
    # ACT
    result = game.get_score()
    # ASSERT
    assert result == "Love-All"


def test_whenPlayer1onePoint_thenFifteenLove(setup, teardown):
    # ARRANGE
    game = setup
    # ACT
    game.player_wins("Toni")
    result = game.get_score()
    # ASSERT
    assert result == "Fifteen-Love"


def test_whenPlayer2onePoint_thenFifteenLove(setup, teardown):
    # ARRANGE
    game = setup
    # ACT
    game.player_wins("Carla")
    result = game.get_score()
    # ASSERT
    assert result == "Love-Fifteen"


def test_whenPlayer1onePointandPlayer2onePoint_thenFifteenAll(setup, teardown):
    # ARRANGE
    game = setup
    # ACT
    game.player_wins("Carla")
    game.player_wins("Toni")
    result = game.get_score()
    # ASSERT
    assert result == "Fifteen-All"

def test_whenPlayer1twoPointsandPlayer2zeroPoints_thenThirtyLove(setup, teardown):
    # ARRANGE
    game = setup
    # ACT

    game.player_wins("Toni")
    game.player_wins("Toni")
    result = game.get_score()
    print(result)
    # ASSERT
    assert result == "Thirty-Love"


##################### File 2 #####################
    """
    def create_game(player1: Player, player2: Player):
        return Game(player1, player2)

    def create_player(name: str):
        return Player(name)
  
   


    def create_game(player1: Player, player2: Player):
        return Game(player1, player2)

    def create_player(name: str):
        return Player(name)

    @pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
        (0, 0, "Love-All"),
        (1, 0, "Fifteen-Love"),
        (1, 1, "Fifteen-All"),
        (2, 1, "Thirty-Fifteen"),
        (2, 0, "Thirty-Love")
    ])
    def test_game_score(score_player_1: int, score_player_2: int, expected_result: str) -> None:
        # ARRANGE
        player1 = create_player("player1")
        player2 = create_player("player2")
        game = create_game(player1, player2)

        score_max = max(score_player_1, score_player_2)
        for score in range(0, score_max):
            if score < score_player_1:
                game.won_point(player1)
            if score < score_player_2:
                game.won_point(player2)

        # ACT
        result = game.get_score()

        # ASSERT
        assert result == expected_result
    """