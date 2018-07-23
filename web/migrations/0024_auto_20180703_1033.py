# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20180703_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancer',
            name='abbr',
            field=models.CharField(max_length=4, default=''),
        ),
    ]
