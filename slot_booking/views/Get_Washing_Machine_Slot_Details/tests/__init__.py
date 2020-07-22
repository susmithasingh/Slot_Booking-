# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Get_Washing_Machine_Slot_Details"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/washing_machine_slot_details/{washing_machine_id}/{day}/"

from .test_case_01 import TestCase01GetWashingMachineSlotDetailsAPITestCase

__all__ = [
    "TestCase01GetWashingMachineSlotDetailsAPITestCase"
]
