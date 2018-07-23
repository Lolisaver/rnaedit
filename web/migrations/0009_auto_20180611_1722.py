# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_sample_valid_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='clinvar',
            field=models.CharField(default='.', max_length=20),
        ),
        migrations.AddField(
            model_name='site',
            name='exac',
            field=models.CharField(default='.', max_length=20),
        ),
        migrations.AddField(
            model_name='site',
            name='gg',
            field=models.CharField(default='.', max_length=20),
        ),
        migrations.AddField(
            model_name='site',
            name='intervar',
            field=models.CharField(default='.', max_length=20),
        ),
        migrations.AlterField(
            model_name='site',
            name='snp_id',
            field=models.CharField(default='.', max_length=20),
        ),
    ]
