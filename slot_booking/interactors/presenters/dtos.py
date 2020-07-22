from dataclasses import dataclass
from datetime import time
@dataclass
class WashingMachineDTO:
    washing_machine_id: int
    slots: str
    from_time: time
    to_time: time
    day: str