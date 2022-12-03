from model.priority_calculator import PriorityCalculator


class Solution:
    rucksack_contents: list[str] = []

    def __init__(self, input):
        self.rucksack_contents = input

    def solve(self) -> (int, int):
        # first task
        priority_of_common_items_in_each_rucksack_half = PriorityCalculator().calculate_total_priority_of_common_items_in_each_rucksack_half(self.rucksack_contents)
        # second task
        priority_of_badges_of_each_group = PriorityCalculator().calculate_total_priority_of_common_items_in_each_group(self.rucksack_contents)
        return priority_of_common_items_in_each_rucksack_half,priority_of_badges_of_each_group


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
    # 7831
