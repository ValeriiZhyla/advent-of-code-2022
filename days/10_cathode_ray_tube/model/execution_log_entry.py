class ExecutionLogEntry:
    cycle_id: int = 0
    register_value: int = 0

    def __init__(self, cycle_id: int, register_value: int):
        self.cycle_id = cycle_id
        self.register_value = register_value

