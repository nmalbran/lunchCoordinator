# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20141002_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
