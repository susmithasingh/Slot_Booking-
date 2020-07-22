from typing import List

from slot_booking.interactors.presenters.get_washing_machine_slot_presenter_interface import \
    GetWashingMachineSlotsPresenterInterface

from slot_booking.constants.exception_messages import INVALID_MACHINE_ID

from slot_booking.exceptions.exceptions import NotFound



class GetWashingMachineSlotsPresenterImplementation(GetWashingMachineSlotsPresenterInterface):

    def raise_invalid_washing_machine_id_exception(self):
        raise NotFound(*INVALID_MACHINE_ID)

    def get_washing_machine_slots_response(self, list_of_slot_details: List[dict]):

        return list_of_slot_details
