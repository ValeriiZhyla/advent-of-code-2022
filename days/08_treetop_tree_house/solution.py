from model.forest_analyzer import ForestAnalyzer

class Solution:
    trees: list[list[int]] = []

    def __init__(self, input: list[list[int]]):
        self.trees = input

    def solve(self) -> int:
        amount_of_visible_trees = ForestAnalyzer().count_visible_trees_lrtb(self.trees)

        return amount_of_visible_trees


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


def transform_input(input_lines: list[str]) -> list[list[int]]:
    trees = []
    for line in input_lines:
        trees.append(list(map(lambda c: int(c), list(line))))
    return trees



if __name__ == '__main__':
    input_lines = read_input()
    input_lines = transform_input(input_lines)
    print(input_lines)
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")

