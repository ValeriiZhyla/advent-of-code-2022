import json
from .packet import Packet, PacketPair


class SignalParser:
    def parse_signal_into_pairs(self, lines: list[str]) -> list[PacketPair]:
        pairs: list[PacketPair] = []
        for i in range(0, int(len(lines) / 3) + 1):
            line_first_packet = lines[i * 3]
            line_second_packet = lines[i * 3 + 1]
            pairs.append(PacketPair(i + 1, Packet(json.loads(line_first_packet)), Packet(json.loads(line_second_packet))))
        return pairs

    def parse_signal_into_packets(self, lines: list[str]) -> list[Packet]:
        packets: list[Packet] = []
        for line in lines:
            packets.append(Packet(json.loads(line)))
        return packets
