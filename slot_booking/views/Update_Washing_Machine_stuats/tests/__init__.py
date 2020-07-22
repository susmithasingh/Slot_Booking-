# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Update_Washing_Machine_stuats"
REQUEST_METHOD = "put"
URL_SUFFIX = "update/washing_machine_status/"

from .test_case_01 import TestCase01UpdateWashingMachineStuatsAPITestCase

__all__ = [
    "TestCase01UpdateWashingMachineStuatsAPITestCase"
]
