from .knot import Knot


class RopePhysics:
    starting_point = (0, 0)

    def find_unique_points_visited_by_tail(self, head_moves_lines: list[str], knots_number: int = 2) -> int:
        assert knots_number >= 2
        knots: list[Knot] = [Knot(self.starting_point) for i in range(0, knots_number)]
        unique_visited_points: {int, int} = set()
        for line in head_moves_lines:
            x = 0
            y = 0
            match line.split():
                case [direction, steps]:
                    for step in range(0, int(steps)):
                        head_knot = knots[0]
                        tail_knot = knots[-1]
                        head_knot.move_one_step_in_direction(direction)
                        for knot_idx in range(0, knots_number-1):
                            distance_vector = self.get_distance_between_two_knots(knots[knot_idx], knots[knot_idx+1])
                            if self.knots_are_not_adjacent(distance_vector):
                                knots[knot_idx + 1].move(self.sign(distance_vector[0]), self.sign(distance_vector[1]))
                        unique_visited_points.add(tail_knot.position)
        return len(unique_visited_points)

    def get_distance_between_two_knots(self, first_knot: Knot, second_knot: Knot) -> (int, int):
        head_x, head_y = first_knot.position
        tail_x, tail_y = second_knot.position

        return head_x - tail_x, head_y - tail_y

    def knots_are_not_adjacent(self, distance_vector):
        x, y = distance_vector
        return abs(x) > 1 or abs(y) > 1

    def sign(self, x):
        if x == 0:
            return 0
        return 1 if x > 0 else -1



