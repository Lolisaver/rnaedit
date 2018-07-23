# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_auto_20180703_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteeditcancer',
            old_name='edited_in',
            new_name='edin',
        ),
        migrations.RenameField(
            model_name='siteeditcancer',
            old_name='lev_mean',
            new_name='mean',
        ),
        migrations.RenameField(
            model_name='siteeditcancer',
            old_name='lev_med',
            new_name='p50',
        ),
        migrations.AddField(
            model_name='siteeditcancer',
            name='p0',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteeditcancer',
            name='p100',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteeditcancer',
            name='p25',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteeditcancer',
            name='p75',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteeditcancer',
            name='sd',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=5),
            preserve_default=False,
        ),
    ]
