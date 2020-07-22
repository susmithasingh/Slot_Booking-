from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json

from .validator_class import ValidatorClass
from slot_booking.presenters.get_washing_machine_presenter_implementation import \
    GetWashingMachineSlotsPresenterImplementation

from slot_booking.storages.get_washing_mechine_slots_storage_implementation import \
    GetWashingMachineSlotDetailsStorageImplementation

from slot_booking.interactors.get_washing_machine_slots_interactor import GetWashingMachineSlots


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    washing_machine_id = kwargs["washing_machine_id"]
    day = kwargs["day"]

    presenter = GetWashingMachineSlotsPresenterImplementation()
    storage = GetWashingMachineSlotDetailsStorageImplementation()

    interactor = GetWashingMachineSlots(
        storage=storage,
        presenter=presenter
    )
    data = interactor.get_washing_machine_slots(
            washing_machine_id=washing_machine_id,
            day=day
    )
    data = json.dumps(data)
    response = HttpResponse(data, status=200)
    return response



