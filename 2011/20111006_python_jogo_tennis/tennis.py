class Game():

    def __init__(self, score1=0, score2=0):
        self.score = (score1, score2)

    def scores(self, player):
        score1, score2 = self.score

        if player == 1:
            score1 = self._calculate_new_score(score1)
        else:
            score2 = self._calculate_new_score(score2)

        self.score = (score1, score2)

    def _calculate_new_score(self, old_score):
        if old_score == 30:
            return old_score + 10
        elif old_score == 40:
            return 45
        else:
            return old_score + 15

    def status(self):
        if self.score[0] == 45:
            return 'player 1 win'
        return 'Deuce'
