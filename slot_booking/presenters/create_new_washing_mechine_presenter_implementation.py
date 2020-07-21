from slot_booking.constants.exception_messages import \
    (
        INVALID_MACHINE_ID

    )
from slot_booking.interactors.presenters.add_washing_mechine_presenter_interface import AddNewWashingMachinePresenterInterface

from django_swagger_utils.drf_server.exceptions import NotFound

class AddNewWashingMachinePresenterImplementation(AddNewWashingMachinePresenterInterface):

    def raise_invalid_washing_machine_id_exception(self):
        raise NotFound(*INVALID_MACHINE_ID)
