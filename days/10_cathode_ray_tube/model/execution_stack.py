from .instruction import Instruction
from .register import Register


class ExecutionStack:
    register: Register = None
    instructions: list[Instruction] = []

    def __init__(self, register: Register):
        self.register = register
        self.instructions = []

    def process_cycle_sequential(self):
        self.remove_finished_instructions_from_stack()
        # tick
        if len(self.instructions) > 0:
            self.instructions[0].tick()

    def add_instruction(self, instruction: Instruction):
        self.instructions.append(instruction)

    def has_no_pending_tasks(self) -> bool:
        return len(list(filter(lambda i: not i.executed, self.instructions))) == 0

    def remove_finished_instructions_from_stack(self):
        self.instructions = list(filter(lambda i: not i.executed, self.instructions))
