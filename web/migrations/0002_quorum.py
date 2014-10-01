# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quorum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(unique=True, editable=False, name=b'uuid', blank=True)),
                ('lunch', models.IntegerField(default=0, choices=[(0, b'n/a'), (1, b'yes'), (2, b'no')])),
                ('person', models.ForeignKey(to='web.Person')),
            ],
            options={
                'verbose_name': 'Quorum',
                'verbose_name_plural': 'Quorums',
            },
            bases=(models.Model,),
        ),
    ]
