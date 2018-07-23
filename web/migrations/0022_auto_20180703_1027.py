# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_auto_20180703_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancer',
            name='abbr',
            field=models.CharField(max_length=4, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cancer',
            name='name',
            field=models.CharField(max_length=70, default=''),
        ),
    ]
