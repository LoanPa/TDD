

class Game:
    def __init__(self, player1: str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._player1_points = 0
        self._player2_points = 0
        
    def player_wins(self, player):
        if self._player1 == player:
            self._player1_points += 1
        else:
            self._player2_points += 1
        
    def get_score(self):
        if self._player1_points == 1 and self._player2_points == 1:
            return "Fifteen-All"
        if self._player1_points == 1:
            return "Fifteen-Love"
        if self._player2_points == 1:
            return "Love-Fifteen"
        return "Love-All"

