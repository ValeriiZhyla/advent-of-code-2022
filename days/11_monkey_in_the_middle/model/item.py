from .operation import Operation, Add, Square, MultiplyBy


class Item:
    original_worry_level: int = 0
    applied_operations: list[Operation] = []

    def __init__(self, worry_level: int):
        self.original_worry_level = worry_level
        self.applied_operations = []

    def add_operation(self, operation: Operation):
        self.applied_operations.append(operation)

    def apply_all_operations_and_get_value(self):
        current_value = self.original_worry_level
        for operation in self.applied_operations:
            current_value = operation.apply(current_value)
        return current_value

    def is_divisible_by(self, test_divisor: int) -> bool:
        assert self.original_worry_level != 0
        current_value = self.original_worry_level
        if current_value % test_divisor == 0:
            return True
        else:
            for operation in reversed(self.applied_operations):
                if isinstance(operation, Square):
                    continue
                elif isinstance(operation, MultiplyBy):
                    factor = operation.value
                    if factor % test_divisor == 0:
                        return True
                elif isinstance(operation, Add):
                    return self.apply_all_operations_and_get_value() % test_divisor == 0
        return self.apply_all_operations_and_get_value() % test_divisor == 0
