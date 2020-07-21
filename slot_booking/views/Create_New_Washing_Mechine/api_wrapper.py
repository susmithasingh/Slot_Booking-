from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json

from .validator_class import ValidatorClass
from slot_booking.interactors.add_washing_mechine_interactor import AddNewWashingMachineInteractor
from slot_booking.presenters.create_new_washing_mechine_presenter_implementation import \
    AddNewWashingMachinePresenterImplementation
from slot_booking.storages.create_new_washing_mechine import AddNewWashingMachineStorageImplimentation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data= kwargs['request_data']
    print(request_data)
    washing_machine_id = request_data['washing_mechine_id']
    storage = AddNewWashingMachineStorageImplimentation()
    presenter = AddNewWashingMachinePresenterImplementation()

    interactor = AddNewWashingMachineInteractor(
        storage=storage,
        presenter=presenter
    )
    data = interactor.create_new_washing_machine(washing_machine_id=washing_machine_id)
    data = json.dumps(data)
    response = HttpResponse(data, status=200)
    return response