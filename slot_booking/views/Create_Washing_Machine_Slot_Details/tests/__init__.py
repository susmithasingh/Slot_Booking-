# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Create_Washing_Machine_Slot_Details"
REQUEST_METHOD = "post"
URL_SUFFIX = "create/washing_machine_slot_details/"

from .test_case_01 import TestCase01CreateWashingMachineSlotDetailsAPITestCase

__all__ = [
    "TestCase01CreateWashingMachineSlotDetailsAPITestCase"
]
