from model.cave import Cave
from model.cave_simulation import CaveSimulation
from model.scan_traces_parser import ScanTracesParser
from model.point import Point

class Solution:
    input = []
    DEFAULT_SAND_SOURCE_POSITION = Point(500,0)

    def __init__(self, input):
        self.input = input

    def solve(self):
        cave_structure = ScanTracesParser().parse_cave_rock_structure(self.input)
        cave_structure.add_sand_source(self.DEFAULT_SAND_SOURCE_POSITION)
        cave_simulation = CaveSimulation(cave_structure)
        sand_units = cave_simulation.perform_simulation_until_sand_falls_into_abyss()
        return sand_units



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
    # 592

