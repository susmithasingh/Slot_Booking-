from abc import ABC
from abc import abstractmethod

class WashingMachineStorageInterface(ABC):
    @abstractmethod
    def update_washing_machine_status(self, washing_machine_id: int):
        pass
