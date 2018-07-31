# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0054_auto_20180726_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='cox',
            name='coeff',
            field=models.DecimalField(max_digits=8, decimal_places=6, default=0),
            preserve_default=False,
        ),
    ]
