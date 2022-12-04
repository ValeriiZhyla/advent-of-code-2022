from .cleaning_pair import CleaningPair


class OverlapCalculator:
    def find_amount_of_pairs_with_full_overlap(self, pairs: list[CleaningPair]):
        pairs_with_full_overlap = 0
        for pair in pairs:
            if self.full_overlap(pair.sections_first, pair.sections_second):
                pairs_with_full_overlap += 1
        return pairs_with_full_overlap

    def find_amount_of_pairs_with_partial_overlap(self, pairs: list[CleaningPair]):
        pairs_with_partial_overlap = 0
        for pair in pairs:
            if self.partial_overlap(pair.sections_first, pair.sections_second):
                pairs_with_partial_overlap += 1
        return pairs_with_partial_overlap

    def full_overlap(self, sections_first, sections_second):
        return all(elem in sections_second for elem in sections_first) or all(elem in sections_first for elem in sections_second)

    def partial_overlap(self, sections_first, sections_second):
        return any(elem in sections_second for elem in sections_first) or any(elem in sections_first for elem in sections_second)
