from .point import Point

class Cave:
    rock_coordinates: set[Point] = set()
    sand_sources_coordinates: set[Point] = set()
    sand_in_rest_state_coordinates: set[Point] = set()

    ROCK_SYMBOL = "#"
    SAND_SOURCE_SYMBOL = "+"
    SAND_SYMBOL = "o"
    AIR_SYMBOL = "."

    def __init__(self):
        self.last_simulation_terminated = True
        self.rock_coordinates = set()
        self.sand_sources_coordinates = set()
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
                elif Point(x, y) in self.sand_sources_coordinates:
                    print(self.SAND_SOURCE_SYMBOL, end="")
                elif Point(x, y) in self.sand_in_rest_state_coordinates:
                    print(self.SAND_SYMBOL, end="")
                else:
                    print(self.AIR_SYMBOL, end="")
            print()
        print("=====================================")

    def add_sand_source(self, sand_source: Point):
        self.sand_sources_coordinates.add(sand_source)

    def all_filled_coordinates(self) -> set[Point]:
        return self.rock_coordinates.union(self.sand_sources_coordinates.union(self.sand_in_rest_state_coordinates))

    def amount_of_sand_in_rest_state(self):
        return len(self.sand_in_rest_state_coordinates)

    def perform_simulation_round(self) -> bool:
        """
        :return: True if sand unit stays still at the end. False if it falls into abyss.
        """
        simulation_results = []
        for sand_source in self.sand_sources_coordinates:
            if self.has_air_beneath(sand_source):
                new_sand_unit = Point(sand_source.x, sand_source.y + 1)
                simulation_results.append(self.simulate_sand_unit(new_sand_unit))
            else:
                simulation_results.append(False)
        return all(simulation_results)

    def simulate_sand_unit(self, sand_unit: Point) -> bool:
        """
        :return: True if simulation terminated. False if sand unit falls into abyss.
        """
        abyss_level_y = max(map(lambda point: point.y, self.all_filled_coordinates())) + 1
        current_sand_coordinate: Point = sand_unit
        while current_sand_coordinate.y < abyss_level_y:
            #self.print()
            if self.has_air_beneath(current_sand_coordinate):
                current_sand_coordinate = Point(current_sand_coordinate.x, current_sand_coordinate.y + 1)
            elif self.has_air_beneath_left(current_sand_coordinate):
                current_sand_coordinate = Point(current_sand_coordinate.x - 1, current_sand_coordinate.y + 1)
            elif self.has_air_beneath_right(current_sand_coordinate):
                current_sand_coordinate = Point(current_sand_coordinate.x + 1, current_sand_coordinate.y + 1)
            else:
                self.sand_in_rest_state_coordinates.add(current_sand_coordinate)
                return True
        return False

    def has_air_beneath(self, original_point: Point) -> bool:
        return Point(original_point.x, original_point.y + 1) not in self.all_filled_coordinates()

    def has_air_beneath_right(self, original_point: Point) -> bool:
        return Point(original_point.x + 1, original_point.y + 1) not in self.all_filled_coordinates()

    def has_air_beneath_left(self, original_point: Point) -> bool:
        return Point(original_point.x - 1, original_point.y + 1) not in self.all_filled_coordinates()
