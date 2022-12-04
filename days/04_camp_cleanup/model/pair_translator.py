from .cleaning_pair import CleaningPair


class PairTranslator:
    PAIR_DELIMITER = ","
    INTERVAL_DELIMITER = "-"

    def transform_input_to_list_of_pairs(self, input_pairs: list[str]) -> list[CleaningPair]:
        pairs: list[CleaningPair] = []
        for pair_line in input_pairs:
            pairs_ranges_text = pair_line.split(self.PAIR_DELIMITER)
            assert len(pairs_ranges_text) == 2
            interval_fst = self.range_from_interval_notation(pairs_ranges_text[0])
            interval_snd = self.range_from_interval_notation(pairs_ranges_text[1])
            pairs.append(CleaningPair(interval_fst, interval_snd))
        return pairs

    def range_from_interval_notation(self, interval: str) -> list[int]:
        interval_boundaries = interval.split(self.INTERVAL_DELIMITER)
        assert len(interval_boundaries) == 2
        start_idx = int(interval_boundaries[0])
        end_idx = int(interval_boundaries[1])
        return list(range(start_idx, end_idx + 1, 1))
