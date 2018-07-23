# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_auto_20180703_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancer',
            old_name='name',
            new_name='full',
        ),
    ]
