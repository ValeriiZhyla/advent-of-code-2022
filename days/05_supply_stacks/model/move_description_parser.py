from .move_instruction import MoveInstruction


class MoveDescriptionParser():
    def moves_description_to_move_instructions(self, moves_description: list[str]) -> list[MoveInstruction]:
        move_instructions: list[MoveInstruction] = []
        for move in moves_description:
            move_instructions.append(MoveInstruction(move))
        return move_instructions
