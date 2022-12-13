from .monkey import Monkey


class MonkeyInteraction:
    monkeys: list[Monkey] = []

    WORRY_LEVEL_DIVISOR_AFTER_OPERATION_SHORT = 3
    WORRY_LEVEL_DIVISOR_AFTER_OPERATION_LONG = 1

    def __init__(self, monkeys: list[Monkey]):
        self.monkeys = monkeys

    def perform_rounds(self, rounds_count: int):
        for i in range(0, rounds_count):
            self.perform_one_round()
            self.print_round_results(i)

    def get_monkey_business(self):
        inspections_of_each_monkey: list[int] = list(map(lambda monkey: monkey.count_of_items_inspected, self.monkeys))
        inspections_of_each_monkey.sort(reverse=True)
        assert len(inspections_of_each_monkey) >= 2
        return inspections_of_each_monkey[0] * inspections_of_each_monkey[1]

    def perform_one_round(self):
        for monkey in self.monkeys:
            monkey.inspect_items_and_throw_to_other_monkeys_simple(self.monkeys, self.WORRY_LEVEL_DIVISOR_AFTER_OPERATION_SHORT)

    def print_round_results(self, round_id):
        print(f"After round {round_id + 1}, the monkeys are holding items with these worry levels:")
        for monkey in self.monkeys:
            print(f"Monkey {monkey.id}: {list(map(lambda item: item.apply_all_operations_and_get_value(), monkey.items))}")
        print()


class MonkeyInteractionLong(MonkeyInteraction):
    def perform_one_round(self):
        for monkey in self.monkeys:
            monkey.inspect_items_and_throw_to_other_monkeys_optimized(self.monkeys, self.WORRY_LEVEL_DIVISOR_AFTER_OPERATION_LONG)

    def print_round_results(self, round_id):
        print(f"== After round {round_id + 1} ==")
        for monkey in self.monkeys:
            # print(f"Monkey {monkey.id} inspected items {str(monkey.count_of_items_inspected)}")
            print(f"Monkey {monkey.id} inspected items {str(monkey.count_of_items_inspected)}, items: {str(monkey.items)}")

        print()
