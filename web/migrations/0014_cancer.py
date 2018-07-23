# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20180612_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancer',
            fields=[
                ('cancer_id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
    ]
