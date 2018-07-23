# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0031_auto_20180705_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miexpcancer',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='miexpcancer',
            name='miexp',
        ),
        migrations.DeleteModel(
            name='MiexpCancer',
        ),
    ]
