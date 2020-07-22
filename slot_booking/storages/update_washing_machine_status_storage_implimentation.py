from slot_booking.interactors.presenters.washing_machine_storage_interface import \
    WashingMachineStorageInterface
from slot_booking.models import WashingMechine


class WashingMachineStorageImplementation(WashingMachineStorageInterface):

    def update_washing_machine_status(self, washing_machine_id: int, is_active: bool):

        WashingMechine.objects.filter(washing_machine_id=washing_machine_id).update(is_active=is_active)
