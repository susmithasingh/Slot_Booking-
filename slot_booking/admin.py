from django.contrib import admin
# your django admin
from .models import User, WashingMachineSlots, Issues, DateRange
from .models import WashingMechine
admin.site.register(User)
admin.site.register(WashingMechine)
admin.site.register(WashingMachineSlots)
admin.site.register(Issues)
admin.site.register(DateRange)