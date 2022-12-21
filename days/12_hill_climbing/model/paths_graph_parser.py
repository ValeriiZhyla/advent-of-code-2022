from .paths_graph import PathsGraph
from .node import Node

class PathsGraphParser:
    def build_graph(self, input_grid: list[str]) -> PathsGraph:

        nodes_grid: list[list[Node]] = self.create_nodes_grid(input_grid)
        graph: PathsGraph = self.build_connections(nodes_grid)
        return graph

    def create_nodes_grid(self, input_grid: list[str]) -> list[list[Node]]:
        nodes_grid = []
        for line in input_grid:
            nodes_line = []
            for letter in line:
                nodes_line.append(Node(letter))
            nodes_grid.append(nodes_line)
        return nodes_grid

    def build_connections(self, nodes_grid: list[list[Node]]) -> PathsGraph:
        min_width = 0
        min_height = 0
        max_width = len(nodes_grid[0]) - 1
        max_height = len(nodes_grid) - 1
        for x in range(min_width, max_width):
            for y in range(min_height, max_height):
                current_node = nodes_grid[y][x]
                if x < max_width:
                    right_node = nodes_grid[y][x+1]
                    if right_node.is_accessible_from(current_node):
                        self.connect_nodes(current_node, right_node)
                if x > min_width:
                    left_node = nodes_grid[y][x-1]
                    if left_node.is_accessible_from(current_node):
                        self.connect_nodes(current_node, left_node)
                if y < max_height:
                    upper_node = nodes_grid[y+1][x]
                    if upper_node.is_accessible_from(current_node):
                        self.connect_nodes(current_node, upper_node)
                if y > min_height:
                    bottom_node = nodes_grid[y-1][x]
                    if bottom_node.is_accessible_from(current_node):
                        self.connect_nodes(current_node, bottom_node)
        nodes_set = set([item for sublist in nodes_grid for item in sublist])
        return PathsGraph(nodes_set)

    def connect_nodes(self, first_node: Node, second_node: Node):
        first_node.add_neighbour(second_node)
        second_node.add_neighbour(first_node)
