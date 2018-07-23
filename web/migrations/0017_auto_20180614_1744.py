# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20180614_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mirna',
            name='id',
        ),
        migrations.AlterField(
            model_name='mirna',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
