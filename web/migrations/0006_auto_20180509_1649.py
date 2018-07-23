# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20180509_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='bind',
            name='mir',
            field=models.ForeignKey(default='', to='web.Mirna'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bind',
            name='energy',
            field=models.DecimalField(max_digits=7, decimal_places=3, null=True),
        ),
        migrations.AlterField(
            model_name='bind',
            name='score',
            field=models.DecimalField(max_digits=7, decimal_places=3, null=True),
        ),
        migrations.AlterField(
            model_name='mirna',
            name='accession',
            field=models.CharField(default='', max_length=40),
        ),
    ]
