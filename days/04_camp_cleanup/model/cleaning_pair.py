class CleaningPair:
    sections_first: list[int] = []
    sections_second: list[int] = []

    def __init__(self, fst: list[int], snd: list[int]):
        self.sections_first = fst
        self.sections_second = snd
