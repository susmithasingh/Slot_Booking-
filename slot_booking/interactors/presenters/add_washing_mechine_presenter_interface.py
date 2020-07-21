from abc import ABC
from abc import abstractmethod

class AddNewWashingMachinePresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_washing_machine_id_exception():
        pass