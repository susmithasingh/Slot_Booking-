from abc import ABC
from abc import abstractmethod
from typing import List

from slot_booking.constants.enums import ListOfDays


class GetWashingMachineSlotsPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_washing_machine_id_exception(self) :
        pass

    @abstractmethod
    def get_washing_machine_slots_response(self,washing_machine_id: int,
                                           days: ListOfDays) -> List[dict]:
        pass
