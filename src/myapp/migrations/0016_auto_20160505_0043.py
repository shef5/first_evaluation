# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-04 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20160504_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='d_a',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='url',
            name='p_a',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
