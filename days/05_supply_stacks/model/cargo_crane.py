from .stack import Stack
from .crate import Crate
from .move_instruction import MoveInstruction


class CargoCrane:
    stacks: list[Stack]

    def __init__(self, stacks_to_rearrange: list[Stack]):
        self.stacks = stacks_to_rearrange

    def perform_move_instructions(self, moves: list[MoveInstruction]):
        for instruction in moves:
            crates_to_move = instruction.quantity_to_move
            assert crates_to_move >= 1
            while crates_to_move != 0:
                self.move_one_crate(instruction.stack_from, instruction.stack_to)
                crates_to_move -= 1

    def move_one_crate(self, stack_from, stack_to):
        crate: Crate = self.stacks[stack_from].take_top_crate()
        self.stacks[stack_to].place_new_crate_on_top(crate)

    def top_crate_of_each_stack_as_string(self) -> str:
        top_of_stacks = [stack.get_top_crate_name() for stack in self.stacks]
        return "".join(top_of_stacks)
