# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 15:24
from __future__ import unicode_literals


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cog', '0006_auto_20160303_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
