# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150722_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='service',
        ),
        migrations.AddField(
            model_name='article',
            name='services',
            field=models.ManyToManyField(blank=True, to='main.Service', related_name='services'),
        ),
    ]
