import copy

from .directions import Directions


class RopePhysics:
    starting_point = (0, 0)

    VISITED_MARK = "#"
    NOT_VISITED_MARK = "."

    EMPTY_CELL_MARK = "."
    ROPE_HEAD_MARK = "H"
    ROPE_TAIL_MARK = "T"

    rope_grid: list[list[str]] = []
    visited_positions_grid: list[list[int]] = []

    def __init__(self):
        self.rope_grid = []
        self.visited_positions_grid = []

    def create_grid_and_perform_moves(self, head_moves_lines: list[str], knots: int = 2):
        self.initialize_grids(head_moves_lines)
        self.perform_moves(head_moves_lines, knots)

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
        self.rope_grid = [[self.EMPTY_CELL_MARK] * (width + 1) for row in range(0, height+1)]
        self.visited_positions_grid = [[self.NOT_VISITED_MARK] * (width + 1) for row in range(0, height+1)]
        # initialize starting point
        self.starting_point = (-min_width, -min_height)

    def count_visited_tail_positions(self):
        total_count = 0
        for line in self.visited_positions_grid:
            for mark in line:
                if mark == self.VISITED_MARK:
                    total_count += 1
        return total_count

    def show_movement(self, knot_positions):
        rope_grid_copy = copy.deepcopy(self.rope_grid)
        for knot_idx in range(0, len(knot_positions)):
            if knot_idx == 0:
                label = self.ROPE_HEAD_MARK
            else:
                label = knot_idx
            x, y = knot_positions[knot_idx]
            if rope_grid_copy[y][x] == self.EMPTY_CELL_MARK:
                rope_grid_copy[y][x] = str(label)

        for row in reversed(rope_grid_copy):
            print("".join(row))
        print("==============================")

    def show_visited_by_tail(self):
        for row in reversed(self.visited_positions_grid):
            print("".join(row))

    def perform_moves(self, head_moves_lines: list[str], knots_number: int = 2):
        assert knots_number >= 2
        knots: list[(int, int)] = [self.starting_point for i in range(0, knots_number)]

        self.mark_tail_visited_position(self.starting_point)
        for move in head_moves_lines:
            for knot_idx in range(0, knots_number-1):
                current_head_position = knots[knot_idx]
                current_tail_position = knots[knot_idx+1]
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
                            # track only last knot
                            if knot_idx == knots_number - 2:
                                self.mark_tail_visited_position(current_tail_position)
                            knots[knot_idx] = current_head_position
                            knots[knot_idx + 1] = current_tail_position
                            self.show_movement(knots)
                    case _:
                        raise Exception(f"Unexpected move format: {move}")

    def mark_tail_visited_position(self, current_tail_position: (int, int)):
        x, y = current_tail_position
        assert y < len(self.visited_positions_grid)
        assert x < len(self.visited_positions_grid[0])

        self.visited_positions_grid[y][x] = self.VISITED_MARK

    def calculate_new_position_tail_one_step(self, tail_position: (int, int), old_head_position: (int, int), new_head_position: (int, int), direction: str) -> (int, int):
        if self.distance(tail_position, new_head_position) <= 1:
            return tail_position
        x, y = tail_position
        match direction:
            case (Directions.RIGHT):
                if self.same_row(tail_position, new_head_position):
                    return x + 1, y
                elif self.head_was_on_right_top_diagonal(tail_position, old_head_position):
                    return x + 1, y + 1
                elif self.head_was_on_left_top_diagonal(tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_right_bottom_diagonal(tail_position, old_head_position):
                    return x + 1, y - 1
                elif self.head_was_on_left_bottom_diagonal(tail_position, old_head_position):
                    return x, y
            case (Directions.LEFT):
                if self.same_row(tail_position, new_head_position):
                    return x - 1, y
                elif self.head_was_on_right_top_diagonal(tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_top_diagonal(tail_position, old_head_position):
                    return x - 1, y + 1
                elif self.head_was_on_right_bottom_diagonal(tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_bottom_diagonal(tail_position, old_head_position):
                    return x - 1, y - 1
            case (Directions.UP):
                if self.same_column(tail_position, new_head_position):
                    return x, y + 1
                elif self.head_was_on_right_top_diagonal(tail_position, old_head_position):
                    return x + 1, y + 1
                elif self.head_was_on_left_top_diagonal(tail_position, old_head_position):
                    return x - 1, y + 1
                elif self.head_was_on_right_bottom_diagonal(tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_bottom_diagonal(tail_position, old_head_position):
                    return x, y
            case (Directions.DOWN):
                if self.same_column(tail_position, new_head_position):
                    return x, y - 1
                elif self.head_was_on_right_top_diagonal(tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_left_top_diagonal(tail_position, old_head_position):
                    return x, y
                elif self.head_was_on_right_bottom_diagonal(tail_position, old_head_position):
                    return x + 1, y - 1
                elif self.head_was_on_left_bottom_diagonal(tail_position, old_head_position):
                    return x - 1, y - 1
        raise Exception(f"Unexpected move: current_tail_position={tail_position},old_head_position={old_head_position}, new_head_position={new_head_position}, direction={direction}")

    def distance(self, tail_position: (int, int), head_position: (int, int)) -> int:
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
