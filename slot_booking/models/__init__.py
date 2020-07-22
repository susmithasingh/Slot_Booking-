from .User_model import User
from .issues import Issues
from .washing_mechine import WashingMechine
from .washing_mechine_slots import WashingMachineSlots

__all__ = ["User", "WashingMechine", "WashingMachineSlots", "Issues"]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique

#         :var value: String field which will be of 128 char length