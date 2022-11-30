class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.game_cases_tie = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All"),
            (3, 3, "Forty-All"),
            (4, 4, "Deuce"),
        ]
        self.game_cases_over_4 = [
            (4, 6, "Win for player2"),
            (4, 5, "Advantage player2"),
            None,
            (5, 4, "Advantage player1"),
            (6, 4, "Win for player1"),
        ]
        self.game_cases_under_4 = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player):
        if player == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def game_is_a_tie(self, score):
        return self.game_cases_tie[score][2]

    def both_have_4_or_more_points(self, subtract):
        if subtract in [-1, 1]:
            score_return = self.game_cases_over_4[subtract + 2][2]
        elif 2 <= subtract:
            score_return = self.game_cases_over_4[4][2]
        else:
            score_return = self.game_cases_over_4[0][2]
        return score_return

    def both_have_3_or_less_points(self, score_tuple):
        player1_score = score_tuple[0]
        player2_score = score_tuple[1]
        return self.game_cases_under_4[player1_score] + "-" + self.game_cases_under_4[player2_score]

    def get_score(self):
        
        if self.m_score1 == self.m_score2:
            score = self.game_is_a_tie(self.m_score1)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            subtract = self.m_score1 - self.m_score2
            score = self.both_have_4_or_more_points(subtract)

        else:
            score = self.both_have_3_or_less_points((self.m_score1, self.m_score2))

        return score
