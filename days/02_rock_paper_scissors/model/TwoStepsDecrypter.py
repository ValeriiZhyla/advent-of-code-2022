from .RPS import RPS


class TwoStepsDecrypter:
    ROCK_CODES = ["A"]
    PAPER_CODES = ["B"]
    SCISSORS_CODES = ["C"]

    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"

    def decrypt_moves(self, encrypted_moves: list[str]) -> list[(RPS, RPS)]:
        decrypted_moves: list[(RPS, RPS)] = []
        for line in encrypted_moves:
            (move_fst, desired_result) = line.split(" ")
            shape_fst = self.decrypt(move_fst)
            shape_snd = self.shape_to_get_desired_result(shape_fst, desired_result)
            decrypted_moves.append((shape_fst, shape_snd))
        return decrypted_moves

    def decrypt(self, token: str) -> RPS:
        if token in self.ROCK_CODES:
            return RPS.ROCK
        elif token in self.PAPER_CODES:
            return RPS.PAPER
        elif token in self.SCISSORS_CODES:
            return RPS.SCISSORS
        else:
            raise Exception(f"Token {token} cannot be decrypted")

    def shape_to_get_desired_result(self, shape: RPS, desired_result: str) -> RPS:
        if desired_result == self.DRAW:
            return shape
        if shape == RPS.ROCK:
            if desired_result == self.WIN:
                return RPS.PAPER
            if desired_result == self.LOSS:
                return RPS.SCISSORS
        if shape == RPS.PAPER:
            if desired_result == self.WIN:
                return RPS.SCISSORS
            if desired_result == self.LOSS:
                return RPS.ROCK
        if shape == RPS.SCISSORS:
            if desired_result == self.WIN:
                return RPS.ROCK
            if desired_result == self.LOSS:
                return RPS.PAPER
