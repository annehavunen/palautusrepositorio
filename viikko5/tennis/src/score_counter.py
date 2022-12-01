class ScoreCounter:
    def get_score(self, score1, score2):
        if score1 == score2:
            score = self.even_scores(score1)
        elif score1 >= 4 or score2 >= 4:
            score = self.uneven_four_or_more(score1, score2)
        else:
            score = self.uneven_under_four(score1, score2)

        return score

    def even_scores(self, score1):
        if score1 == 0:
            score = "Love-All"
        elif score1 == 1:
            score = "Fifteen-All"
        elif score1 == 2:
            score = "Thirty-All"
        elif score1 == 3:
            score = "Forty-All"
        else:
            score = "Deuce"

        return score

    def uneven_four_or_more(self, score1, score2):
        minus_result = score1 - score2
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score
    
    def uneven_under_four(self, score1, score2):
        temp_score = 0
        score = ""

        for i in range(1, 3):
            if i == 1:
                temp_score = score1
            else:
                score = score + "-"
                temp_score = score2

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"

        return score
