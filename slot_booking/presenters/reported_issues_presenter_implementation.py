from typing import List

from slot_booking.interactors.presenters.reported_issues_presenter_interface import \
    GetReportedIssuesPresenterInterface


class GetReportedIssuesPresenterImplementation(GetReportedIssuesPresenterInterface):

    def get_all_reported_issues_response(self, list_of_reported_issues: List[dict]):

        return list_of_reported_issues