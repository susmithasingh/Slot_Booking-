from slot_booking.interactors.storages.reported_isues_storage_interface import \
    GetReportedIssuesStorageInterface
from slot_booking.models import Issues


class GetReportedIssuesStorageImplementation(GetReportedIssuesStorageInterface):

    # def is_valid_offset(self, offset: int) -> bool:
    #
    #     if offset < 0:
    #         return False
    #     else:
    #         return True
    #
    # def is_valid_limit(self, limit: int) -> bool:
    #     if limit >= 10:
    #         return False
    #     else:
    #         return True

    def get_all_reported_issues(self, offset: int, limit: int):
        issue_data = Issues.objects.all()
        data = issue_data[offset:offset+limit]
        reported_issues =[]
        for issues in data:
            print(issues)
            print("%%%%%%%%%%%%%%%%%*****************")
            print(type(issues))
            all_reported_issues = {}
            all_reported_issues["issue"] = issues.issue
            all_reported_issues["reported_date_time"] = str(issues.reported_date_time)
            all_reported_issues["is_resolved"] = issues.is_resolved
            reported_issues.append(all_reported_issues)
        return reported_issues

    def update_issues_resolved_status(self, machine_id: int, is_resolved: bool):

        Issues.objects.filter(id=machine_id).update(is_resolved=is_resolved)

    def create_issue(self, issue: str):
        Issues.objects.create(issue=issue)

    def get_total_number_of_issues(self):
        print("%%%%%%%%%%%%%%%%%%55")
        return len(Issues.objects.all())


