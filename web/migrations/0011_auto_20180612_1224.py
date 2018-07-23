# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20180612_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='intervar',
            field=models.CharField(max_length=20, default='.'),
        ),
    ]
