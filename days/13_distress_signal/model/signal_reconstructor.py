from .packet import Packet


class SignalReconstructor:
    def reconstruct_signal(self, packets_with_dividers: list[Packet]) -> list[Packet]:
        reordered_packets = sorted(packets_with_dividers)
        return reordered_packets
