# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150722_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='service',
        ),
        migrations.AddField(
            model_name='article',
            name='tests',
            field=models.ManyToManyField(related_name='sss', to='main.Service'),
        ),
    ]
