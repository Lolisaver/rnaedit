# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0043_auto_20180720_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteedincancer',
            name='edin5p',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='siteedincancer',
            name='p50p',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
