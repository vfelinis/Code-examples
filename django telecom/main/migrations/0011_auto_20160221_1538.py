# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-21 12:38
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160218_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='address_1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_1_foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_1_map',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_2_foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_2_map',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_3',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_3_foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_3_map',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_4',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_4_foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='address_4_map',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='contact',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
