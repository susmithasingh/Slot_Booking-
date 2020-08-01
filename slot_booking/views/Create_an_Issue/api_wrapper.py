from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.storages.reported_issues_storage_implimentation import GetReportedIssuesStorageImplementation
from slot_booking.interactors.create_an_issue_interactor import CreateIssueInteractor

from slot_booking.presenters.reported_issues_presenter_implementation import GetReportedIssuesPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    
    request_data = kwargs["request_data"]
    issue = request_data["issue"]
    
    storage = GetReportedIssuesStorageImplementation()
    presenter = GetReportedIssuesPresenterImplementation()
    
    interactor = CreateIssueInteractor(
        storage=storage,
        presenter=presenter
    )
    
    interactor.create_an_issue(issue=issue)

    response = HttpResponse(status=200)
    return response
