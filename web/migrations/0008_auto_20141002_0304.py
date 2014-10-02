# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20141002_0221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['name'], 'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
    ]
