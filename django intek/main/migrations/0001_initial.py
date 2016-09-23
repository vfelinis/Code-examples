# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'About',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=100)),
                ('phone2', models.CharField(blank=True, max_length=100)),
                ('phone3', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'Home',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('media_file', models.FileField(blank=True, upload_to='')),
                ('text', models.TextField()),
                ('price', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'Service',
            },
        ),
    ]
