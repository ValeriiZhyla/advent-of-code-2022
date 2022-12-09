from .directions import Directions


class RopePhysics:
    starting_point = (0, 0)

    VISITED_MARK = 1
    NOT_VISITED_MARK = 0

    EMPTY_CELL_MARK = "."
    ROPE_HEAD_MARK = "H"
    ROPE_TAIL_MARK = "T"

    rope_grid: list[list[str]] = []
    visited_positions_grid: list[list[int]] = []

    def __init__(self):
        self.rope_grid = []
        self.visited_positions_grid = []

    def calculate_tail_movements_for_head_moves(self, head_moves_lines: list[str]):
        self.initialize_grids(head_moves_lines)
        self.perform_moves(head_moves_lines)
        self.show(self.rope_grid)

    def initialize_grids(self, head_moves_lines: list[str]):
        max_height = 0
        min_height = 0
        current_vertical_position = 0
        max_width = 0
        min_width = 0
        current_horizontal_position = 0
        for move in head_moves_lines:
            match move.split():
                case (Directions.RIGHT, steps):
                    current_horizontal_position += int(steps)
                    max_width = max(max_width, current_horizontal_position)
                case (Directions.LEFT, steps):
                    current_horizontal_position -= int(steps)
                    min_width = min(min_width, current_horizontal_position)
                case (Directions.UP, steps):
                    current_vertical_position += int(steps)
                    max_height = max(max_height, current_vertical_position)
                case (Directions.DOWN, steps):
                    current_vertical_position -= int(steps)
                    min_height = min(min_height, current_vertical_position)
        # find target dimensions
        width = max_width + (-min_width)
        height = max_height + (-min_height)
        # fill both grids
        self.rope_grid = [[self.EMPTY_CELL_MARK] * width for row in range(0, height)]
        self.visited_positions_grid = [[self.NOT_VISITED_MARK] * width for row in range(0, height)]
        # initialize starting point
        self.starting_point = (-min_width, -min_height)

    def show(self, grid: list[list[str]]):
        for row in reversed(grid):
            print("".join(row))

    def perform_moves(self, head_moves_lines: list[str]):
        current_head_position = self.starting_point
        current_tail_position = self.starting_point
        self.mark_tail_visited_position(current_tail_position)
        for move in head_moves_lines:
            match move.split():
                case (direction, steps):
                    steps = int(steps)
                    for i in range(0, steps):
                        old_head_position = current_head_position
                        head_x, head_y = current_head_position
                        match direction:
                            case (Directions.RIGHT):
                                current_head_position = (head_x + 1, head_y)
                            case (Directions.LEFT):
                                current_head_position = (head_x - 1, head_y)
                            case (Directions.UP):
                                current_head_position = (head_x, head_y + 1)
                            case (Directions.DOWN):
                                current_head_position = (head_x, head_y - 1)
                        current_tail_position = self.calculate_new_position_tail_one_step(current_tail_position, old_head_position, current_head_position, direction)
                        self.mark_tail_visited_position(current_tail_position)
                case _:
                    raise Exception(f"Unexpected move format: {move}")

    def mark_tail_visited_position(self, current_tail_position: (int, int)):
        x, y = current_tail_position
        self.visited_positions_grid[y][x] = self.VISITED_MARK

    def calculate_new_position_tail_one_step(self, current_tail_position: (int, int), old_head_position: (int, int), new_head_position: (int, int), direction: str) -> (int, int):
        if self.distance(current_tail_position, new_head_position) <= 1:
            return current_tail_position
        x, y = current_tail_position
        match direction:
            case (Directions.RIGHT):
                if self.same_row(current_tail_position, new_head_position):
                    return x + 1, y
                elif self.head_was_on_right_top_diagonal(current_tail_position, old_head_position):
                    return x + 1, y + 1
                elif self.head_was_on_left_top_diagonal(current_tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_right_bottom_diagonal(current_tail_position, old_head_position):
                    return x + 1, y - 1
                elif self.head_was_on_left_bottom_diagonal(current_tail_position, old_head_position):
                    return x, y
            case (Directions.LEFT):
                if self.same_row(current_tail_position, new_head_position):
                    return x - 1, y
                elif self.head_was_on_right_top_diagonal(current_tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_top_diagonal(current_tail_position, old_head_position):
                    return x - 1, y + 1
                elif self.head_was_on_right_bottom_diagonal(current_tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_bottom_diagonal(current_tail_position, old_head_position):
                    return x - 1, y - 1
            case (Directions.UP):
                if self.same_column(current_tail_position, new_head_position):
                    return x, y + 1
                elif self.head_was_on_right_top_diagonal(current_tail_position, old_head_position):
                    return x + 1, y + 1
                elif self.head_was_on_left_top_diagonal(current_tail_position, old_head_position):
                    return x - 1, y + 1
                elif self.head_was_on_right_bottom_diagonal(current_tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_bottom_diagonal(current_tail_position, old_head_position):
                    return x, y
            case (Directions.DOWN):
                if self.same_column(current_tail_position, new_head_position):
                    return x, y - 1
                elif self.head_was_on_right_top_diagonal(current_tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_top_diagonal(current_tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_right_bottom_diagonal(current_tail_position, old_head_position):
                    return x + 1, y - 1
                elif self.head_was_on_left_bottom_diagonal(current_tail_position, old_head_position):
                    return x - 1, y - 1
            case _:
                raise Exception("Unexpected move")

    def distance(self, tail_position: (int, int), head_position: (int, int)) -> int :
        tail_x, tail_y = tail_position
        head_x, head_y = head_position
        delta_x = abs(head_x - tail_x)
        delta_y = abs(head_y - tail_y)
        return max(delta_x, delta_y)

    def same_row(self, tail_position: (int, int), head_position: (int, int)) -> bool:
        return tail_position[1] == head_position[1]

    def same_column(self, tail_position: (int, int), head_position: (int, int)) -> bool:
        return tail_position[0] == head_position[0]

    def head_was_on_right_top_diagonal(self, tail_position, head_position):
        head_x, head_y = head_position
        tail_x, tail_y = tail_position
        return head_x == tail_x + 1 and head_y == tail_y + 1

    def head_was_on_left_top_diagonal(self, tail_position, head_position):
        head_x, head_y = head_position
        tail_x, tail_y = tail_position
        return head_x == tail_x - 1 and head_y == tail_y + 1

    def head_was_on_right_bottom_diagonal(self, tail_position, head_position):
        head_x, head_y = head_position
        tail_x, tail_y = tail_position
        return head_x == tail_x + 1 and head_y == tail_y - 1

    def head_was_on_left_bottom_diagonal(self, tail_position, head_position):
        head_x, head_y = head_position
        tail_x, tail_y = tail_position
        return head_x == tail_x - 1 and head_y == tail_y - 1
