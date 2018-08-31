# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-08-31 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(blank=True, max_length=10000, null=True)),
                ('bill_details', models.CharField(blank=True, max_length=10000, null=True)),
                ('total_bill', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]