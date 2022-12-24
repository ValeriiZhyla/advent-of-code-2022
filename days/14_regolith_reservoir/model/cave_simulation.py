from .cave import Cave


class CaveSimulation:
    cave: Cave = None

    def __init__(self, cave: Cave):
        self.cave = cave

    def perform_simulation_until_sand_falls_into_abyss(self) -> int:
        while self.cave.perform_simulation_round():
            pass
        return self.cave.amount_of_sand_in_rest_state()
