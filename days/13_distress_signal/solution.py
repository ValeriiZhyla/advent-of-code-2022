from model.pair import PacketPair
from model.signal_parser import SignalParser
from model.signal_analyzer import SignalAnalyzer

class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self):
        # Task 1
        pairs: list[PacketPair] = SignalParser().parse_signal(self.input)
        filtered_pairs: list[PacketPair] = SignalAnalyzer().filter_pairs_with_right_order(pairs)
        return sum(map(lambda pair: pair.index, filtered_pairs))


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
    # 5557

