class Elf:
    carried_provision: list[int] = []

    def __init__(self, elf_provision: list[int]):
        self.carried_provision = elf_provision

    def all_carried_calories(self) -> int:
        return sum(self.carried_provision)
