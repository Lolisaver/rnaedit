# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20180619_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gtexsample',
            fields=[
                ('scan', models.CharField(primary_key=True, default='', serialize=False, max_length=14)),
                ('tissue', models.CharField(default='', max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='rediLevel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nas', models.PositiveIntegerField(default=0)),
                ('ngs', models.PositiveIntegerField(default=0)),
                ('level', models.DecimalField(max_digits=3, decimal_places=2, null=True)),
                ('gcover', models.PositiveIntegerField(default=0)),
                ('gfreq', models.DecimalField(max_digits=3, decimal_places=2, null=True)),
                ('sample', models.ForeignKey(to='web.Gtexsample')),
            ],
        ),
        migrations.RenameField(
            model_name='site',
            old_name='hh19loc',
            new_name='hg19loc',
        ),
        migrations.AddField(
            model_name='site',
            name='hg19str',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='redilevel',
            name='site',
            field=models.ForeignKey(to='web.Site'),
        ),
    ]
