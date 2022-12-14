from .coordinate import Coordinate


class Path:
    visited_positions: list[Coordinate] = []

    def __init__(self):
        self.visited_positions = []

    def point_is_already_visited(self, point: Coordinate) -> bool:
        for visited in self.visited_positions:
            if point == visited:
                return True
        return False

    def add_point(self, point: Coordinate):
        self.visited_positions.append(point)

    def steps_till_point(self, target_point: Coordinate):
        steps = 0
        for point in self.visited_positions:
            if point != target_point:
                steps += 1
            else:
                return steps
