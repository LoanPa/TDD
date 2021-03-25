

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
        result = ""

        if self._player1_points >= 4 or self._player2_points >= 4:  # Algun dels dos es mes de 4
            if self._player1_points > self._player2_points:  # p1 te avantatge o guanya
                if (self._player2_points + 1) < self._player1_points:  # p1 guanya
                    result = "Win for Player One"
                else:
                    result = "Advantage Player One"
            elif self._player1_points < self._player2_points:
                if (self._player1_points + 1) < self._player2_points:
                    result = "Win for Player Two"
                else:
                    result = "Advantage Player Two"
            else:
                result = "Deuce"
            return result
        else:

            if self._player2_points >= 4 and self._player1_points < (self._player2_points + 2):
                result += "Win for Player Two"
            else:
                if self._player1_points == 0:
                    result = "Love-"
                if self._player1_points == 1:
                    result = "Fifteen-"
                if self._player1_points == 2:
                    result = "Thirty-"
                if self._player1_points == 3:
                    result = "Forty-"
                if self._player1_points == self._player2_points:
                    if self._player2_points == 3:
                        return "Deuce"
                    else:
                        result += "All"

                else:
                    if self._player2_points == 0:
                        result += "Love"
                    if self._player2_points == 1:
                        result += "Fifteen"
                    if self._player2_points == 2:
                        result += "Thirty"
                    if self._player2_points == 3:
                        result += "Forty"
        return result


