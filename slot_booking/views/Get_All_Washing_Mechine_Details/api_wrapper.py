from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json

from .validator_class import ValidatorClass
from ...interactors.get_all_washing_machine_details_interactors import GetWashingMachineDetailsInteractor
from ...presenters.get_all_washing_mechine_details_presenter_implimentation import \
    GetWashingMachineDetailsPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    presenter = GetWashingMachineDetailsPresenterImplementation()

    interactor = GetWashingMachineDetailsInteractor(
        presenter=presenter
    )

    data = interactor.get_washing_machine_details()
    print(data)

    data1 = json.dumps(data)
    print('**************')
    print(data1)
    print("******************")
    response =  HttpResponse(data1, status=200)
    return response
    #
    # print("************************")
    # print(response.content)
    #
    # return response.content
