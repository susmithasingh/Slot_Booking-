from django.http import HttpResponse

from raven.utils import json

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass

from slot_booking.interactors.user_login_details_interactor import  \
    UserLoginInteractor

from slot_booking.storages.user_login_storage_implimentation import \
    UserLoginStorageImplimentation

from slot_booking.presenters.user_login_presenter_implementation import \
        LoginDetailsPresenterImplementation

from django_swagger_utils.drf_server.exceptions import BadRequest

from common.oauth2_storage import OAuth2SQLStorage

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    username = request_data["username"]
    password = request_data["password"]

    storage = UserLoginStorageImplimentation()
    presenter = LoginDetailsPresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
    )

    response = interactor.user_login_interactor(
        username=username,
        password=password)
    # print(response)
    # data = json.dumps({"response": response})
    # response = HttpResponse(data, status=200)
    return response