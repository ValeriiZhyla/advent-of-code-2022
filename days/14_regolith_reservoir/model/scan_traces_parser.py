from .point import Point
from .cave import Cave

class ScanTracesParser:
    ENTRY_SPLIT = " -> "
    COORDINATE_SPLIT = ","

    def parse_cave_rock_structure(self, input: list[str]) -> Cave:
        cave = Cave()
        for line in input:
            points: list[Point] = self.get_all_points(line)
            for idx in range(0, len(points) - 1):
                cave.add_rock_path_between(points[idx], points[idx+1])
        return cave

    def get_all_points(self, line: str) -> list[Point]:
        entries = line.split(self.ENTRY_SPLIT)
        points: list[Point] = []
        for entry in entries:
            split = entry.split(self.COORDINATE_SPLIT)
            points.append(Point(int(split[0]), int(split[1])))
        return points

