from .operation import Operation, Add, Square, MultiplyBy


class Item:
    default_worry_level: int = 0
    applied_operations: list[Operation] = []
    # save known divisors to optimize recursion
    # dict[operation_index, dict[modulus, residual]]
    known_divisors: dict[int, dict[int, int]] = {}

    def __init__(self, worry_level: int):
        self.default_worry_level = 0
        self.applied_operations = [Add(worry_level)]
        self.known_divisors = {}

    def add_operation(self, operation: Operation):
        self.applied_operations.append(operation)

    def apply_all_operations_and_get_value(self):
        current_value = self.default_worry_level
        for operation in self.applied_operations:
            current_value = operation.apply(current_value)
        return current_value

    def is_divisible_by(self, test_divisor: int) -> bool:
        assert self.applied_operations != []
        last_operation_index = len(self.applied_operations) - 1
        return self.calculate_modulo_residual(self.default_worry_level, last_operation_index, test_divisor) == 0

    def calculate_modulo_residual(self, original: int, current_operation_index: int, modulus: int) -> int:
        # check cache
        if self.modulus_is_in_list_of_divisors_for_current_operation(current_operation_index, modulus):
            return self.known_divisors[current_operation_index].get(modulus)
        # perform calculations and fill cache
        if current_operation_index == 0:
            # case very first entry
            operation = self.applied_operations[current_operation_index]
            if isinstance(operation, Add):
                residual = operation.value % modulus
                self.add_cache_entry(current_operation_index, modulus, residual)
                return operation.value % modulus
            else:
                raise Exception("Initialization error")
        else:
            # normal case
            operation = self.applied_operations[current_operation_index]
            if isinstance(operation, Square):
                a = self.calculate_modulo_residual(original, current_operation_index - 1, modulus)
                residual = (a * a) % modulus
                self.add_cache_entry(current_operation_index, modulus, residual)
                return residual
            elif isinstance(operation, MultiplyBy):
                factor = operation.value
                residual = (self.calculate_modulo_residual(original, current_operation_index - 1, modulus) * (factor % modulus)) % modulus
                self.add_cache_entry(current_operation_index, modulus, residual)
                return residual
            elif isinstance(operation, Add):
                summand = operation.value
                residual = (self.calculate_modulo_residual(original, current_operation_index - 1, modulus) + summand % modulus) % modulus
                self.add_cache_entry(current_operation_index, modulus, residual)
                return residual

    def modulus_is_in_list_of_divisors_for_current_operation(self, current_operation_index: int, modulus: int) -> bool:
        if current_operation_index in self.known_divisors.keys():
            if modulus in self.known_divisors.get(current_operation_index):
                return True

    def add_cache_entry(self, current_operation_index, modulus, residual):
        if current_operation_index not in self.known_divisors.keys():
            self.known_divisors[current_operation_index] = {modulus: residual}
        else:
            self.known_divisors[current_operation_index][modulus] = residual
