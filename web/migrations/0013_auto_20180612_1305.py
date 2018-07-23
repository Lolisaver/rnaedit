# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20180612_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='clin_cc',
        ),
        migrations.AddField(
            model_name='site',
            name='clin',
            field=models.CharField(max_length=20, default='.'),
        ),
    ]
