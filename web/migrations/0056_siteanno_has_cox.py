# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0055_cox_coeff'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteanno',
            name='has_cox',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
