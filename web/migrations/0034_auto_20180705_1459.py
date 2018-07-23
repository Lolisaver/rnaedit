# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_miexpcancer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miexpcancer',
            old_name='miexp',
            new_name='mirna',
        ),
    ]
