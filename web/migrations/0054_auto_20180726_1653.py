# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0053_auto_20180726_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteanno',
            name='edinn',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='siteanno',
            name='edint',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
