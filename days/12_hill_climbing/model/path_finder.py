from .paths_graph import PathsGraph
from .node import Node


class PathFinder:
    def find_length_of_shortest_path_from_start_to_end(self, graph: PathsGraph) -> int:
        start_node = graph.get_start_node()
        end_node = graph.get_end_node()
        return self.calculate_minimal_distance_from_start_node_to_end(start_node, end_node)

    def calculate_minimal_distance_from_start_node_to_end(self, start: Node, end: Node) -> int:
        # BFS
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        start.depth = 0
        while queue:
            node = queue.pop(0)

            if end in node.neighbours:
                return node.depth + 1

            for neighbour in node.neighbours:
                print(neighbour.x_coordinate, neighbour.y_coordinate)
                if neighbour not in visited:
                    neighbour.depth = node.depth + 1
                    visited.append(neighbour)
                    queue.append(neighbour)

        print("There are no more")
        return -1
        

