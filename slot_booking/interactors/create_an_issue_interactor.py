from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface


class CreateIssueInteractor:
    def __init__(self, storage:GetReportedIssuesStorageInterface):
        self.storage = storage

    def create_an_issue(self, issue: str):
        self.storage.create_issue(issue=issue)