# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0041_auto_20180713_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiexpNormal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('edin', models.PositiveIntegerField(default=0)),
                ('p50', models.DecimalField(max_digits=10, decimal_places=4)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('mirna', models.ForeignKey(to='web.Mirna')),
            ],
        ),
        migrations.CreateModel(
            name='MiexpTumor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('edin', models.PositiveIntegerField(default=0)),
                ('p50', models.DecimalField(max_digits=10, decimal_places=4)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('mirna', models.ForeignKey(to='web.Mirna')),
            ],
        ),
    ]
