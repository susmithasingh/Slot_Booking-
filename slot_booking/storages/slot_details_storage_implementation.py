from typing import List
from datetime import datetime

from slot_booking.interactors.storages.slots_storage_interafce import UserSlotDetailsInterface


class UserSlotDetailsStorageImplementation(UserSlotDetailsInterface):

    def get_available_slots(self, dates: List) -> List[dict]:

        # TODO convert date into day
        days = []
        for date in dates:
            days.append(date.strftime('%A'))

        # TODO  get_slots for particular day
        for day in days :
            day_slots = {}
            slots = WashingMachineSlots.objcts.filter(day=day)





