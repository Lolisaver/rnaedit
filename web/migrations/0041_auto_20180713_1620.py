# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0040_siteedinnormal_siteedintumor'),
    ]

    operations = [
        migrations.AddField(
            model_name='mirna',
            name='p5',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mirna',
            name='p50',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mirna',
            name='p95',
            field=models.DecimalField(default=0, decimal_places=4, max_digits=10),
            preserve_default=False,
        ),
    ]
