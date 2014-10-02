# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20141002_0304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='quorum',
            options={'ordering': ['-lunch', 'person'], 'verbose_name': 'Quorum', 'verbose_name_plural': 'Quorums'},
        ),
    ]
