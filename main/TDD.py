

class Game:
    def __init__(self, player1: str, player2: str):
        self._player1 = player1
        self._player2 = player2
        self._p1Score = 0
        self._p2Score = 0
        
    def player_wins(self, player):
        if self._player1 == player:
            self._p1score += 1
        else:
            self._p2score += 1  
        
    def get_score(self):
        if _p1Score == _p2Score:
            return "Fifteen-All"
        if self._p1Score == 1:
            return "Fifteen-Love"
        if self._p1Score == 1:
            return "Love-Fifteen"
        return "Love-All"
