from abc import ABC
from abc import abstractmethod
from typing import List


class GetReportedIssuesStorageInterface(ABC):

    @abstractmethod
    def get_all_reported_issues(self) -> List[dict]:
        pass