from model.ExpeditionBuilder import ExpeditionBuilder


class Solution:
    common_provision_calories: list[str] = []

    def __init__(self, input):
        self.common_provision_calories_list = input

    def solve(self) -> (int, int):
        expedition = ExpeditionBuilder().create_expedition(self.common_provision_calories_list)
        # first task
        main_carrier_calories = expedition.calories_of_main_carrier()
        # second task
        amount_of_calories_carried_by_top_3_elves = expedition.sum_of_top_tree_carriers()

        return main_carrier_calories, amount_of_calories_carried_by_top_3_elves


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
