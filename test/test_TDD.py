
import pytest

import sys
sys.path.append('../')
from main.TDD import *

def test_call_get_score():
    get_score()

# When game starts return "love-all"
def test_WhenGameStarts_then_loveAll():
    get_score()