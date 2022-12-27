from .valve import Valve


class Path:
    visited_nodes: list[Valve]
    valves_opened: list[bool]

    def __init__(self):
        self.visited_nodes = []
        self.valves_opened = []

    def add_node_open_valve(self, node: Valve):
        self.visited_nodes.append(node)
        self.valves_opened.append(True)

    def add_node_close_valve(self, node: Valve):
        self.visited_nodes.append(node)
        self.valves_opened.append(False)

    def append_path(self, neighbour_path: 'Path'):
        self.visited_nodes += neighbour_path.visited_nodes
        self.valves_opened += neighbour_path.valves_opened
