# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='social',
        ),
        migrations.AddField(
            model_name='contact',
            name='vkontakte',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='keywords',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
