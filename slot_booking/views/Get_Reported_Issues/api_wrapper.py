from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json

from .validator_class import ValidatorClass
from slot_booking.storages.reported_issues_storage_implimentation import GetReportedIssuesStorageImplementation

from slot_booking.presenters.reported_issues_presenter_implementation import GetReportedIssuesPresenterImplementation

from slot_booking.interactors.get_reported_issues_interactor import GetReportedIssuesInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    presenter = GetReportedIssuesPresenterImplementation()
    storage = GetReportedIssuesStorageImplementation()

    interactor = GetReportedIssuesInteractor(
        storage=storage,
        presenter=presenter
    )
    data = interactor.get_reported_issues()
    print(data)
    data = json.dumps(data)
    response = HttpResponse(data, status=200)
    return response