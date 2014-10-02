# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20141002_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quorum',
            name='person',
            field=models.ForeignKey(to='web.Person', unique=True),
        ),
    ]
