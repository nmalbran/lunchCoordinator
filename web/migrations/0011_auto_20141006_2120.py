# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20141002_0525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-active', 'name'], 'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.AddField(
            model_name='place',
            name='visit_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
