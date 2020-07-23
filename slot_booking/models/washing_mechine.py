from django.db import models
class WashingMechine(models.Model):
    washing_machine_id = models.IntegerField()
    is_active = models.BooleanField(default = True)
    washing_machine_image = models.URLField()