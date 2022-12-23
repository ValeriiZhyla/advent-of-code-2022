from .node import Node


class PathsGraph:
    nodes: set[Node] = []

    def __init__(self, nodes: set[Node]):
        self.nodes = nodes

    def get_start_node(self):
        for node in self.nodes:
            if node.is_start_node():
                return node

    def get_end_node(self):
        for node in self.nodes:
            if node.is_end_node():
                return node

    def erase_current_depth_in_nodes(self):
        for node in self.nodes:
            node.depth = 0
