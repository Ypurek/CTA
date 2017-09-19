# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 20:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=12)),
                ('percent', models.IntegerField(verbose_name='discount percentage')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Features')),
                ('performance_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Performance')),
            ],
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('message', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=16)),
                ('date', models.DateField(verbose_name='date of performance')),
                ('time', models.TimeField(verbose_name='time of perormance')),
                ('price', models.FloatField(verbose_name='price')),
                ('booked', models.DateTimeField(verbose_name='booked when')),
                ('booked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booked_by', to=settings.AUTH_USER_MODEL)),
                ('bought_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bought_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('birth_day', models.DateField(verbose_name='birth date')),
                ('image', models.ImageField(upload_to='', verbose_name='photo')),
                ('amount', models.IntegerField(verbose_name='money')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tickethistory',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tickets'),
        ),
        migrations.AddField(
            model_name='discount',
            name='ticket_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Tickets'),
        ),
    ]