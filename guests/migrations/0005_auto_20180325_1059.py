# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-25 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_weddingguest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingguest',
            name='food',
            field=models.IntegerField(choices=[(1, 'Normalne'), (2, 'Wegetariańskie')], null=True),
        ),
        migrations.AlterField(
            model_name='weddingguest',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]