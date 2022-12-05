from .stack import Stack


class StackDescriptionParser:
    SIZE_OF_CRATE_DESCRIPTION = 3
    SIZE_OF_INTERVAL = 1

    def stacks_description_to_stacks(self, stacks_description: list[str]) -> list[Stack]:
        assert stacks_description != []

        # last line contains information about element_amount
        amount_of_columns = self.get_amount_of_columns(stacks_description[-1])
        stacks_description = stacks_description[: -1]

        stacks_columns: list[list[str]] = []
        for i in range(0, amount_of_columns):
            stacks_columns.append([])
        for description_line in stacks_description:
            for i in range(0, amount_of_columns):
                entry: str = self.get_entry_from_column(description_line, i)
                if entry.replace(" ", "") != "":
                    stacks_columns[i].append(entry)
        stacks = []
        for stack_column in stacks_columns:
            stacks.append(Stack(stack_column))
        return stacks

    def get_amount_of_columns(self, line: str) -> int:
        return int(line.split()[-1])

    def get_entry_from_column(self, line: str, column_idx: int) -> str:
        # for column 0: return line[0:3]
        # for column 1: return line[4:7]
        # for column 2: return line[8:11]
        start = column_idx * (self.SIZE_OF_CRATE_DESCRIPTION + self.SIZE_OF_INTERVAL)
        end = column_idx * (self.SIZE_OF_CRATE_DESCRIPTION + self.SIZE_OF_INTERVAL) + self.SIZE_OF_CRATE_DESCRIPTION
        return line[start:end]
