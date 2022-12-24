from .packet import Packet


class SignalProtocol:
    divider_packets: list[Packet] = [Packet([[2]]), Packet([[6]])]

    def add_divider_packets(self, original_packets: list[Packet]) -> list[Packet]:
        new_list: list[Packet] = original_packets.copy()
        new_list += self.divider_packets
        return new_list

    def calculate_decoder_key(self, reconstructed_signal: list[Packet]) -> int:
        decoder_key = 1
        for idx in range(1, len(reconstructed_signal) + 1):
            if reconstructed_signal[idx - 1] in self.divider_packets:
                decoder_key *= idx
        return decoder_key
