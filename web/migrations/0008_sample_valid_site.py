# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_miexp'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='valid_site',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
