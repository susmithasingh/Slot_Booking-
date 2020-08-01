from .User_model import User
from .date_range import DateRange
from .issues import Issues
from .washing_mechine import WashingMechine
from .washing_mechine_slots import WashingMachineSlots

__all__ = [
        "User",
        "WashingMechine",
        "WashingMachineSlots",
        "Issues",
        "DateRange"]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique

#         :var value: String field which will be of 128 char length