# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-13 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reit',
            name='reit',
            field=models.IntegerField(max_length=5, verbose_name='Рейтинг'),
        ),
    ]
