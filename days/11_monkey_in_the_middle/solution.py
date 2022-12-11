from model.monkey import Monkey
from model.monkey_interaction import MonkeyInteraction

class Solution:
    monkeys: list[Monkey] = []

    def __init__(self, input: list[Monkey]):
        self.monkeys = input

    def solve(self):
        monkey_interaction = MonkeyInteraction(self.monkeys)
        monkey_interaction.perform_rounds(20)
        return monkey_interaction.get_monkey_business()


def read_input() -> list[Monkey]:
    return [
        Monkey(0, [84, 72, 58, 51], lambda worry: worry * 3, lambda worry: worry % 13 == 0, 1, 7),
        Monkey(1, [88, 58, 58], lambda worry: worry + 8, lambda worry: worry % 2 == 0, 7, 5),
        Monkey(2, [93, 82, 71, 77, 83, 53, 71, 89], lambda worry: worry * worry, lambda worry: worry % 7 == 0, 3, 4),
        Monkey(3, [81, 68, 65, 81, 73, 77, 96], lambda worry: worry + 2, lambda worry: worry % 17 == 0, 4, 6),
        Monkey(4, [75, 80, 50, 73, 88], lambda worry: worry + 3, lambda worry: worry % 5 == 0, 6, 0),
        Monkey(5, [59, 72, 99, 87, 91, 81], lambda worry: worry * 17, lambda worry: worry % 11 == 0, 2, 3),
        Monkey(6, [86, 69], lambda worry: worry + 6, lambda worry: worry % 3 == 0, 1, 0),
        Monkey(7, [91], lambda worry: worry + 1, lambda worry: worry % 19 == 0, 2, 5),
    ]


if __name__ == '__main__':
    input_lines = read_input()
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
