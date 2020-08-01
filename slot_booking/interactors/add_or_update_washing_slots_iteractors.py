from typing import List

from slot_booking.interactors.storages.get_machine_details_storage_interface import \
    GetWashingMachineSlotsStorageInterface


class CreateOrUpdateWashingMachineSlotsInteractor:

    def __init__(self, storage: GetWashingMachineSlotsStorageInterface):
        self.storage = storage

    def create_or_update_washing_machine_slots(self, washing_machine_id: int,
                                               day: str,
                                               washing_machine_slots: List[dict]):
        add_or_updatewashing_slots_Dto = [
            PrefilledCodeDto(
                slot=machine_slots["slot_details"]["slots"],
                languages=prefilled["slot_details"]["from_time"],
                file_name=prefilled["slot_details"]["file_name"],
                problem_id=problem_id
            ) for prefilled in create_prefilled_code_list
        ]
