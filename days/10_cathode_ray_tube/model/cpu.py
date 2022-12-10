from .execution_stack import ExecutionStack
from .instruction import Instruction, AddxInstruction, NoopInstruction
from .execution_log import ExecutionLog

class CPU:
    execution_stack: ExecutionStack = None

