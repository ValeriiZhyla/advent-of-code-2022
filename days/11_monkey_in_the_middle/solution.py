from model.monkey import Monkey
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
        monkey_interaction_long.perform_rounds(1000)
        # return monkey_interaction_short.get_monkey_business(), monkey_interaction_long.get_monkey_business()
        return 1, monkey_interaction_long.get_monkey_business()


def read_input() -> list[Monkey]:
    return [
        Monkey(0, [79, 98], lambda worry: worry * 19, lambda worry: worry % 23 == 0, 2, 3),
        Monkey(1, [54, 65, 75, 74], lambda worry: worry + 6, lambda worry: worry % 19 == 0, 2, 0),
        Monkey(2, [79, 60, 97], lambda worry: worry * worry, lambda worry: worry % 13 == 0, 1, 3),
        Monkey(3, [74], lambda worry: worry + 3, lambda worry: worry % 17 == 0, 0, 1),
    ]


if __name__ == '__main__':
    input_lines = read_input()
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
    # 55458