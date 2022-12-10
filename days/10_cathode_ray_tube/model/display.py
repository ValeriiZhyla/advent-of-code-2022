from .execution_log import ExecutionLog

class Display:
    LIT_PIXEL: str = "#"
    DARK_PIXEL: str = "."
    ROW_WIDTH = 40

    def render(self, register_values: ExecutionLog):
        entries = register_values.entries
        for i in range(0, int(len(entries) / self.ROW_WIDTH)):
            rendering_information = entries[i*self.ROW_WIDTH: (i+1) * self.ROW_WIDTH]
            line = ""
            for item_idx in range(0, len(rendering_information)):
                item = rendering_information[item_idx]
                cycle = item.cycle_id
                current_row_symbol_index = (cycle - 1) % self.ROW_WIDTH
                register_value = item.register_value
                sprite_position = list(range(register_value - 1, register_value + 2))
                if self.current_rendering_symbol_overlaps_with_sprite(current_row_symbol_index, sprite_position):
                    line += self.LIT_PIXEL
                else:
                    line += self.DARK_PIXEL
            print(line)

    def current_rendering_symbol_overlaps_with_sprite(self, cycle: int, sprite_positions: list[int]):
        return cycle in sprite_positions
