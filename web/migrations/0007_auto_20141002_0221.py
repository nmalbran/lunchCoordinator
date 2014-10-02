# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20141002_0220'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blacklist',
            unique_together=set([('person', 'place')]),
        ),
    ]
