# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0003_auto_20170912_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, help_text='Here is a description'),
        ),
    ]
