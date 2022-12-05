from model.stack import Stack
from model.move_instruction import MoveInstruction
from model.stack_description_parser import StackDescriptionParser
from model.move_description_parser import MoveDescriptionParser
from model.cargo_crane import CargoCrane


class Solution:
    input: list[str] = []
    stacks_description: list[str] = []
    moves_description: list[str] = []

    EMPTY_LINE = ""

    def __init__(self, input):
        self.input = input

    def solve(self):
        self.process_input()
        parsed_stacks: list[Stack] = StackDescriptionParser().stacks_description_to_stacks(self.stacks_description)
        parsed_moves: list[MoveInstruction] = MoveDescriptionParser().moves_description_to_move_instructions(self.moves_description)
        cargo_crane = CargoCrane(parsed_stacks)
        cargo_crane.perform_move_instructions(parsed_moves)
        return cargo_crane.top_crate_of_each_stack_as_string()


    def process_input(self):
        newline_met = False
        for line in self.input:
            if line == self.EMPTY_LINE:
                newline_met = True
                continue
            if not newline_met:
                self.stacks_description.append(line)
            else:
                self.moves_description.append(line)


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
    # QNNTGTPFN

