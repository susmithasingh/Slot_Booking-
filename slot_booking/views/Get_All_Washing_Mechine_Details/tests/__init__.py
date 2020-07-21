# pylint: disable=wrong-import-position

APP_NAME = "slot_booking"
OPERATION_NAME = "Get_All_Washing_Mechine_Details"
REQUEST_METHOD = "get"
URL_SUFFIX = "get/all_washing_mechine_detalis/"

from .test_case_01 import TestCase01GetAllWashingMechineDetailsAPITestCase

__all__ = [
    "TestCase01GetAllWashingMechineDetailsAPITestCase"
]
