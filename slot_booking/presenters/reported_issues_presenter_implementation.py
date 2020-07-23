from typing import List

from django_swagger_utils.drf_server.exceptions import NotFound
from slot_booking.interactors.presenters.reported_issues_presenter_interface import \
    GetReportedIssuesPresenterInterface

from slot_booking.constants.exception_messages import INVALID_OFFSET, INVALID_LIMIT


class GetReportedIssuesPresenterImplementation(GetReportedIssuesPresenterInterface):

    def get_all_reported_issues_response(self, list_of_reported_issues: List[dict], total_no_of_issues: int):

        return {
            "total_no_of_issues": total_no_of_issues,
            "list_of_issues": list_of_reported_issues
        }



    # def raise_invalid_offset_exception(self):
    #     raise NotFound(*INVALID_OFFSET)
    #
    # def raise_invalid_limit_exception(self):
    #     raise NotFound(*INVALID_LIMIT)