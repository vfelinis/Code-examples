# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='service',
            field=models.ManyToManyField(related_name='service', to='main.Service'),
        ),
    ]
