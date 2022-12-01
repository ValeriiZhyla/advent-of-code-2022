from .Expedition import Expedition
from .Elf import Elf


class ExpeditionBuilder:
    DELIMITER: str = ""

    def create_expedition(self, provision_calories_list: list[str]) -> Expedition:
        elves = self.transform_list_of_provision_entries_to_elves(provision_calories_list)
        return Expedition(elves)

    def transform_list_of_provision_entries_to_elves(self, provision_calories_list):
        elves = []
        current_elf_provision = []
        while len(provision_calories_list) != 0:
            entry = provision_calories_list.pop(0)
            if entry != self.DELIMITER:
                current_elf_provision.append(int(entry))
            else:
                if len(current_elf_provision) == 0:
                    continue
                else:
                    elves.append(Elf(current_elf_provision))
                    current_elf_provision = []
        return elves
