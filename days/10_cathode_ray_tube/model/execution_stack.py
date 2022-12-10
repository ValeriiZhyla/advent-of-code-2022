from .instruction import Instruction
from .register import Register


class ExecutionStack:
    register: Register = None
    instructions: list[Instruction] = []

    def __init__(self, register: Register):
        self.register = register
        self.instructions = []

    def process_cycle(self):
        self.remove_finished_instructions_from_stack()
        # tick
        for instruction in self.instructions:
            instruction.tick()

    def add_instruction(self, instruction: Instruction):
        self.instructions.append(instruction)

    def is_empty(self) -> bool:
        return self.instructions == []

    def remove_finished_instructions_from_stack(self):
        self.instructions = list(filter(lambda i: not i.executed, self.instructions))
