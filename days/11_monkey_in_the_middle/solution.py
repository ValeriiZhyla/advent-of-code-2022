from model.monkey import Monkey
from model.monkey_interaction import MonkeyInteraction, MonkeyInteractionLong
from model.item import Item
from model.operation import Operation, Add, Square, MultiplyBy
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
        monkey_interaction_long.perform_rounds(20)
        # return monkey_interaction_short.get_monkey_business(), monkey_interaction_long.get_monkey_business()
        return 1, monkey_interaction_long.get_monkey_business()


def read_input() -> list[Monkey]:
    return [
        Monkey(0, [Item(79), Item(98)], MultiplyBy(19), 23, 2, 3),
        Monkey(1, [Item(54), Item(65), Item(75), Item(74)], Add(6), 19, 2, 0),
        Monkey(2, [Item(79), Item(60), Item(97)], Square(), 13, 1, 3),
        Monkey(3, [Item(74)], Add(3), 17, 0, 1),
    ]


if __name__ == '__main__':
    input_lines = read_input()
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
    # 55458