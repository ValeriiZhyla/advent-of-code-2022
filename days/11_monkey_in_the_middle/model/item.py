from .operation import Operation, Add, Square, MultiplyBy


class Item:
    default_worry_level: int = 0
    applied_operations: list[Operation] = []

    def __init__(self, worry_level: int):
        self.default_worry_level = 0
        self.applied_operations = [Add(worry_level)]

    def add_operation(self, operation: Operation):
        self.applied_operations.append(operation)

    def apply_all_operations_and_get_value(self):
        current_value = self.default_worry_level
        for operation in self.applied_operations:
            current_value = operation.apply(current_value)
        return current_value

    def is_divisible_by(self, test_divisor: int) -> bool:
        return self.calculate_modulo_residuum(self.default_worry_level, self.applied_operations, test_divisor) == 0

    def calculate_modulo_residuum(self, original: int, operations: list[Operation], modulus: int) -> int:
        if len(operations) == 1:
            operation = operations[-1]
            if isinstance(operation, Add):
                return operation.value % modulus
            else:
                raise Exception("Initialization error")
        else:
            operation = operations[-1]
            if isinstance(operation, Square):
                a = self.calculate_modulo_residuum(original, operations[:-1], modulus)
                return (a * a) % modulus
            elif isinstance(operation, MultiplyBy):
                factor = operation.value
                if factor % modulus == 0:
                    return 0
                else:
                    return (self.calculate_modulo_residuum(original, operations[:-1], modulus) * (factor % modulus)) % modulus
            elif isinstance(operation, Add):
                summand = operation.value
                return (self.calculate_modulo_residuum(original, operations[:-1], modulus) + summand % modulus) % modulus
