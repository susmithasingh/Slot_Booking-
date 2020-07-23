# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Update_Issues_status"
REQUEST_METHOD = "put"
URL_SUFFIX = "update/issues/is_resolved/"

from .test_case_01 import TestCase01UpdateIssuesStatusAPITestCase

__all__ = [
    "TestCase01UpdateIssuesStatusAPITestCase"
]
