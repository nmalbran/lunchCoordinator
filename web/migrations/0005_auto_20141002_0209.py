# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20141001_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.ForeignKey(to='web.Person')),
                ('place', models.ForeignKey(to='web.Place')),
            ],
            options={
                'verbose_name': 'BlackList',
                'verbose_name_plural': 'BlackLists',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='quorum',
            options={'ordering': ['-lunch'], 'verbose_name': 'Quorum', 'verbose_name_plural': 'Quorums'},
        ),
        migrations.AlterField(
            model_name='place',
            name='info',
            field=models.TextField(blank=True),
        ),
    ]
