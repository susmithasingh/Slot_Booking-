# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Get_Reported_Issues"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/reported_issues/"

from .test_case_01 import TestCase01GetReportedIssuesAPITestCase

__all__ = [
    "TestCase01GetReportedIssuesAPITestCase"
]
