class ForestAnalyzer:
    def count_visible_trees(self, trees: list[list[int]]) -> int:
        count = 0
        if trees == []:
            return count
        count += self.visible_at_border(trees)
        for row_idx in range(1, len(trees) - 1):
            for col_idx in range(1, len(trees[0]) - 1):
                tree_idx = (row_idx, col_idx)
                if self.tree_is_visible_from_left(tree_idx, trees):
                    count += 1
                elif self.tree_is_visible_from_rigth(tree_idx, trees):
                    count += 1
                elif self.tree_is_visible_from_top(tree_idx, trees):
                    count += 1
                elif self.tree_is_visible_from_bottom(tree_idx, trees):
                    count += 1
        return count

    def find_best_scenic_score(self, trees: list[list[int]]) -> int:
        scenic_scores: list[list[int]] = self.create_empty_scenic_scores(trees)
        self.fill_scenic_scores_edges(trees, scenic_scores)
        self.fill_scenic_scores_middle(trees, scenic_scores)
        return max([max(row) for row in scenic_scores])

    def fill_scenic_scores_edges(self, trees: list[list[int]], scenic_scores: list[list[int]]):
        # one side is zero -> scenic score is zero
        pass

    def fill_scenic_scores_middle(self, trees: list[list[int]], scenic_scores: list[list[int]]):
        for row_idx in range(1, len(trees) - 1):
            for col_idx in range(1, len(trees[0]) - 1):
                tree_idx = (row_idx, col_idx)
                view_distance_left = self.count_visible_trees_left(tree_idx, trees)
                view_distance_right = self.count_visible_trees_right(tree_idx, trees)
                view_distance_top = self.count_visible_trees_top(tree_idx, trees)
                view_distance_bottom = self.count_visible_trees_bottom(tree_idx, trees)
                scenic_scores[row_idx][col_idx] = self.calculate_scenic_score(view_distance_left, view_distance_right, view_distance_top, view_distance_bottom)
        return scenic_scores

    def visible_at_border(self, trees):
        return 2 * len(trees) + 2 * len(trees[0]) - 4

    def tree_is_visible_from_left(self, tree_idx: (int, int), trees: list[list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = trees[target_tree_row][0:target_tree_col]
        return self.tree_is_visible_behind_barriers(potential_barriers, target_tree_height)

    def tree_is_visible_from_rigth(self, tree_idx: (int, int), trees: list[list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = trees[target_tree_row][(target_tree_col + 1):]
        return self.tree_is_visible_behind_barriers(potential_barriers, target_tree_height)

    def tree_is_visible_from_top(self, tree_idx: (int, int), trees: list[list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = [row[target_tree_col] for row in trees][0: target_tree_row]
        return self.tree_is_visible_behind_barriers(potential_barriers, target_tree_height)

    def tree_is_visible_from_bottom(self, tree_idx: (int, int), trees: [list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = [row[target_tree_col] for row in trees][target_tree_row + 1:]
        return self.tree_is_visible_behind_barriers(potential_barriers, target_tree_height)

    def tree_is_visible_behind_barriers(self, potential_barriers: list[int], target_tree_height:int) -> bool:
        for potential_barrier_tree_height in potential_barriers:
            if potential_barrier_tree_height >= target_tree_height:
                return False
        return True

    def create_empty_scenic_scores(self, trees: list[list[int]]) -> list[list[int]]:
        scenic_scores = []
        for x in range(0, len(trees)):
            columns = []
            for y in range(0, len(trees[0])):
                columns.append(0)
            scenic_scores.append(columns)
        return scenic_scores

    def calculate_scenic_score(self, view_distance_left: int, view_distance_right: int, view_distance_top: int, view_distance_bottom: int) -> int:
        return view_distance_left * view_distance_right * view_distance_top * view_distance_bottom

    def count_visible_trees_left(self, tree_idx: (int, int), trees: list[list[int]]) -> int:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = trees[target_tree_row][0:target_tree_col]
        potential_barriers.reverse()
        return self.calculate_visibility_from_tree_to_border(potential_barriers, target_tree_height)

    def count_visible_trees_right(self, tree_idx: (int, int), trees: list[list[int]]) -> int:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = trees[target_tree_row][(target_tree_col + 1):]
        return self.calculate_visibility_from_tree_to_border(potential_barriers, target_tree_height)

    def count_visible_trees_top(self, tree_idx: (int, int), trees: list[list[int]]) -> int:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = [row[target_tree_col] for row in trees][0: target_tree_row]
        potential_barriers.reverse()
        return self.calculate_visibility_from_tree_to_border(potential_barriers, target_tree_height)

    def count_visible_trees_bottom(self, tree_idx: (int, int), trees: list[list[int]]) -> int:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = [row[target_tree_col] for row in trees][target_tree_row + 1:]
        return self.calculate_visibility_from_tree_to_border(potential_barriers, target_tree_height)

    def calculate_visibility_from_tree_to_border(self, potential_barriers: list[int], target_tree_height:int) -> int:
        view_distance = 1
        for potential_barrier_idx in range(0, len(potential_barriers)):
            potential_barrier_tree_height = potential_barriers[potential_barrier_idx]
            if potential_barrier_tree_height >= target_tree_height:
                return view_distance
            elif potential_barrier_idx < len(potential_barriers) - 1:
                view_distance += 1
        return view_distance