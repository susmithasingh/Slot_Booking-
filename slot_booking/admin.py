from django.contrib import admin
# your django admin
from .models import User
from .models import WashingMechine
admin.site.register(User)
admin.site.register(WashingMechine)