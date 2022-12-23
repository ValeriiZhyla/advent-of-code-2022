import json
from .pair import PacketPair
class SignalParser:
    def parse_signal(self, lines: list[str]) -> list[PacketPair]:
        pairs: list[PacketPair] = []
        for i in range(0, int(len(lines)/3) + 1):
            line_first_packet = lines[i*3]
            line_second_packet = lines[i*3 + 1]
            pairs.append(PacketPair(json.loads(line_first_packet), json.loads(line_second_packet)))
        return pairs

