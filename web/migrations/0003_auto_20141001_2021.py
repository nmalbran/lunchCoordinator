# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_quorum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quorum',
            name='id',
        ),
        migrations.AlterField(
            model_name='quorum',
            name='uuid',
            field=django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, name=b'uuid'),
        ),
    ]
