# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_statistics', '0022_set_suggestion_submitters'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scorelog',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='scorelog',
            name='submission',
        ),
        migrations.RemoveField(
            model_name='scorelog',
            name='user',
        ),
        migrations.DeleteModel(
            name='ScoreLog',
        ),
    ]
