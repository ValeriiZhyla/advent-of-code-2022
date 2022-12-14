class Coordinate:
    x: int = 0
    y: int = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other: 'Coordinate'):
        return self.x == other.x and self.y == other.y
