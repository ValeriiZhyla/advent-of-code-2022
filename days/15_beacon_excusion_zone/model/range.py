class Range:
    row_number = 0
    start = 0
    end = 0

    def __init__(self, row: int, start: int, end: int):
        self.row_number = row
        self.start = start
        self.end = end

    def contains_x(self, x: int) -> bool:
        return self.start <= x <= self.end

    def get_all_x_in_range(self) -> set[int]:
        return set([x for x in range(self.start, self.end + 1)])

