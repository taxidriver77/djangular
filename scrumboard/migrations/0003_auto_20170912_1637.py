# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 16:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20170912_1629'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cards',
            new_name='Card',
        ),
    ]
