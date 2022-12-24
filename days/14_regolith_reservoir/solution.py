from model.cave_structure import CaveStructure
from model.scan_traces_parser import ScanTracesParser

class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self):
        cave_structure = ScanTracesParser().parse_cave_rock_structure(self.input)
        cave_structure.print()



def read_input() -> list[str]:
    input_file_name = 'small_input.txt'
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

