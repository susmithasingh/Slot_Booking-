from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json

from .validator_class import ValidatorClass
from slot_booking.presenters.get_all_washing_mechine_details_presenter_implimentation import \
    GetWashingMachineDetailsPresenterImplementation

from ...interactors.get_all_washing_machine_details_interactors import GetWashingMachineDetailsInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    presenter = GetWashingMachineDetailsPresenterImplementation()
    interactor = GetWashingMachineDetailsInteractor(
        presenter=presenter
    )

    data = interactor.get_washing_machine_details()
    print(data)
    data = json.dumps(data)
    response = HttpResponse(data, status=200)
    print(response.content)
    return response.content