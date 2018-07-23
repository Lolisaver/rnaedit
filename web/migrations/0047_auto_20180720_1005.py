# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0046_auto_20180720_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteedincancer',
            name='edin5p',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
