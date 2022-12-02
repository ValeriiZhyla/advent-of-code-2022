from model.RPS import RPS
from model.SimpleDecrypter import SimpleDecrypter
from model.TwoStepsDecrypter import TwoStepsDecrypter

from model.FirstGame import FirstGame


class Solution:
    encrypted_moves = []

    def __init__(self, input):
        self.encrypted_moves = input

    def solve(self) -> (int, int):
        # first task
        encrypted_rounds_plain: list[(RPS, RPS)] = SimpleDecrypter().decrypt_moves(self.encrypted_moves)
        score_of_second_player_normal_game = FirstGame(encrypted_rounds_plain).calculate_score_of_second_player()
        # second task
        encrypted_rounds_cheating: list[(RPS, RPS)] = TwoStepsDecrypter().decrypt_moves(self.encrypted_moves)
        score_of_second_player_second_variation = FirstGame(encrypted_rounds_cheating).calculate_score_of_second_player()

        return score_of_second_player_normal_game, score_of_second_player_second_variation


def read_input() -> list[str]:
    input_file_name = 'input.txt'
    try:
        with open(input_file_name) as file:
            input_lines = file.readlines()
            if len(input_lines) == 0:
                raise Exception(f"File {input_file_name} is empty")
            input_lines_without_newline = [line.rstrip('\n') for line in input_lines]
            return input_lines_without_newline
    except EnvironmentError:
        raise Exception(f"File {input_file_name} is missing or invalid")


if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
