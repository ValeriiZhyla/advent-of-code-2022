from .operation import Operation


class Item:
    original_worry_level: int = 0
    applied_operations: list[Operation] = []

    def __init__(self, worry_level: int):
        self.original_worry_level = worry_level

    def add_operation(self, operation: Operation):
        self.applied_operations.append(operation)

    def apply_all_operations_and_get_value(self):
        current_value = self.original_worry_level
        for operation in self.applied_operations:
            current_value = operation.apply(current_value)
        return current_value
