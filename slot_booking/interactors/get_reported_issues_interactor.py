from slot_booking.interactors.presenters.reported_issues_presenter_interface import \
    GetReportedIssuesPresenterInterface
from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface


class GetReportedIssuesInteractor:

    def __init__(self,storage: GetReportedIssuesStorageInterface, presenter: GetReportedIssuesPresenterInterface
                 ):
        self.storage= storage
        self.presenter = presenter

    def get_reported_issues(self, offset: int, limit: int):

        # is_valid_offset = self.storage.is_valid_offset(
        #     offset=offset
        # )
        # not_valid_offset = not is_valid_offset
        #
        # if not_valid_offset:
        #     self.presenter.raise_invalid_offset_exception()
        #     return
        #
        # is_valid_limit = self.storage.is_valid_limit(
        #     limit=limit
        # )
        # not_valid_limit = not is_valid_limit
        #
        # if not_valid_limit:
        #     self.presenter.raise_invalid_limit_exception()
        #     return

        # TODO get all the reported issues
        list_of_issues = self.storage.get_all_reported_issues(offset=offset, limit=limit)
        total_no_of_issues = self.storage.get_total_number_of_issues()

        return self.presenter.get_all_reported_issues_response(list_of_issues, total_no_of_issues)
