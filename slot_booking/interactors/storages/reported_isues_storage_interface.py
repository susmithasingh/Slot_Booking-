from abc import ABC
from abc import abstractmethod
from typing import List


class GetReportedIssuesStorageInterface(ABC):

    @abstractmethod
    def get_all_reported_issues(self,offset: int, limit: int) -> List[dict]:
        pass

    @abstractmethod
    def update_issues_resolved_status(
            self,
            machine_id: int,
            is_resolved: bool):
        pass

    @abstractmethod
    def create_issue(self, issue: str):
        pass

    # @abstractmethod
    # def is_valid_offset(self, offset: int):
    #     pass
    #
    # @abstractmethod
    # def is_valid_limit(self, limit: int):
    #     pass

    @abstractmethod
    def get_total_number_of_issues(self):
        pass