from .point import Point

class CaveStructure:
    rock_coordinates: set[Point] = set()

    ROCK_SYMBOL = "#"
    AIR_SYMBOL = "."

    def __init__(self):
        self.rock_coordinates = set()

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
        min_x, max_x = min(map(lambda point: point.x, self.rock_coordinates)), max(map(lambda point: point.x, self.rock_coordinates))
        min_y, max_y = min(map(lambda point: point.y, self.rock_coordinates)), max(map(lambda point: point.y, self.rock_coordinates))

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if Point(x, y) in self.rock_coordinates:
                    print(self.ROCK_SYMBOL, end="")
                else:
                    print(self.AIR_SYMBOL, end="")
            print()
        print("=====================================")



