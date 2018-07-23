# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_auto_20180705_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miexpcancer',
            name='site',
        ),
        migrations.AddField(
            model_name='miexpcancer',
            name='miexp',
            field=models.ForeignKey(default='', to='web.Mirna'),
            preserve_default=False,
        ),
    ]
