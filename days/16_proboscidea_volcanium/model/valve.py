from dataclasses import dataclass

class Valve:
    name: str = ""
    flow_rate: int = 0
    tunnels_lead_to_valves_names: list[str] = []
    tunnels_lead_to_valves: list['Valve'] = []

    def __init__(self, name: str, flow_rate: int, tunnels_lead_to_valves_names: list[str]):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels_lead_to_valves_names = tunnels_lead_to_valves_names
        self.closed = True

    def initialize_neighbours(self, all_valves: list['Valve']):
        self.tunnels_lead_to_valves = list(filter(lambda valve: valve.name in self.tunnels_lead_to_valves_names, all_valves))

    def get_neighbours(self):
        return self.tunnels_lead_to_valves
