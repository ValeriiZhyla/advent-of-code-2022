from model.directory import Directory, RootDirectory
from model.disk_structure_parser import DiskStructureParser
from model.file_system_analyzer import FileSystemAnalyzer

class Solution:
    console_output = []
    DIRECTORY_TOTAL_SIZE_THRESHOLD = 100000
    TOTAL_SPACE_SIZE = 70000000
    REQUIRED_SPACE = 30000000

    def __init__(self, input):
        self.console_output = input

    def solve(self) -> (int, int):
        root_directory: Directory = DiskStructureParser().create_file_system_structure_from_console_lines(self.console_output)
        # task 1
        total_size_of_small_directories = FileSystemAnalyzer().get_total_size_of_directories_with_size_less_or_equal_than(root_directory, self.DIRECTORY_TOTAL_SIZE_THRESHOLD)
        # task 2
        size_of_smallest_directory_to_delete = FileSystemAnalyzer().get_size_of_smallest_directory_to_delete_for_update(root_directory, self.TOTAL_SPACE_SIZE, self.REQUIRED_SPACE)
        return total_size_of_small_directories, size_of_smallest_directory_to_delete



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
    # 1432936

