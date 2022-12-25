from .sensor import Sensor
from .point import Point

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
        coverage = self.calculate_coverage_full()
        min_x = min(map(lambda point: point.x, coverage))
        max_x = max(map(lambda point: point.x, coverage))
        min_y = min(map(lambda point: point.y, coverage))
        max_y = max(map(lambda point: point.y, coverage))
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

    def print_map_with_coverage_line(self, row):
        coverage = self.calculate_coverage_for_one_row(row)
        min_x = min(map(lambda point: point.x, coverage))
        max_x = max(map(lambda point: point.x, coverage))
        min_y = min(map(lambda point: point.y, coverage))
        max_y = max(map(lambda point: point.y, coverage))
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

    def calculate_coverage_full(self) -> set[Point]:
        coverage: set[Point] = set()
        for sensor in self.sensors:
            possible_x = [x for x in range(sensor.sensor_coordinate.x - sensor.manhattan_distance, sensor.sensor_coordinate.x + sensor.manhattan_distance)]
            possible_y = [y for y in range(sensor.sensor_coordinate.y - sensor.manhattan_distance, sensor.sensor_coordinate.y + sensor.manhattan_distance)]

            sensor_coverage_square = set([Point(x, y) for (x, y) in itertools.product(possible_x, possible_y)])
            sensor_coverage_circle = set(filter(lambda point: point.calculate_manhattan_distance_to(sensor.sensor_coordinate) <= sensor.manhattan_distance , sensor_coverage_square))
            coverage = coverage.union(sensor_coverage_circle)
        return coverage

    def calculate_coverage_for_one_row(self, row: int) -> set[Point]:
        coverage: set[Point] = set()
        sensors_to_check = list(filter(lambda sensor: row in range(sensor.sensor_coordinate.y - sensor.manhattan_distance, sensor.sensor_coordinate.y + sensor.manhattan_distance + 1) ,self.sensors))
        i = 0
        for sensor in sensors_to_check:
            sensor_line = set([Point(x, row) for x in range(sensor.sensor_coordinate.x - sensor.manhattan_distance, sensor.sensor_coordinate.x + sensor.manhattan_distance + 1)])
            sensor_line_coverage = set(filter(lambda point: point.calculate_manhattan_distance_to(sensor.sensor_coordinate) <= sensor.manhattan_distance , sensor_line))

            #possible_x = [x for x in range(sensor.sensor_coordinate.x - sensor.manhattan_distance, sensor.sensor_coordinate.x + sensor.manhattan_distance + 1)]
            #possible_y = [row]
            #sensor_coverage_line = set([Point(x, y) for (x, y) in itertools.product(possible_x, possible_y)])
            coverage = coverage.union(sensor_line_coverage)
            i += 1
            print(f"Sensor {i} out {len(sensors_to_check)} processed")
        return coverage

    def amount_of_positions_where_a_beacon_cannot_be_present_in_row(self, row: int) -> int:
        return len(self.calculate_coverage_for_one_row(row)) - len(list(filter(lambda beacon: beacon.y == row, self.beacon_positions)))
