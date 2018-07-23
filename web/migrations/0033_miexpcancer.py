# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_auto_20180705_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiexpCancer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('edin', models.PositiveIntegerField(default=0)),
                ('p0', models.DecimalField(max_digits=10, decimal_places=4)),
                ('p25', models.DecimalField(max_digits=10, decimal_places=4)),
                ('p50', models.DecimalField(max_digits=10, decimal_places=4)),
                ('p75', models.DecimalField(max_digits=10, decimal_places=4)),
                ('p100', models.DecimalField(max_digits=10, decimal_places=4)),
                ('mean', models.DecimalField(max_digits=10, decimal_places=4)),
                ('sd', models.DecimalField(max_digits=10, decimal_places=4)),
                ('is_tumor', models.PositiveSmallIntegerField()),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('miexp', models.ForeignKey(to='web.Mirna')),
            ],
        ),
    ]
