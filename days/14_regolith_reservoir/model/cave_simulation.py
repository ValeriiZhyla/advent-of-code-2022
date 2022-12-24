from .cave import Cave


class CaveSimulation:
    cave: Cave = None

    def __init__(self, cave: Cave):
        self.cave = cave

    def perform_simulation(self) -> int:
        while self.cave.perform_simulation_round():
            if self.cave.amount_of_sand_in_rest_state() % 100 == 0:
                print("Step", self.cave.amount_of_sand_in_rest_state())
            pass
        return self.cave.amount_of_sand_in_rest_state()
