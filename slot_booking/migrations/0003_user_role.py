# Generated by Django 2.2.1 on 2020-07-31 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slot_booking', '0002_auto_20200723_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.BooleanField(default=False),
        ),
    ]
