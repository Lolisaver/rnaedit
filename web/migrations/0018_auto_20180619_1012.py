# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20180614_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='hg19chr',
            field=models.CharField(max_length=30, default='chr0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='hh19loc',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
