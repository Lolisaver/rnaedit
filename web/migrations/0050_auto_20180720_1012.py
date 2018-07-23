# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0049_auto_20180720_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteedintn',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='siteedintn',
            name='site',
        ),
        migrations.DeleteModel(
            name='SiteEdinTN',
        ),
    ]
