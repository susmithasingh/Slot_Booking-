from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface


class UpdateIssuesResolvedInteractor:
    def __init__(self, storage: GetReportedIssuesStorageInterface):
        self.storage = storage

    def update_issues_resolved_status(
            self, machine_id: int, is_resolved: bool):

        self.storage.update_issues_resolved_status(
            machine_id=machine_id,
            is_resolved=is_resolved)