from .paths_graph import PathsGraph
from .node import Node

class PathFinder:

    def find_length_of_shortest_path_from_start_to_end(self, graph: PathsGraph) -> int:
        start_node = graph.get_start_node()
        end_node = graph.get_end_node()
        return self.calculate_minimal_distance_from_start_node_to_end(start_node, end_node, graph)

    def calculate_minimal_distance_from_start_node_to_end(self, start: Node, end: Node, graph: PathsGraph) -> int:
        # BFS
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        graph.erase_current_depth_in_nodes()
        while queue:
            node = queue.pop(0)

            if end in node.neighbours:
                return node.depth + 1

            for neighbour in node.neighbours:
                if neighbour not in visited:
                    neighbour.depth = node.depth + 1
                    visited.append(neighbour)
                    queue.append(neighbour)

        # print("There are no more")
        return float('inf')
        
    def find_length_of_shortest_path_from_all_lowest_points_to_end(self, graph: PathsGraph) -> int:
        possible_starting_points: list[Node] = list(filter(lambda node: node.has_same_elevation_as_starting_point(), graph.nodes))
        end_node = graph.get_end_node()
        distances = list(map(lambda start: self.calculate_minimal_distance_from_start_node_to_end(start, end_node, graph), possible_starting_points))
        return min(distances)
