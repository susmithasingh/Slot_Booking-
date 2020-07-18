# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "get_access_Token"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/"

from .test_case_01 import TestCase01GetAccessTokenAPITestCase

__all__ = [
    "TestCase01GetAccessTokenAPITestCase"
]
