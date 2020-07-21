from slot_booking.models import WashingMechine
from slot_booking.interactors.storages.add_washing_mechine_storage_interface import AddNewWashingMachineStorageInterface
from slot_booking.exceptions.exceptions import InvalidWashingMachineId

class AddNewWashingMachineStorageImplimentation(AddNewWashingMachineStorageInterface):

    def validate_new_machine_id(self, washing_machine_id: int) -> bool:
        if washing_machine_id <= 0 :
            return False
        else:
            return True

    def create_new_washing_machine(self, washing_machine_id: int) -> int:

        new_machine_id = WashingMechine.objects.create(washing_machine_id=washing_machine_id)
        return new_machine_id