from model.pair_translator import PairTranslator
from model.pair_translator import CleaningPair
from model.overlap_calculator import OverlapCalculator


class Solution:
    cleaning_pairs_text: list[str] = []

    def __init__(self, input):
        self.cleaning_pairs_text = input

    def solve(self) -> (int, int):
        parsed_pairs: list[CleaningPair] = PairTranslator().transform_input_to_list_of_pairs(self.cleaning_pairs_text)
        # first task
        pairs_with_full_overlap_amount = OverlapCalculator().find_amount_of_pairs_with_full_overlap(parsed_pairs)
        # second task
        pairs_with_partial_overlap_amount = OverlapCalculator().find_amount_of_pairs_with_partial_overlap(parsed_pairs)
        return pairs_with_full_overlap_amount, pairs_with_partial_overlap_amount


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
    # 483, 874
