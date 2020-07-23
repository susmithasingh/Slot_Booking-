from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json

from .validator_class import ValidatorClass
from slot_booking.storages.update_washing_machine_status_storage_implimentation \
    import WashingMachineStorageImplementation

from slot_booking.interactors.updating_washing_mechine_status_interactor \
    import UpdateWashingMachineStatusInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$44")
    washing_machine_id = request_data["washing_machine_id"]
    is_active = request_data["is_active"]
    storage = WashingMachineStorageImplementation()
    interactor = UpdateWashingMachineStatusInteractor(
        storage=storage
    )
    interactor.update_washing_machine_status(
        washing_machine_id=washing_machine_id,
        is_active=is_active)
    print("**************************888888888")

    response = HttpResponse(status=200)

    return response
