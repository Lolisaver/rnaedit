# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180502_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bind',
            old_name='score1',
            new_name='score',
        ),
        migrations.RemoveField(
            model_name='bind',
            name='gubind',
        ),
        migrations.RemoveField(
            model_name='bind',
            name='mismatches',
        ),
        migrations.RemoveField(
            model_name='bind',
            name='score2',
        ),
        migrations.AddField(
            model_name='bind',
            name='binder',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bind',
            name='miseq',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bind',
            name='mseq',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bind',
            name='seed_type',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bind',
            name='utr',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
