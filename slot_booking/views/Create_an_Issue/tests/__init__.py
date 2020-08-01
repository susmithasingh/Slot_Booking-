# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Create_an_Issue"
REQUEST_METHOD = "post"
URL_SUFFIX = "report/issue/"

from .test_case_01 import TestCase01CreateAnIssueAPITestCase

__all__ = [
    "TestCase01CreateAnIssueAPITestCase"
]
