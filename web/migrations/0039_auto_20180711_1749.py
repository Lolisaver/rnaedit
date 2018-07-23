# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0038_cox'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancer',
            name='normalSample',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cancer',
            name='tumorSample',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
