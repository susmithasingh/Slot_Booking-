from abc import ABC
from abc import abstractmethod
from typing import List


class GetWashingMachineSlotsStorageInterface(ABC):

    @abstractmethod

    def validate_washing_machine_id(self, washing_machine_id: int):
        pass

    @abstractmethod
    def get_washing_machine_slots(
            self,
            washing_machine_id: int,
            day: str) -> List[dict]:
        pass
