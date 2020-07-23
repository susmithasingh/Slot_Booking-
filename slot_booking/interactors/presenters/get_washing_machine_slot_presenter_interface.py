from abc import ABC
from abc import abstractmethod
from typing import List

from slot_booking.constants.enums import ListOfDays


class GetWashingMachineSlotsPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_washing_machine_id_exception(self) :
        pass