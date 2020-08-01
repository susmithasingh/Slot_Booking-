from datetime import timedelta, date, datetime

from slot_booking.models import DateRange

from slot_booking.interactors.storages.slots_storage_interafce import UserSlotDetailsInterface


class GetAvailableSlotsInteractor:

    def __init__(
            self,
            storage: UserSlotDetailsInterface,
            presenter):
        self.storage = storage,
        self.presenter = presenter

    def get_all_available_slots(self):

        # TODO find consicutive date
        ranges = DateRange.objects.all()
        date_range = ranges[0].range
        dates = []
        for daterange in range(0, date_range):
            d = date.today() + timedelta(days=daterange)
            dates.append(d)

        # TODO gte the slots in date
        available_slots = self.storage.get_available_slots(dates)
