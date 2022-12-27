from .valve import Valve
import re


class ValveParser:
    def parse(self, input: list[str]) -> list[Valve]:
        valves: list[Valve] = []
        for line in input:
            words = line.split()
            valve_name = words[1]
            valve_flow_rate = int(re.search(r'\d+', words[4]).group())
            neighbour_valves = list(map(lambda word: word.replace(",", ""), words[9:]))
            valves.append(Valve(valve_name, valve_flow_rate, neighbour_valves))
        for valve in valves:
            valve.initialize_neighbours(valves)
        return valves
