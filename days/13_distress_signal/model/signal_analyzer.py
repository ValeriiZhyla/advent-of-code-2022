from .packet import PacketPair


class SignalAnalyzer:
    def filter_pairs_with_right_order(self, pairs: list[PacketPair]) -> list[PacketPair]:
        return list(filter(lambda pair: pair.has_right_order(), pairs))
