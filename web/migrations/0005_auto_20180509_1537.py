# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180509_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='location',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='region',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='conserve',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='site',
            name='gene',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterField(
            model_name='site',
            name='repetitive',
            field=models.CharField(max_length=20),
        ),
    ]
