# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150722_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tests',
        ),
        migrations.AddField(
            model_name='article',
            name='service',
            field=models.ManyToManyField(related_name='service', to='main.Service'),
        ),
    ]
