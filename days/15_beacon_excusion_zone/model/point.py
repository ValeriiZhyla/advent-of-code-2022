from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def calculate_manhattan_distance_to(self, other: 'Point') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

