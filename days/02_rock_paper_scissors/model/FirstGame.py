from .RPS import RPS


class FirstGame:
    moves: list[(RPS, RPS)]

    LOSS_SCORE = 0
    DRAW_SCORE = 3
    WIN_SCORE = 6

    def __init__(self, decrypted_moves: list[(RPS, RPS)]):
        self.moves = decrypted_moves

    def calculate_score_of_second_player(self) -> int:
        total_score: int = 0
        for move in self.moves:
            (fst, snd) = move
            total_score += self.shape_score(snd)
            total_score += self.round_outcome_snd(fst, snd)
        return total_score

    def shape_score(self, shape: RPS) -> int:
        return int(shape.value)

    def round_outcome_snd(self, fst: RPS, snd: RPS) -> int:
        if fst == snd:
            return self.DRAW_SCORE
        if snd == RPS.PAPER and fst == RPS.ROCK:
            return self.WIN_SCORE
        if snd == RPS.ROCK and fst == RPS.SCISSORS:
            return self.WIN_SCORE
        if snd == RPS.SCISSORS and fst == RPS.PAPER:
            return self.WIN_SCORE
        else:
            return self.LOSS_SCORE
