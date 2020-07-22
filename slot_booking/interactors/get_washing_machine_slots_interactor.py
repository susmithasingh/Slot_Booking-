from slot_booking.constants.enums import ListOfDays
from slot_booking.exceptions.exceptions import InvalidWashingMachineId
from slot_booking.interactors.presenters.get_washing_machine_slot_presenter_interface import \
    GetWashingMachineSlotsPresenterInterface
from slot_booking.interactors.storages.get_machine_details_storage_interface import GetWashingMachineSlotsStorageInterface
from slot_booking.models import WashingMechine


class GetWashingMachineSlots():
    def __init__(
            self,
            storage: GetWashingMachineSlotsStorageInterface,
            presenter: GetWashingMachineSlotsPresenterInterface
            ):
        self.storage = storage
        self.presenter = presenter

    # def get_washing_machine_slots_wrapper(
    #         self,
    #         washing_machine_id: int,
    #         day: ListOfDays,
    #         presenter: GetWashingMachineSlotsPresenterInterface):
    #
    #     try:
    #         washing_machine_slots = self.get_washing_machine_slots(washing_machine_id=washing_machine_id,day=day)
    #         slot_details = presenter.get_washing_machine_slots_response(washing_machine_slots)
    #         return slot_details
    #     except InvalidWashingMachineId:
    #         presenter.raise_invalid_washing_machine_id_exception()

    def get_washing_machine_slots(self, washing_machine_id: int,
                                      day: ListOfDays):

        # TODO validate washing machine id
        is_valid = self.storage.validate_washing_machine_id(washing_machine_id=washing_machine_id)
        if not is_valid:
            self.presenter.raise_invalid_washing_machine_id_exception()
            return

        # TODO get slots for given washing machine_id in given day

        list_of_slot_details = self.storage.get_washing_machine_slots(
                washing_machine_id=washing_machine_id,
                day=day)
        return list_of_slot_details
