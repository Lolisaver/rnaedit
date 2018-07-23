# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0036_auto_20180709_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='cosmic',
            field=models.CharField(default='.', max_length=15),
        ),
    ]
