# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20180619_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='utr',
        ),
        migrations.AddField(
            model_name='site',
            name='aa',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
