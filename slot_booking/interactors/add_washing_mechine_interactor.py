from slot_booking.interactors.presenters.add_washing_mechine_presenter_interface import AddNewWashingMachinePresenterInterface
from slot_booking.interactors.storages.add_washing_mechine_storage_interface import AddNewWashingMachineStorageInterface

from slot_booking.exceptions.exceptions import InvalidWashingMachineId


class AddNewWashingMachineInteractor:

    def __init__(
            self,
            storage: AddNewWashingMachineStorageInterface,
            presenter: AddNewWashingMachinePresenterInterface):
        self.storage = storage
        self.presenter = presenter

    # def create_new_washing_machine_wrapper(self, presenter: AddNewWashingMachinePresenterInterface, washing_machine_id: int):
    #     try:
    #         self.create_new_washing_machine(washing_machine_id = washing_machine_id)
    #     except InvalidWashingMachineId:
    #         presenter.raise_invalid_Washing_mechine_id_exception()
    #
    def create_new_washing_machine(self, washing_machine_id: int, washing_machine_image: str):

        # TODO Validate washing_machine_id

        is_valid_machine_id = self.storage.validate_new_machine_id(washing_machine_id=washing_machine_id)
        print(is_valid_machine_id)
        if not is_valid_machine_id:
            self.presenter.raise_invalid_washing_machine_id_exception()
            return

        # TODO create new washing_mechine with valid details
        return self.storage.create_new_washing_machine(washing_machine_id=washing_machine_id, washing_machine_image=washing_machine_image)