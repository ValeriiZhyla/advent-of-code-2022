from typing import Callable
from .item import Item
from .operation import Operation, DivideBy

class Monkey:
    id: int = 0
    count_of_items_inspected: int = 0
    items: list[Item] = []
    operation: Operation = None
    test_divisor: int = 1
    if_test_true_throw_to_monkey_with_id: int = 0
    if_test_false_throw_to_monkey_with_id: int = 0

    def __init__(self, id: int, starting_items: list[Item],
                 operation: Operation, test_divisor: int,
                 if_test_true_throw_to_monkey_with_id: int, if_test_false_throw_to_monkey_with_id: int):
        self.id = id
        self.items = starting_items
        self.count_of_items_inspected = 0
        self.operation = operation
        self.test_divisor = test_divisor
        self.if_test_true_throw_to_monkey_with_id = if_test_true_throw_to_monkey_with_id
        self.if_test_false_throw_to_monkey_with_id = if_test_false_throw_to_monkey_with_id

    def inspect_items_and_throw_to_other_monkeys_simple(self, monkeys: list['Monkey'], worry_level_divisor_rules: int):
        while self.items != []:
            item = self.items.pop(0)
            item.add_operation(self.operation)
            worry_level = item.apply_all_operations_and_get_value()

            worry_level_bored = int(worry_level / worry_level_divisor_rules)
            item.add_operation(DivideBy(worry_level_divisor_rules))

            if worry_level_bored % self.test_divisor == 0:
                self.throw_to_monkey(item, self.if_test_true_throw_to_monkey_with_id, monkeys)
            else:
                self.throw_to_monkey(item, self.if_test_false_throw_to_monkey_with_id, monkeys)
            self.count_of_items_inspected += 1

    def inspect_items_and_throw_to_other_monkeys_optimized(self, monkeys: list['Monkey'], worry_level_divisor_rules: int):
        if worry_level_divisor_rules > 1:
            return self.inspect_items_and_throw_to_other_monkeys_simple(monkeys, worry_level_divisor_rules)
        if worry_level_divisor_rules == 1:
            while self.items != []:
                item = self.items.pop(0)
                item.add_operation(self.operation)
                if item.is_divisible_by(self.test_divisor):
                    self.throw_to_monkey(item, self.if_test_true_throw_to_monkey_with_id, monkeys)
                else:
                    self.throw_to_monkey(item, self.if_test_false_throw_to_monkey_with_id, monkeys)
                self.count_of_items_inspected += 1
        else:
            raise Exception(f"No optimization for factor {worry_level_divisor_rules}")

    def throw_to_monkey(self, item: Item, target_monkey_id: int, monkeys: list['Monkey']):
        target_list = list(filter(lambda monkey: monkey.id == target_monkey_id, monkeys))
        if len(target_list) != 1:
            raise Exception(f"Monkey with id {target_monkey_id} does not exist!")
        else:
            target_list[0].add_item(item)

    def add_item(self, item: Item):
        self.items.append(item)





