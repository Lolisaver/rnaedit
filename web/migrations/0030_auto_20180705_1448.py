# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_miexpcancer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miexpcancer',
            name='mean',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='miexpcancer',
            name='p0',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='miexpcancer',
            name='p100',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='miexpcancer',
            name='p25',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='miexpcancer',
            name='p50',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='miexpcancer',
            name='p75',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='miexpcancer',
            name='sd',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
    ]
