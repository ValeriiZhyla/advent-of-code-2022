from .execution_log_entry import ExecutionLogEntry

class ExecutionLog:
    entries: list[ExecutionLogEntry] = []

    def __init__(self):
        self.entries = []

    def create_entry(self, current_cycle_id: int, current_register_value: int):
        self.entries.append(ExecutionLogEntry(current_cycle_id, current_register_value))
