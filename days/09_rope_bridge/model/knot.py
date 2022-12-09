from .directions import Directions


class Knot:
    position: (int, int) = (0, 0)

    def __init__(self, initial_position: (int, int)):
        self.position = initial_position

    def move(self, x_offset, y_offset):
        current_x, current_y = self.position
        self.position = (current_x + x_offset, current_y + y_offset)

    def move_one_step_in_direction(self, direction):
        x = 0
        y = 0
        if direction == Directions.UP:
            x = 0
            y = -1
        elif direction == Directions.DOWN:
            x = 0
            y = 1
        elif direction == Directions.RIGHT:
            x = 1
            y = 0
        elif direction == Directions.LEFT:
            x = -1
            y = 0
        self.move(x, y)
