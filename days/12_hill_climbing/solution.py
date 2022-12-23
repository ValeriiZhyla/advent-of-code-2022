from model.path_finder import PathFinder
from model.paths_graph import PathsGraph
from model.paths_graph_parser import PathsGraphParser

class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self) -> (int, int):
        # task 1
        graph: PathsGraph = PathsGraphParser().build_graph(self.input)
        minimal_distance_from_start = PathFinder().find_length_of_shortest_path_from_start_to_end(graph)
        # task_2
        graph: PathsGraph = PathsGraphParser().build_graph(self.input)
        minimal_distance_from_any_lowest_point = PathFinder().find_length_of_shortest_path_from_all_lowest_points_to_end(graph)
        return minimal_distance_from_start, minimal_distance_from_any_lowest_point


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
    # 425, 418

