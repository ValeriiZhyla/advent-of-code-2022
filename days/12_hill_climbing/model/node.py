START_POINT_NAME = "S"
END_POINT_NAME = "E"

START_POINT_ELEVATION: str = "a"
END_POINT_ELEVATION: str = "z"


class Node:
    name: str = ""
    elevation: str = ""
    neighbours: set['Node'] = set()

    def __init__(self, name):
        self.name = name
        self.neighbours = set()
        if name == START_POINT_NAME:
            self.elevation = START_POINT_ELEVATION
        elif name == END_POINT_NAME:
            self.elevation = END_POINT_ELEVATION
        else:
            self.elevation = name

    def add_neighbour(self, neighbour: 'Node'):
        self.neighbours.add(neighbour)

    def is_start_node(self) -> bool:
        if self.name == START_POINT_NAME:
            return True

    def is_end_node(self) -> bool:
        if self.name == END_POINT_NAME:
            return True

    def is_accessible_from(self, node: 'Node') -> bool:
        return abs(ord(self.elevation) - ord(node.elevation)) <= 1
