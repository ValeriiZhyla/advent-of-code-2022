from model.sensor import Sensor
from model.sensor_report_parser import SensorReportParser
from model.coverage_map import CoverageMap

FULL_INPUT = "input.txt"
TEST_INPUT = "small_input.txt"


class Solution:
    input = []

    def __init__(self, input):
        self.input = input

    def solve(self):
        # Task 1
        sensors: list[Sensor] = SensorReportParser().parse(self.input)
        beacon_coverage_map: CoverageMap = CoverageMap(sensors)
        sample_covered_positions = beacon_coverage_map.amount_of_positions_where_a_beacon_cannot_be_present_in_row(2000000)
        print("Task 1 completed")
        # Task 2
        tuning_frequency_of_beacon = beacon_coverage_map.calculate_tuning_frequency_of_distress_beacon(4000000)
        return sample_covered_positions, tuning_frequency_of_beacon


def read_input() -> list[str]:
    input_file_name = FULL_INPUT
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
    # 4748135, 13743542639657
