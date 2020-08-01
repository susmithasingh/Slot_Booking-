from typing import List

from slot_booking.models import WashingMachineSlots
from slot_booking.interactors.storages.get_machine_details_storage_interface import GetWashingMachineSlotsStorageInterface

from slot_booking.models import WashingMechine


class GetWashingMachineSlotDetailsStorageImplementation(GetWashingMachineSlotsStorageInterface):

    def get_washing_machine_slots(
            self,
            washing_machine_id: int,
            day: str) -> List[dict]:

        data = WashingMachineSlots.objects.filter(washing_machine_id=washing_machine_id, day=day)

        machine_slot_list = []
        for machine_slots in data:
            washing_machine_slots={}

            washing_machine_slots["slots"] = machine_slots.slots
            washing_machine_slots["from_time"] = str(machine_slots.from_time)
            washing_machine_slots["to_time"] = str(machine_slots.to_time)
            machine_slot_list.append(washing_machine_slots)

        return machine_slot_list

    def validate_washing_machine_id(self, washing_machine_id: int) -> bool:
        is_valid_machine_id = WashingMechine.objects.filter(washing_machine_id=washing_machine_id).exists()
        return is_valid_machine_id

    def create_or_update_washing_machine_slots(
            self,
            washing_machine_id: int,
            day: str,
            washing_machine_slots: List[dict]):
        machine = WashingMachineSlots.objects.filter(washing_machine_id=washing_machine_id, day=day)
        machine_slots = []
        for data in machine:




