from .instruction import Instruction
from .register import Register


class ExecutionStack:
    register: Register = None
    instructions: list[Instruction] = []
    current_cycle_id: int = 1

    def __init__(self, register: Register):
        self.register = register
        self.instructions = []
        self.current_cycle_id = 1

    def process_cycle(self):
        # remove finished instructions
        for instruction_idx in range(0, len(self.instructions)):
            instruction = self.instructions[instruction_idx]
            if instruction.executed:
                self.instructions.pop(instruction_idx)
        # tick
        for instruction in self.instructions:
            instruction.tick()
