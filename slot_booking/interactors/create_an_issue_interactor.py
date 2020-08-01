from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface

from slot_booking.interactors.presenters.reported_issues_presenter_interface import \
    GetReportedIssuesPresenterInterface


class CreateIssueInteractor:
    def __init__(self, storage: GetReportedIssuesStorageInterface, presenter: GetReportedIssuesPresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_an_issue(self, issue: str):
        is_valid_issue = self.storage.validate_issue(issue=issue)
        if not is_valid_issue:
            self.presenter.raise_invalid_issue_exception()
            return
        self.storage.create_issue(issue=issue)