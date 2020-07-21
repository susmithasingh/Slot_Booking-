# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Create_New_Washing_Mechine"
REQUEST_METHOD = "post"
URL_SUFFIX = "add/new_washing_mechine/"

from .test_case_01 import TestCase01CreateNewWashingMechineAPITestCase

__all__ = [
    "TestCase01CreateNewWashingMechineAPITestCase"
]
