from model.monkey import Monkey, OptimizedMonkey
from model.monkey_interaction import MonkeyInteraction, MonkeyInteractionLong
import copy

class Solution:
    monkeys: list[Monkey] = []

    def __init__(self, input: list[Monkey]):
        self.monkeys = input

    def solve(self) -> (int, int):
        # task 1
        #monkey_interaction_short = MonkeyInteraction(copy.deepcopy(self.monkeys))
        #monkey_interaction_short.perform_rounds(20)
        # task 2
        monkey_interaction_long = MonkeyInteractionLong(copy.deepcopy(self.monkeys))
        monkey_interaction_long.perform_rounds(10000)
        # return monkey_interaction_short.get_monkey_business(), monkey_interaction_long.get_monkey_business()
        return 1, monkey_interaction_long.get_monkey_business()


def read_input() -> list[OptimizedMonkey]:
    return [
        OptimizedMonkey(0, [chr(79), chr(98)], lambda worry: worry * 19, 23, 2, 3),
        OptimizedMonkey(1, [chr(54), chr(65), chr(75), chr(74)], lambda worry: chr(ord(worry[-1]) + 6), 19, 2, 0),
        OptimizedMonkey(2, [chr(79), chr(60), chr(97)], lambda worry: worry + worry, 13, 1, 3),
        OptimizedMonkey(3, [chr(74)], lambda worry: chr(ord(worry[-1]) + 3), 17, 0, 1),
    ]


if __name__ == '__main__':
    input_lines = read_input()
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
    # 55458