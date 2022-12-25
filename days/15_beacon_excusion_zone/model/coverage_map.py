from .sensor import Sensor
from .point import Point
from .range import Range

import itertools


class CoverageMap:
    sensors: list[Sensor] = []
    sensor_positions: set[Point] = set()
    beacon_positions: set[Point] = set()

    BEACON_SYMBOL = "B"
    SENSOR_SYMBOL = "S"
    FREE_SYMBOL = "."
    COVERAGE_SYMBOL = "#"

    def __init__(self, sensors: list[Sensor]):
        self.sensors = sensors
        self.sensor_positions = set(map(lambda sensor: sensor.sensor_coordinate, self.sensors))
        self.beacon_positions = set(map(lambda sensor: sensor.closest_beacon_coordinate, self.sensors))

    def print_map_without_coverage(self):
        min_x = min(map(lambda sensor: min(sensor.sensor_coordinate.x, sensor.closest_beacon_coordinate.x), self.sensors))
        max_x = max(map(lambda sensor: max(sensor.sensor_coordinate.x, sensor.closest_beacon_coordinate.x), self.sensors))
        min_y = min(map(lambda sensor: min(sensor.sensor_coordinate.y, sensor.closest_beacon_coordinate.y), self.sensors))
        max_y = max(map(lambda sensor: max(sensor.sensor_coordinate.y, sensor.closest_beacon_coordinate.y), self.sensors))
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                point = Point(x, y)
                if point in self.sensor_positions:
                    print(self.SENSOR_SYMBOL, end="")
                elif point in self.beacon_positions:
                    print(self.BEACON_SYMBOL, end="")
                else:
                    print(self.FREE_SYMBOL, end="")
            print()

    def print_map_with_coverage(self):
        coverage: set[Range] = self.calculate_coverage_full()
        min_x = min(map(lambda range: range.start, coverage))
        max_x = max(map(lambda range: range.end, coverage))
        min_y = min(map(lambda range: range.row_number, coverage))
        max_y = max(map(lambda range: range.row_number, coverage))
        for y in range(min_y, max_y + 1):
            coverage_ranges_for_current_row: list[Range] = list(filter(lambda range: range.row_number == y, coverage))

            if y < 0:
                print(y, " ", end="")
            elif y < 10:
                print("", y, " ", end="")
            else:
                print(y, " ", end="")
            for x in range(min_x, max_x + 1):
                point = Point(x, y)
                if point in self.sensor_positions:
                    print(self.SENSOR_SYMBOL, end="")
                elif point in self.beacon_positions:
                    print(self.BEACON_SYMBOL, end="")
                elif self.row_coverage_contains_x(point.x, coverage_ranges_for_current_row) and point not in self.sensor_positions and point not in self.beacon_positions:
                    print(self.COVERAGE_SYMBOL, end="")
                else:
                    print(self.FREE_SYMBOL, end="")
            print()

    def print_map_with_coverage_line(self, row):
        coverage = self.calculate_coverage_for_one_row(row)
        min_x = min(map(lambda range: range.start, coverage))
        max_x = max(map(lambda range: range.end, coverage))
        min_y = min(map(lambda range: range.row_number, coverage))
        max_y = max(map(lambda range: range.row_number, coverage))
        for y in range(min_y, max_y + 1):
            if y < 0:
                print(y, " ", end="")
            elif y < 10:
                print("", y, " ", end="")
            else:
                print(y, " ", end="")
            for x in range(min_x, max_x + 1):
                point = Point(x, y)
                if point in self.sensor_positions:
                    print(self.SENSOR_SYMBOL, end="")
                elif point in self.beacon_positions:
                    print(self.BEACON_SYMBOL, end="")
                elif point in coverage and point not in self.sensor_positions and point not in self.beacon_positions:
                    print(self.COVERAGE_SYMBOL, end="")
                else:
                    print(self.FREE_SYMBOL, end="")
            print()

    def calculate_coverage_full(self) -> set[Range]:
        coverage: set[Range] = set()
        i = 0
        for sensor in self.sensors:
            possible_rows = [y for y in range(sensor.sensor_coordinate.y - sensor.manhattan_distance, sensor.sensor_coordinate.y + sensor.manhattan_distance)]
            for y in possible_rows:
                range_for_current_row = self.create_coverage_range_for_sensor_and_row(sensor, y)
                coverage.add(range_for_current_row)
            i += 1
            print(f"Sensor {i} out {len(self.sensors)} processed")
        return coverage

    def calculate_coverage_for_one_row(self, row: int) -> set[Range]:
        coverage: set[Range] = set()
        sensors_to_check = list(filter(lambda sensor: row in range(sensor.sensor_coordinate.y - sensor.manhattan_distance, sensor.sensor_coordinate.y + sensor.manhattan_distance + 1) ,self.sensors))
        i = 0
        for sensor in sensors_to_check:
            range_for_current_row = self.create_coverage_range_for_sensor_and_row(sensor, row)
            coverage.add(range_for_current_row)
            i += 1
            print(f"Sensor {i} out {len(sensors_to_check)} processed")
        return coverage

    def amount_of_positions_where_a_beacon_cannot_be_present_in_row(self, row: int) -> int:
        coverage_ranges_of_row = self.calculate_coverage_for_one_row(row)
        all_covered_x = set()
        for range in coverage_ranges_of_row:
            all_covered_x = all_covered_x.union(range.get_all_x_in_range())
        return len(all_covered_x) - len(list(filter(lambda beacon: beacon.y == row, self.beacon_positions)))

    def create_coverage_range_for_sensor_and_row(self, sensor: Sensor, row_number: int) -> Range:
        row_range_start = sensor.sensor_coordinate.x - (sensor.manhattan_distance - abs(sensor.sensor_coordinate.y - row_number))
        row_range_end = sensor.sensor_coordinate.x + (sensor.manhattan_distance - abs(sensor.sensor_coordinate.y - row_number))
        range_for_current_row = Range(row_number, row_range_start, row_range_end)
        return range_for_current_row

    def calculate_tuning_frequency_of_distress_beacon(self, coordinates_upper_bound):
        covered_positions: set[Point] = self.calculate_coverage_full()
        min_x = min(map(lambda point: point.x, covered_positions))
        max_x = max(map(lambda point: point.x, covered_positions))
        min_y = min(map(lambda point: point.y, covered_positions))
        max_y = max(map(lambda point: point.y, covered_positions))
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if Point(x, y) not in covered_positions and 0 <= x <= coordinates_upper_bound and 0 <= y <= coordinates_upper_bound:
                    return x * 4000000 + y
        raise Exception("Beacon not found")

    def row_coverage_contains_x(self, x: int, coverage_ranges_for_current_row: list[Range]) -> bool:
        for range in coverage_ranges_for_current_row:
            if range.contains_x(x):
                return True
        return False
