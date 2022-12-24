from model.packet import Packet, PacketPair
from model.signal_parser import SignalParser
from model.signal_analyzer import SignalAnalyzer
from model.signal_protocol import SignalProtocol
from model.signal_reconstructor import SignalReconstructor


class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self):
        # Task 1
        pairs: list[PacketPair] = SignalParser().parse_signal_into_pairs(self.input)
        filtered_pairs: list[PacketPair] = SignalAnalyzer().filter_pairs_with_right_order(pairs)
        index_sum_of_correct_pairs = sum(map(lambda pair: pair.index, filtered_pairs))

        # Task 2
        input_without_blank_lines: list[str] = self.get_input_lines_without_blank_lines()
        packets: list[Packet] = SignalParser().parse_signal_into_packets(input_without_blank_lines)
        packets_with_dividers: list[Packet] = SignalProtocol().add_divider_packets(packets)
        reconstructed_signal: list[Packet] = SignalReconstructor().reconstruct_signal(packets_with_dividers)
        decoder_key: int = SignalProtocol().calculate_decoder_key(reconstructed_signal)
        return index_sum_of_correct_pairs, decoder_key

    def get_input_lines_without_blank_lines(self) -> list[str]:
        return list(filter(lambda line: line != "", self.input))


def read_input() -> list[str]:
    input_file_name = 'input.txt'
    try:
        with open(input_file_name) as file:
            input_lines = file.readlines()
            if len(input_lines) == 0:
                raise Exception(f"File {input_file_name} is empty")
            input_lines_without_newline = [line.rstrip('\n') for line in input_lines]
            return input_lines_without_newline
    except EnvironmentError:
        raise Exception(f"File {input_file_name} is missing or invalid")


if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
    # 5557, 22425

