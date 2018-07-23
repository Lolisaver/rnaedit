# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_auto_20180703_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancer',
            name='cancer_id',
        ),
        migrations.AlterField(
            model_name='cancer',
            name='abbr',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
    ]
