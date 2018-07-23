# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20180509_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miexp',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('exp', models.DecimalField(max_digits=10, decimal_places=3)),
                ('mir', models.ForeignKey(to='web.Mirna')),
                ('sample', models.ForeignKey(to='web.Sample')),
            ],
        ),
    ]
