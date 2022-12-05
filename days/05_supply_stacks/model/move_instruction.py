import re


class MoveInstruction:
    quantity_to_move: int = 0
    stack_from: int = 0
    stack_to: int = 0

    PATTERN_MOVE_INSTRUCTION = r'move (\d+) from (\d+) to (\d+)'

    def __init__(self, instruction_text: str):
        m = re.match(self.PATTERN_MOVE_INSTRUCTION, instruction_text)
        if m:
            self.quantity_to_move = int(m.group(1))
            self.stack_from = int(m.group(2)) - 1
            self.stack_to = int(m.group(3)) - 1
        else:
            raise Exception(f"Text of instruction [{instruction_text}] does not match the expected pattern [{self.PATTERN_MOVE_INSTRUCTION}]")
