# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0050_auto_20180720_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEdinTN',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('edin5', models.PositiveIntegerField(default=0)),
                ('edin5p', models.PositiveIntegerField(default=0)),
                ('p50', models.DecimalField(max_digits=5, decimal_places=4)),
                ('p50p', models.PositiveIntegerField(default=0)),
                ('tumor', models.NullBooleanField(default=None)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('site', models.ForeignKey(to='web.Site')),
            ],
        ),
    ]
