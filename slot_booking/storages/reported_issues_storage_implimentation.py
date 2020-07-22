from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface
from slot_booking.models import Issues


class GetReportedIssuesStorageImplementation(GetReportedIssuesStorageInterface):

    def get_all_reported_issues(self):
        data = Issues.objects.all()
        reported_issues =[]
        for issues in data:
            all_reported_issues = {}
            all_reported_issues["issue"] = issues.issue
            all_reported_issues["reported_date_time"] = str(issues.reported_date_time)
            all_reported_issues["is_resolved"] = issues.is_resolved
            reported_issues.append(all_reported_issues)
        return reported_issues
