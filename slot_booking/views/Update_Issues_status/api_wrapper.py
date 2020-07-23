from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from slot_booking.interactors.update_issues_resolved_interactor import \
    UpdateIssuesResolvedInteractor

from slot_booking.storages.reported_issues_storage_implimentation import \
    GetReportedIssuesStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data = kwargs["request_data"]

    machine_id = request_data["machine_id"]
    is_resolved = request_data["is_resolved"]
    storage = GetReportedIssuesStorageImplementation()

    interactor = UpdateIssuesResolvedInteractor(
        storage=storage
    )
    interactor.update_issues_resolved_status(
        machine_id=machine_id,
        is_resolved=is_resolved)

    response = HttpResponse(status=200)

    return response