START_POINT_NAME = "S"
END_POINT_NAME = "E"

START_POINT_ELEVATION: str = "a"
END_POINT_ELEVATION: str = "z"


class Node:
    name: str = ""
    elevation: str = ""
    neighbours: set['Node'] = set()
    x_coordinate: int = 0
    y_coordinate: int = 0
    depth = 0

    def __init__(self, name, x, y):
        self.name = name
        self.neighbours = set()
        if name == START_POINT_NAME:
            self.elevation = START_POINT_ELEVATION
        elif name == END_POINT_NAME:
            self.elevation = END_POINT_ELEVATION
        else:
            self.elevation = name
        self.x_coordinate = x
        self.y_coordinate = y

    def add_neighbour(self, neighbour: 'Node'):
        self.neighbours.add(neighbour)

    def is_start_node(self) -> bool:
        if self.name == START_POINT_NAME:
            return True

    def is_end_node(self) -> bool:
        if self.name == END_POINT_NAME:
            return True

    def target_node_is_accessible(self, target: 'Node') -> bool:
        return ord(target.elevation) - ord(self.elevation) <= 1

    def has_same_elevation_as_starting_point(self):
        return self.elevation == START_POINT_ELEVATION
