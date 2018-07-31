# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0056_siteanno_has_cox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miexp',
            name='exp',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
