from .valve import Valve
from .path import Path
import math

from copy import deepcopy

class TunnelNetwork:
    valves: list[Valve]

    def __init__(self, valves: list[Valve]):
        self.valves = valves

    def calculate_max_possible_pressure_release(self, start: Valve, time: int) -> int:
        all_possible_paths: list[Path] = self.calculate_all_possible_paths_with_all_valve_states(start, time)
        return max(map(lambda path: self.calculate_flow_rate_of_path(path), all_possible_paths))

    def calculate_all_possible_paths_with_all_valve_states(self, current, time) -> list[Path]:
        if time == 0:
            # we can do nothing
            return [Path()]
        if time == 1:
            # we can only open current valve
            path = Path()
            path.add_node_open_valve(current)
            return [path]
        if time == 2:
            # we can open current valve or make one more step and try following valve
            all_paths_from_neighbours: list[Path] = self.flatten(list(map(lambda neighbour: self.calculate_all_possible_paths_with_all_valve_states(neighbour, time - 1), current.get_neighbours())))
            path_current_opened: Path = Path()
            path_current_opened.add_node_open_valve(current)
            paths_current_closed: list[Path] = []
            for neighbour_path in all_paths_from_neighbours:
                current_path_closed: Path = Path()
                current_path_closed.add_node_close_valve(current)
                current_path_closed.append_path(neighbour_path)
                paths_current_closed.append(current_path_closed)
            if current.flow_rate != 0:
                return [path_current_opened] + paths_current_closed
            else:
                return paths_current_closed
        if time >= 3:
            # we can open current valve and try following valves or we can leave current valve closed and try following valves
            all_paths_from_neighbours_current_closed: list[Path] = self.flatten(list(map(lambda neighbour: self.calculate_all_possible_paths_with_all_valve_states(neighbour, time - 1), current.get_neighbours())))
            all_paths_from_neighbours_current_opened: list[Path] = self.flatten(list(map(lambda neighbour: self.calculate_all_possible_paths_with_all_valve_states(neighbour, time - 2), current.get_neighbours())))
            paths_current_closed: list[Path] = []
            for neighbour_path in all_paths_from_neighbours_current_closed:
                current_path_closed: Path = Path()
                current_path_closed.add_node_close_valve(current)
                current_path_closed.append_path(neighbour_path)
                paths_current_closed.append(current_path_closed)
            paths_current_opened: list[Path] = []
            if current.flow_rate != 0:
                for neighbour_path in all_paths_from_neighbours_current_opened:
                    current_path_opened: Path = Path()
                    current_path_opened.add_node_close_valve(current)
                    current_path_opened.append_path(neighbour_path)
                    paths_current_closed.append(current_path_opened)
            return paths_current_closed + paths_current_opened

    def calculate_flow_rate_of_path(self, path: Path):
        flow_rate = 1
        for idx in range(0, len(path.visited_nodes)):
            if path.valves_opened[idx]:
                flow_rate *= path.visited_nodes[idx].flow_rate
        return flow_rate

    def flatten(self, list):
        return [item for sublist in list for item in sublist]

