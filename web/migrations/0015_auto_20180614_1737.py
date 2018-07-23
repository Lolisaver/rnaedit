# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_cancer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mirna',
            name='accession',
            field=models.CharField(primary_key=True, max_length=40, serialize=False),
        ),
        migrations.AlterField(
            model_name='mirna',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
