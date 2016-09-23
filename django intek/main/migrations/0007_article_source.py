# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150722_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
