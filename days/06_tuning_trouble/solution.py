from model.communication_device import CommunicationDevice


class Solution:
    original_datastream = []

    def __init__(self, input):
        self.original_datastream = input[0]

    def solve(self) -> (int,int):
        # first task
        first_index_after_start_marker = CommunicationDevice(self.original_datastream).find_start_of_packet()
        # second task
        first_index_after_message_marker = CommunicationDevice(self.original_datastream).find_start_of_message()

        return first_index_after_start_marker, first_index_after_message_marker


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
    # 1855, 3256
