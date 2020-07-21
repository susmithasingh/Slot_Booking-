from abc import ABC
from abc import abstractmethod

class AddNewWashingMachineStorageInterface(ABC):

    @abstractmethod
    def validate_new_machine_id(self, washing_machine_id: int) -> bool:
        pass

    @abstractmethod
    def create_new_washing_machine(self, washing_machine_id: int) -> int:
        pass
