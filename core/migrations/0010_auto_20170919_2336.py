# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 20:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170919_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
