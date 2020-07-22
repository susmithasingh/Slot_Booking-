from slot_booking.interactors.presenters.reported_issues_presenter_interface import \
    GetReportedIssuesPresenterInterface
from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface


class GetReportedIssuesInteractor:
    def __init__(self,storage: GetReportedIssuesStorageInterface, presenter: GetReportedIssuesPresenterInterface
                 ):
        self.storage= storage
        self.presenter = presenter

    def get_reported_issues(self):

        # TODO get all the reported isseus
        list_of_isssues = self.storage.get_all_reported_issues()

        return self.presenter.get_all_reported_issues_response(list_of_isssues)