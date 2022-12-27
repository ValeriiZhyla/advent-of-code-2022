from model.valve_parser import ValveParser
from model.valve import Valve
from model.tunnel_network import TunnelNetwork

FULL_INPUT = "input.txt"
TEST_INPUT = "small_input.txt"

GIVEN_TIME = 15


class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self) -> int:
        valves: list[Valve] = ValveParser().parse(self.input)
        max_possible_pressure_release: int = TunnelNetwork(valves).calculate_max_possible_pressure_release(valves[0], GIVEN_TIME)
        return max_possible_pressure_release


def read_input() -> list[str]:
    input_file_name = TEST_INPUT
    # input_file_name = FULL_INPUT
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
