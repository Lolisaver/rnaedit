# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0047_auto_20180720_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteedincancer',
            old_name='edin5p',
            new_name='edin',
        ),
        migrations.RemoveField(
            model_name='siteedincancer',
            name='p50p',
        ),
        migrations.AddField(
            model_name='siteedincancer',
            name='mean',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
