# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 15:50
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20160227_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_on_new',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
