# Generated by Django 4.2.1 on 2023-05-24 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0003_register_aadhar_register_confirmpasswd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='date1',
            field=models.DateField(default=datetime.date(2023, 5, 24)),
        ),
    ]
