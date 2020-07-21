from abc import ABC
from abc import abstractmethod
from typing import List


class GetWashingMachineDetailsPresenterInterface(ABC):
    @abstractmethod
    def get_all_washing_machines_details_response(self) ->List[dict]:
        pass