# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppartmentRent', '0011_auto_20170624_1802'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]