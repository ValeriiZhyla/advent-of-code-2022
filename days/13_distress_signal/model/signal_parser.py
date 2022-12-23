import json
from .pair import PacketPair
from .packet import Packet

class SignalParser:
    def parse_signal(self, lines: list[str]) -> list[PacketPair]:
        pairs: list[PacketPair] = []
        for i in range(0, int(len(lines)/3) + 1):
            line_first_packet = lines[i*3]
            line_second_packet = lines[i*3 + 1]
            pairs.append(PacketPair(i+1, Packet(json.loads(line_first_packet)), Packet(json.loads(line_second_packet))))
        return pairs

