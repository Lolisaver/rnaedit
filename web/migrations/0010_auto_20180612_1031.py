# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20180611_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='clinvar',
            new_name='clin_id',
        ),
        migrations.RemoveField(
            model_name='level',
            name='hyper_A',
        ),
        migrations.RemoveField(
            model_name='level',
            name='hyper_C',
        ),
        migrations.RemoveField(
            model_name='level',
            name='hyper_G',
        ),
        migrations.RemoveField(
            model_name='level',
            name='hyper_T',
        ),
        migrations.RemoveField(
            model_name='level',
            name='redi_A',
        ),
        migrations.RemoveField(
            model_name='level',
            name='redi_C',
        ),
        migrations.RemoveField(
            model_name='level',
            name='redi_G',
        ),
        migrations.RemoveField(
            model_name='level',
            name='redi_T',
        ),
        migrations.AddField(
            model_name='site',
            name='clin_dbn',
            field=models.CharField(default='', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='clin_sig',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='site',
            name='exac',
            field=models.DecimalField(decimal_places=8, null=True, max_digits=8),
        ),
        migrations.AlterField(
            model_name='site',
            name='gg',
            field=models.DecimalField(decimal_places=8, null=True, max_digits=8),
        ),
        migrations.AlterField(
            model_name='site',
            name='intervar',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
