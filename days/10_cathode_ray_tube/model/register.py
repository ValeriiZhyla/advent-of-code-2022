class Register:
    value: int = 1

    def __init__(self, staring_value: int):
        self.value = staring_value

    def perform_add(self, summand: int):
        self.value += summand
