import pytest
from Game import *

import sys
sys.path.append('../')


@pytest.fixture()
def setip() -> Game:
    return Game("Toni", "Carla")

@pytest.fixture()
def teardown():
    pass

@pytest.mark.parametrize("score_player_1,score_player_2,expected_result", [
    (0, 0, "Love-All")
# (1,1,"Fifteen-All"),
# ()
# (14,16,"Win for player2))
 ])
def test_whenGameStart_thenLoveAll(setup,  teardown):
    # ARRANGE
    game = setup
    # ACT
    result = get_score()
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