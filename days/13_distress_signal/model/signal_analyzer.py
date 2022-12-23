from .pair import PacketPair


class SignalAnalyzer:
    def filter_pairs_with_right_order(self, pairs: list[PacketPair]) -> list[PacketPair]:
        for pair in pairs:
            print(pair.index, pair.has_right_order())

        return list(filter(lambda pair: pair.has_right_order(), pairs))
