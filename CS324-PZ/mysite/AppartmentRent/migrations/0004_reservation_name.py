# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppartmentRent', '0003_auto_20170610_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
