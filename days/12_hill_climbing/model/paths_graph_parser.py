from .paths_graph import PathsGraph
from .node import Node


class PathsGraphParser:
    def build_graph(self, input_grid: list[str]) -> PathsGraph:

        nodes_grid: list[list[Node]] = self.create_nodes_grid(input_grid)
        graph: PathsGraph = self.build_connections(nodes_grid)
        return graph

    def create_nodes_grid(self, input_grid: list[str]) -> list[list[Node]]:
        nodes_grid = []
        for line_idx in range(0, len(input_grid)):
            line = input_grid[line_idx]
            nodes_line = []
            for letter_idx in range(0, len(line)):
                letter = line[letter_idx]
                nodes_line.append(Node(letter, letter_idx, line_idx))
            nodes_grid.append(nodes_line)
        return nodes_grid

    def build_connections(self, nodes_grid: list[list[Node]]) -> PathsGraph:
        min_width = 0
        min_height = 0
        max_width = len(nodes_grid[0]) - 1
        max_height = len(nodes_grid) - 1
        for x in range(min_width, max_width + 1):
            for y in range(min_height, max_height + 1):
                current_node = nodes_grid[y][x]
                if x < max_width:
                    right_node = nodes_grid[y][x + 1]
                    self.connect_nodes_if_possible(current_node, right_node)
                if x > min_width:
                    left_node = nodes_grid[y][x - 1]
                    self.connect_nodes_if_possible(current_node, left_node)
                if y < max_height:
                    upper_node = nodes_grid[y + 1][x]
                    self.connect_nodes_if_possible(current_node, upper_node)
                if y > min_height:
                    bottom_node = nodes_grid[y - 1][x]
                    self.connect_nodes_if_possible(current_node, bottom_node)
        nodes_set = set([item for sublist in nodes_grid for item in sublist])
        return PathsGraph(nodes_set)

    def connect_nodes_if_possible(self, first_node: Node, second_node: Node):
        if first_node.target_node_is_accessible(second_node):
            first_node.add_neighbour(second_node)
        if second_node.target_node_is_accessible(first_node):
            second_node.add_neighbour(first_node)
