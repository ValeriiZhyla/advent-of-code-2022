from model.rope_physics import RopePhysics

class Solution:
    rope_head_moves: list[str] = []

    def __init__(self, input):
        self.rope_head_moves = input

    def solve(self):
        physics = RopePhysics()
        physics.calculate_tail_movements_for_head_moves(self.rope_head_moves)
        return 0

def read_input() -> list[str]:
    input_file_name = 'full_input.txt'
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

