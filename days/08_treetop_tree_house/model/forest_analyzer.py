class ForestAnalyzer:
    def count_visible_trees_lrtb(self, trees: list[list[int]]) -> int:
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

    def visible_at_border(self, trees):
        return 2*len(trees) + 2*len(trees[0]) - 4

    def tree_is_visible_from_left(self, tree_idx: (int, int), trees: [list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = trees[target_tree_row][0:target_tree_col]
        for potential_barrier_tree_height in potential_barriers:
            if potential_barrier_tree_height >= target_tree_height:
                return False
        return True

    def tree_is_visible_from_rigth(self, tree_idx: (int, int), trees: [list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = trees[target_tree_row][(target_tree_col + 1):]
        for potential_barrier_tree_height in potential_barriers:
            if potential_barrier_tree_height >= target_tree_height:
                return False
        return True

    def tree_is_visible_from_top(self, tree_idx: (int, int), trees: [list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = [row[target_tree_col] for row in trees][0: target_tree_row]
        for potential_barrier_tree_height in potential_barriers:
            if potential_barrier_tree_height >= target_tree_height:
                return False
        return True

    def tree_is_visible_from_bottom(self, tree_idx: (int, int), trees: [list[int]]) -> bool:
        target_tree_row, target_tree_col = tree_idx
        target_tree_height = trees[target_tree_row][target_tree_col]
        potential_barriers = [row[target_tree_col] for row in trees][target_tree_row+1:]
        for potential_barrier_tree_height in potential_barriers:
            if potential_barrier_tree_height >= target_tree_height:
                return False
        return True
