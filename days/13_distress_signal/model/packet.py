TRUE = 1
FALSE = -1
CONTINUE = 0

class Packet:
    data: list = []

    def __init__(self, data: list):
        self.data = data

    def __lt__(self, other):
        return PacketPair(0, self, other).has_right_order()


class PacketPair:
    index: int = 0
    fst: Packet = None
    snd: Packet = None

    def __init__(self, pair_index: int, first: Packet, second: Packet):
        self.index = pair_index
        self.fst = first
        self.snd = second

    def has_right_order(self) -> bool:
        return self.left_is_smaller_than_right(self.fst.data, self.snd.data) == TRUE

    def left_is_smaller_than_right(self, left, right) -> int:
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return CONTINUE
            if left < right:
                return TRUE
            if left > right:
                return FALSE
        if isinstance(left, list) and isinstance(right, list):
            if left == [] and right == []:
                return CONTINUE
            if left == [] and right != []:
                return TRUE
            if left != [] and right == []:
                return FALSE
            comparison_result = self.left_is_smaller_than_right(left[0], right[0])
            if comparison_result == CONTINUE:
                return self.left_is_smaller_than_right(left[1:], right[1:])
            else:
                return comparison_result
        if isinstance(left, int) and isinstance(right, list):
            return self.left_is_smaller_than_right([left], right)
        if isinstance(left, list) and isinstance(right, int):
            return self.left_is_smaller_than_right(left, [right])
