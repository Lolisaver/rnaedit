# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0042_miexpnormal_miexptumor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteedincancer',
            old_name='edin',
            new_name='edin5p',
        ),
        migrations.RenameField(
            model_name='siteedincancer',
            old_name='mean',
            new_name='p50p',
        ),
    ]
