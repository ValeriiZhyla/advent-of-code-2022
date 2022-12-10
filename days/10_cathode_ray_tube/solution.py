from model.register import Register
from model.cpu import CPU

class Solution:
    instructions = []
    REGISTER_STARTING_VALUE = 1

    def __init__(self, input):
        self.instructions = input

    def solve(self):
        register = Register(self.REGISTER_STARTING_VALUE)
        cpu = CPU(register)
        cpu.process_instructions_sequentially(self.instructions)
        return cpu.sum_signal_strengths([20, 60, 100, 140, 180, 220])


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

