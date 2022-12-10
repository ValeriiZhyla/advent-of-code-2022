from .execution_stack import ExecutionStack
from .instruction import Instruction, AddxInstruction, NoopInstruction
from .execution_log import ExecutionLog
from .register import Register
from .execution_log_entry import ExecutionLogEntry

class CPU:
    START_CYCLE_ID = 1

    execution_stack: ExecutionStack = None
    execution_log: ExecutionLog = None
    register: Register = None
    current_cycle_id: int = 1


    def __init__(self, register: Register):
        self.register = register
        self.execution_stack = ExecutionStack(register)
        self.execution_log = ExecutionLog()
        self.current_cycle_id = self.START_CYCLE_ID

    def process_instructions(self, cpu_instructions: list[str]):
        for instruction in cpu_instructions:
            match instruction.split():
                case (NoopInstruction.NOOP_INSTRUCTION_NAME):
                    self.execution_stack.add_instruction(NoopInstruction(self.register))
                case (AddxInstruction.ADDX_INSTRUCTION_NAME, value):
                    parsed_value = int(value)
                    self.execution_stack.add_instruction(AddxInstruction(self.register, parsed_value))
            self.perform_cpu_cycle()
        while not self.execution_stack.is_empty():
            self.perform_cpu_cycle()

    def perform_cpu_cycle(self):
        self.execution_stack.process_cycle()
        self.execution_log.create_entry(self.current_cycle_id, self.register.value)
        self.current_cycle_id += 1

    def sum_signal_strengths(self, list_of_cycle_ids: list[int]) -> int:
        assert list_of_cycle_ids[-1] >= self.current_cycle_id
        target_log_entries: list[ExecutionLogEntry] = list(filter(lambda entry: entry.cycle_id in list_of_cycle_ids, self.execution_log.entries))
        return sum(map(lambda entry: entry.cycle_id * entry.register_value, target_log_entries))




