# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20141001_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quorum',
            name='lunch',
            field=models.CharField(default=b'n/a', max_length=5, verbose_name=b'Almuerza hoy?', choices=[(b'n/a', b'n/a'), (b'yes', b'yes'), (b'no', b'no')]),
        ),
    ]
