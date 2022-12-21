from model.path_finder import PathFinder
from model.paths_graph import PathsGraph
from model.paths_graph_parser import PathsGraphParser

class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self) -> int:
        available_paths: PathsGraph = PathsGraphParser().build_graph(self.input)
        return available_paths


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

