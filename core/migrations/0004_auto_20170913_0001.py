# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170912_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booked',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]