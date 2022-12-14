from .path import Path
from .coordinate import Coordinate

from copy import deepcopy


class PathFinder:
    all_valid_unique_paths_from_S_to_E: list[Path] = []
    grid_description: list[str]

    min_width = 0
    min_height = 0
    max_width = 0
    max_height = 0

    start_point_position = None
    end_point_position = None
    START_POINT_NAME = "S"
    END_POINT_NAME = "E"

    START_POINT_ELEVATION: str = "a"
    END_POINT_ELEVATION: str = "z"

    def __init__(self, lines: list[str]):
        self.all_valid_unique_paths_from_S_to_E = []
        self.grid_description = lines
        assert self.grid_description != []
        self.min_width = 0
        self.min_height = 0
        self.max_width = len(lines[0]) - 1
        self.max_height = len(lines) - 1
        for y in range(0, len(lines)):
            row = lines[y]
            for x in range(0, len(row)):
                if row[x] == self.END_POINT_NAME:
                    self.end_point_position = Coordinate(x, y)
                if row[x] == self.START_POINT_NAME:
                    self.start_point_position = Coordinate(x, y)

    def calculate_shortest_path_length_from_start_to_end(self) -> int:
        starting_point = self.start_point_position
        path = Path()
        path.add_point(starting_point)
        all_unique_paths_from_start_point = self.calculate_all_possible_unique_paths(starting_point, path)
        all_paths_with_end_point = self.find_paths_with_end_point(all_unique_paths_from_start_point)
        return self.find_minimal_steps_until_end_point(all_paths_with_end_point)

    def calculate_all_possible_unique_paths(self, point: Coordinate, current_path: Path) -> list[Path]:
        if self.is_end_point(point):
           return [current_path]
        print(f"Calculating paths from ({point.x},{point.y})...")
        paths_from_right = []
        paths_from_left = []
        paths_from_top = []
        paths_from_bottom = []
        # TODO ADD more memoisation
        if point.x < self.max_width:
            right_point = Coordinate(point.x + 1, point.y)
            if not current_path.point_is_already_visited(right_point):
                if self.step_is_possible(point, right_point):
                    path = deepcopy(current_path)
                    path.add_point(right_point)
                    paths_from_right = self.calculate_all_possible_unique_paths(right_point, path)
        if point.x > self.min_width:
            left_point = Coordinate(point.x - 1, point.y)
            if not current_path.point_is_already_visited(left_point):
                if self.step_is_possible(point, left_point):
                    path = deepcopy(current_path)
                    path.add_point(left_point)
                    paths_from_left = self.calculate_all_possible_unique_paths(left_point, path)
        if point.y < self.max_height:
            upper_point = Coordinate(point.x, point.y + 1)
            if not current_path.point_is_already_visited(upper_point):
                if self.step_is_possible(point, upper_point):
                    path = deepcopy(current_path)
                    path.add_point(upper_point)
                    paths_from_top = self.calculate_all_possible_unique_paths(upper_point, path)
        if point.y > self.min_height:
            bottom_point = Coordinate(point.x, point.y - 1)
            if not current_path.point_is_already_visited(bottom_point):
                if self.step_is_possible(point, bottom_point):
                    path = deepcopy(current_path)
                    path.add_point(bottom_point)
                    paths_from_bottom = self.calculate_all_possible_unique_paths(bottom_point, path)
        all_paths = paths_from_right + paths_from_left + paths_from_top + paths_from_bottom
        all_paths_with_end_point = self.find_paths_with_end_point(all_paths)
        if all_paths_with_end_point == []:
            return [current_path]
        return all_paths_with_end_point

    def is_end_point(self, point: Coordinate):
        return self.grid_description[point.y][point.x] == self.END_POINT_NAME

    def get_elevation(self, point: Coordinate):
        elevation = self.grid_description[point.y][point.x]
        if elevation == self.START_POINT_NAME:
            elevation = self.START_POINT_ELEVATION
        if elevation == self.END_POINT_NAME:
            elevation = self.END_POINT_ELEVATION
        return elevation

    def step_is_possible(self, point_from: Coordinate, point_to: Coordinate) -> bool:
        elevation_from = self.get_elevation(point_from)
        elevation_to = self.get_elevation(point_to)
        return abs(ord(elevation_from) - ord(elevation_to)) <= 1

    def find_paths_with_end_point(self, unique_paths: list[Path]) -> list[Path]:
        paths_with_end_point = []
        for path in unique_paths:
            if path.point_is_already_visited(self.end_point_position):
                paths_with_end_point.append(path)
        return paths_with_end_point

    def find_minimal_steps_until_end_point(self, all_paths_with_end_point):
        return min(map(lambda path: path.steps_till_point(self.end_point_position), all_paths_with_end_point))



