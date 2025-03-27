from enum import Enum

class TaskState(Enum):
    """Enumeration for task states."""
    OPEN = "Open"
    WAITING = "Waiting"
    DONE = "Done"
    
    def __str__(self):
        return self.value