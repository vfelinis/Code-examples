# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_article_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'Social',
            },
        ),
    ]
