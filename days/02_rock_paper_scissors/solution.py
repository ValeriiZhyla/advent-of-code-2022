from model.RPS import RPS
from model.Decrypter import Decrypter
from model.Game import Game

class Solution:
    encrypted_moves = []

    def __init__(self, input):
        self.encrypted_moves = input

    def solve(self) -> int:
        encrypted_rounds: list[(RPS, RPS)] = Decrypter().decrypt_moves(self.encrypted_moves)
        score_of_second_player = Game(encrypted_rounds).calculate_score_of_second_player()
        return score_of_second_player




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

