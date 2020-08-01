from abc import ABC
from abc import abstractmethod
from typing import List


class UserSlotDetailsInterface(ABC):

    @abstractmethod
    def get_available_slots(self, dates: List) -> List[dict]:
        pass
