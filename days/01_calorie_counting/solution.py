import functools
import itertools

from model.ExpeditionBuilder import *


class Solution:
    common_provision_calories: list[str] = []

    def __init__(self, input):
        self.common_provision_calories_list = input

    def solve(self) -> int:
        expedition = ExpeditionBuilder().create_expedition(self.common_provision_calories_list)
        elf_carrying_most_calories = expedition.find_elf_carrying_most_calories()
        return elf_carrying_most_calories.all_carried_calories()

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
    print(f"Full solution : {solution.solve()}")