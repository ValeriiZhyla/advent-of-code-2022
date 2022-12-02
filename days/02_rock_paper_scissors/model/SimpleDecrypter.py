from .RPS import RPS


class SimpleDecrypter:
    ROCK_CODES = ["X", "A"]
    PAPER_CODES = ["Y", "B"]
    SCISSORS_CODES = ["Z", "C"]

    def decrypt_moves(self, encrypted_moves: list[str]) -> list[(RPS, RPS)]:
        decrypted_moves: list[(RPS, RPS)] = []
        for line in encrypted_moves:
            (l, r) = line.split(" ")
            decrypted_moves.append((self.decrypt(l), self.decrypt(r)))
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
