from slot_booking.interactors.presenters.washing_machine_storage_interface import \
    WashingMachineStorageInterface


class UpdateWashingMachineStatusInteractor:
    def __init__(
            self,
            storage: WashingMachineStorageInterface):
        self.storage=storage
    def update_washing_machine_status(self, washing_machine_id: int, is_active: bool):

        self.storage.update_washing_machine_status(washing_machine_id=washing_machine_id, is_active=is_active)