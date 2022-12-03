from .prioritization_rules import PrioritizationRules


class PriorityCalculator:

    def calculate_total_priority_of_common_items_in_each_rucksack_half(self, rucksack_contents: list[str]) -> int:
        total_priority = 0
        for rucksack in rucksack_contents:
            (left_half, right_half) = self.split_rucksack_in_two_halves(rucksack)
            intersection = left_half.intersection(right_half)
            total_priority += PrioritizationRules().priority_of_set(intersection)
        return total_priority

    def calculate_total_priority_of_common_items_in_each_group(self, rucksack_contents: list[str]) -> int:
        total_priority = 0
        groups = self.transform_list_to_groups_with_three_members(rucksack_contents)
        for group in groups:
            common_items_of_group = self.find_commons_items_in_group_of_three(group)
            total_priority += PrioritizationRules().priority_of_set(common_items_of_group)
        return total_priority

    def split_rucksack_in_two_halves(self, rucksack: str) -> (str, str):
        n = len(rucksack)
        mid = int(n / 2)
        (l, r) = (rucksack[0:mid], rucksack[mid: n])
        assert (len(l) == len(r))
        (items_left, items_right) = (set(l), set(r))
        return items_left, items_right

    def transform_list_to_groups_with_three_members(self, list_to_transform):
        assert len(list_to_transform) % 3 == 0
        return [list_to_transform[i: i+3] for i in range(0, len(list_to_transform), 3)]

    def find_commons_items_in_group_of_three(self, group):
        assert len(group) == 3
        unique_items_of_each_member = list(map(lambda l: set(l), group))
        return unique_items_of_each_member[0].intersection(unique_items_of_each_member[1].intersection(unique_items_of_each_member[2]))
