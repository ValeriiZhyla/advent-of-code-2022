from .crate import Crate
import re


class Stack:
    crates_top_down: list[Crate] = []

    PATTERN_CRATE = r'\[(\w+)\]'

    def __init__(self, crates_list_text: list[str]):
        crates: list[Crate] = []
        for crate_description in crates_list_text:
            # "[N]", "[Z]"
            # -> ["N", "Z"]
            m = re.match(self.PATTERN_CRATE, crate_description)
            if m:
                crate_name = m.group(1)
                crates.append(Crate(crate_name))
            else:
                raise Exception(f"Crate [{crate_description}] does not match the expected pattern [{self.PATTERN_CRATE}]")
        self.crates_top_down = crates

    def take_top_crate(self) -> Crate:
        if self.crates_top_down == []:
            raise Exception("Stack is already empty, cant remove top element")
        return self.crates_top_down.pop(0)

    def place_new_crate_on_top(self, crate: Crate):
        self.crates_top_down.insert(0, crate)

    def get_top_crate_name(self) -> str:
        if self.crates_top_down  == []:
            return " "
        return self.crates_top_down[0].name
