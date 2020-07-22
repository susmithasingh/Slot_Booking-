from django.db import models

from slot_booking.constants.enums import ListOfDays
from slot_booking.models import WashingMechine


class WashingMachineSlots(models.Model):
     washing_machine = models.ForeignKey(WashingMechine, on_delete=models.CASCADE)
     DAYS = [(day.value, day.value) for day in ListOfDays]
     slots = models.CharField(max_length=20)
     from_time = models.TimeField()
     to_time = models.TimeField()
     day = models.CharField(choices=DAYS, max_length=20)
