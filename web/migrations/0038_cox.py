# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_site_cosmic'),
    ]

    operations = [
        migrations.CreateModel(
            name='cox',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('p', models.DecimalField(max_digits=10, decimal_places=9)),
                ('fdr', models.DecimalField(max_digits=10, decimal_places=9)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('site', models.ForeignKey(to='web.Site')),
            ],
        ),
    ]
