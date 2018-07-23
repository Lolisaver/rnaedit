# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0035_auto_20180709_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEdin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('edin', models.PositiveIntegerField(default=0)),
                ('edin5', models.PositiveIntegerField(default=0)),
                ('p50', models.DecimalField(max_digits=5, decimal_places=4)),
                ('mean', models.DecimalField(max_digits=5, decimal_places=4)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('site', models.ForeignKey(to='web.Site')),
            ],
        ),
        migrations.RemoveField(
            model_name='siteedincancer',
            name='p0',
        ),
        migrations.RemoveField(
            model_name='siteedincancer',
            name='p100',
        ),
        migrations.RemoveField(
            model_name='siteedincancer',
            name='p25',
        ),
        migrations.RemoveField(
            model_name='siteedincancer',
            name='p75',
        ),
        migrations.RemoveField(
            model_name='siteedincancer',
            name='sd',
        ),
    ]
