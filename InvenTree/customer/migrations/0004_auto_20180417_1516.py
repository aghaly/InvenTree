# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20180417_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]