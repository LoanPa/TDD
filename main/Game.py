

class Game:
    def __init__(self, player1: str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._player1_points = 0
        self._player2_points = 0
        
    def player_wins(self, player, points):
        if self._player1 == player:
            self._player1_points += points
        else:
            self._player2_points += points
        
    def get_score(self):
        if self._player1_points == 1 and self._player2_points == 1:
            return "Fifteen-All"
        if self._player1_points == 1:
            return "Fifteen-Love"
        if self._player2_points == 1:
            return "Love-Fifteen"
        if self._player1_points == 2:
            return "Thirty-Love"
        if self._player1_points == 4 and self._player2_points == 0:
            return "Win for Player One"
        return "Love-All"

