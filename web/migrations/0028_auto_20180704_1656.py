# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_siteeditcancer_edin5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteeditcancer',
            name='is_tumor',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
