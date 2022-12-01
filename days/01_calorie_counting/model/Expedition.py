from . Elf import Elf


class Expedition:
    members: list[Elf] = []

    def __init__(self, members: list[Elf]):
        self.members = members

    def find_elf_carrying_most_calories(self) -> Elf:
        current_elf_with_most_calories = self.members[0]
        for elf in self.members:
            if elf.all_carried_calories() > current_elf_with_most_calories.all_carried_calories():
                current_elf_with_most_calories = elf
        return current_elf_with_most_calories

    def sum_of_top_tree_carriers(self) -> int:
        calories: list[int] = list(map(lambda elf: elf.all_carried_calories(), self.members))
        calories.sort()
        calories.reverse()
        return sum(calories[0:3])

    def calories_of_main_carrier(self) -> int:
        return self.find_elf_carrying_most_calories().all_carried_calories()
