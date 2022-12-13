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
        monkey_interaction_short = MonkeyInteraction(copy.deepcopy(self.monkeys))
        monkey_interaction_short.perform_rounds(20)
        # task 2
        monkey_interaction_long = MonkeyInteractionLong(copy.deepcopy(self.monkeys))
        monkey_interaction_long.perform_rounds(10000)
        return monkey_interaction_short.get_monkey_business(), monkey_interaction_long.get_monkey_business()


def read_input() -> list[Monkey]:
    return [
        Monkey(0, [Item(84), Item(72), Item(58), Item(51)], MultiplyBy(3), 13, 1, 7),
        Monkey(1, [Item(88), Item(58), Item(58)], Add(8), 2, 7, 5),
        Monkey(2, [Item(93), Item(82), Item(71), Item(77), Item(83), Item(53), Item(71), Item(89)], Square(), 7, 3, 4),
        Monkey(3, [Item(81), Item(68), Item(65), Item(81), Item(73), Item(77), Item(96)], Add(2), 17, 4, 6),
        Monkey(4, [Item(75), Item(80), Item(50), Item(73), Item(88)], Add(3), 5, 6, 0),
        Monkey(5, [Item(59), Item(72), Item(99), Item(87), Item(91), Item(81)], MultiplyBy(17), 11, 2, 3),
        Monkey(6, [Item(86), Item(69)], Add(6), 3, 1, 0),
        Monkey(7, [Item(91)], Add(1), 19, 2, 5),
    ]


if __name__ == '__main__':
    input_lines = read_input()
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
    # 55458, 14508081294
