# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20141006_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-active', '-visit_count', 'name'], 'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.AlterField(
            model_name='place',
            name='visit_count',
            field=models.IntegerField(default=0, verbose_name=b'Visit Count'),
        ),
    ]
