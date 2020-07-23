from abc import ABC
from abc import abstractmethod
from typing import List


class GetReportedIssuesPresenterInterface(ABC):
    @abstractmethod
    def get_all_reported_issues_response(self, list_of_reported_issues: List[dict], total_number_of_issues: int):
        pass

    # @abstractmethod
    # def raise_invalid_offset_exception(self):
    #     pass
    #
    # @abstractmethod
    # def raise_invalid_limit_exception(self):
    #     pass