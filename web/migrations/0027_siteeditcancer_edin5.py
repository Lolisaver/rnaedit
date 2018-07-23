# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_auto_20180703_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteeditcancer',
            name='edin5',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
