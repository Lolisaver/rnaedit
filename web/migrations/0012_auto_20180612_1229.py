# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20180612_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='clin_id',
        ),
        migrations.AddField(
            model_name='site',
            name='clin_cc',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
