# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20180614_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='mirna',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mirna',
            name='accession',
            field=models.CharField(max_length=40),
        ),
    ]
