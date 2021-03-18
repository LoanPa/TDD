
import pytest

import sys
sys.path.append('../')
from main.TDD import *



# When game starts return "love-all"
def test_WhenGameStarts_then_loveAll():
    result = get_score()
    assert result == "Love-All"