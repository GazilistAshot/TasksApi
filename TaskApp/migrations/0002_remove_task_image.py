# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-03 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
    ]
