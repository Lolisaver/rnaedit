# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20180704_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiexpCancer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('edin', models.PositiveIntegerField(default=0)),
                ('p0', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p25', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p50', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p75', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p100', models.DecimalField(decimal_places=4, max_digits=5)),
                ('mean', models.DecimalField(decimal_places=4, max_digits=5)),
                ('sd', models.DecimalField(decimal_places=4, max_digits=5)),
                ('is_tumor', models.PositiveSmallIntegerField()),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('site', models.ForeignKey(to='web.Site')),
            ],
        ),
    ]
