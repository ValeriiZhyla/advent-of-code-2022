class Operation:

    def apply(self, x: int) -> int:
        return x


class Add(Operation):
    value: int = 0

    def __init__(self, value_to_add: int):
        self.value = value_to_add

    def apply(self, x: int) -> int:
        return x + self.value


class MultiplyBy(Operation):
    value: int = 0

    def __init__(self, factor: int):
        self.value = factor

    def apply(self, x: int) -> int:
        return x * self.value


class Square(Operation):
    def apply(self, x: int) -> int:
        return x * x
