# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customer_review_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='review_by',
            new_name='reviewed_by',
        ),
    ]
