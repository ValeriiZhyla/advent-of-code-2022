from .point import Point


class Cave:
    rock_coordinates: set[Point] = set()
    sand_source: Point = None
    sand_in_rest_state_coordinates: set[Point] = set()

    ROCK_SYMBOL = "#"
    SAND_SOURCE_SYMBOL = "+"
    SAND_SYMBOL = "o"
    AIR_SYMBOL = "."

    LEFTMOST_FLOOR_X = -1000
    RIGHTMOST_FLOOR_X = 3000

    def __init__(self):
        self.last_simulation_terminated = True
        self.rock_coordinates = set()
        self.sand_source = None
        self.sand_in_rest_state_coordinates = set()

    def add_rock_path_between(self, path_start: Point, path_end: Point):
        if path_start.x == path_end.x:
            x = path_start.x
            start_y, end_y = min(path_start.y, path_end.y), max(path_start.y, path_end.y)
            points = [Point(x, y) for y in range(start_y, end_y + 1)]
            self.rock_coordinates = self.rock_coordinates.union(set(points))
        elif path_start.y == path_end.y:
            y = path_start.y
            start_x, end_x = min(path_start.x, path_end.x), max(path_start.x, path_end.x)
            points = [Point(x, y) for x in range(start_x, end_x + 1)]
            self.rock_coordinates = self.rock_coordinates.union(set(points))
        else:
            raise Exception("Unexpected topology")

    def print(self):
        min_x, max_x = min(map(lambda point: point.x, self.all_filled_coordinates())), max(map(lambda point: point.x, self.all_filled_coordinates()))
        min_y, max_y = min(map(lambda point: point.y, self.all_filled_coordinates())), max(map(lambda point: point.y, self.all_filled_coordinates()))

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if Point(x, y) in self.rock_coordinates:
                    print(self.ROCK_SYMBOL, end="")
                elif Point(x, y) == self.sand_source and self.sand_source not in self.sand_in_rest_state_coordinates:
                    print(self.SAND_SOURCE_SYMBOL, end="")
                elif Point(x, y) in self.sand_in_rest_state_coordinates:
                    print(self.SAND_SYMBOL, end="")
                else:
                    print(self.AIR_SYMBOL, end="")
            print()
        print("=====================================")

    def add_sand_source(self, sand_source: Point):
        self.sand_source = sand_source

    def point_is_in_all_filled_coordinates(self, point: Point) -> bool:
        return point == self.sand_source or point in self.rock_coordinates or point in self.sand_in_rest_state_coordinates

    def all_filled_coordinates(self):
        all = self.rock_coordinates.union(self.sand_in_rest_state_coordinates)
        all.add(self.sand_source)
        return all

    def amount_of_sand_in_rest_state(self):
        return len(self.sand_in_rest_state_coordinates)

    def perform_simulation_round(self) -> bool:
        """
        :return: True if sand unit stays still at the end. False if it falls into abyss.
        """
        new_sand_unit = Point(self.sand_source.x, self.sand_source.y)
        return self.simulate_sand_unit(new_sand_unit)

    def simulate_sand_unit(self, sand_unit: Point) -> bool:
        """
        :return: True if simulation terminated. False if sand unit falls into abyss or blocks the source.
        """
        abyss_level_y = max(map(lambda point: point.y, self.all_filled_coordinates())) + 1
        current_sand_coordinate: Point = sand_unit
        while current_sand_coordinate.y < abyss_level_y:
            if self.has_air_beneath(current_sand_coordinate):
                current_sand_coordinate = Point(current_sand_coordinate.x, current_sand_coordinate.y + 1)
            elif self.has_air_beneath_left(current_sand_coordinate):
                current_sand_coordinate = Point(current_sand_coordinate.x - 1, current_sand_coordinate.y + 1)
            elif self.has_air_beneath_right(current_sand_coordinate):
                current_sand_coordinate = Point(current_sand_coordinate.x + 1, current_sand_coordinate.y + 1)
            elif current_sand_coordinate == self.sand_source and not self.move_is_possible(current_sand_coordinate):
                self.sand_in_rest_state_coordinates.add(current_sand_coordinate)
                # self.print()
                return False
            else:
                self.sand_in_rest_state_coordinates.add(current_sand_coordinate)
                # self.print()
                return True
        return False

    def has_air_beneath(self, original_point: Point) -> bool:
        return not self.point_is_in_all_filled_coordinates(Point(original_point.x, original_point.y + 1))

    def has_air_beneath_right(self, original_point: Point) -> bool:
        return not self.point_is_in_all_filled_coordinates(Point(original_point.x + 1, original_point.y + 1))

    def has_air_beneath_left(self, original_point: Point) -> bool:
        return not self.point_is_in_all_filled_coordinates(Point(original_point.x - 1, original_point.y + 1))

    def add_floor(self):
        floor_level_y = max(map(lambda point: point.y, self.all_filled_coordinates())) + 2
        self.add_rock_path_between(Point(self.LEFTMOST_FLOOR_X, floor_level_y), Point(self.RIGHTMOST_FLOOR_X, floor_level_y))

    def move_is_possible(self, current_sand_coordinate):
        return self.has_air_beneath(current_sand_coordinate) or self.has_air_beneath_left(current_sand_coordinate) or self.has_air_beneath_right(current_sand_coordinate)
