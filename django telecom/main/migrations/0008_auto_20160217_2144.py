# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 18:44
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160217_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
