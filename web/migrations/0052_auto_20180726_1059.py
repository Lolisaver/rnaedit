# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0051_siteedintn'),
    ]

    operations = [
        migrations.CreateModel(
            name='siteAnno',
            fields=[
                ('site', models.OneToOneField(serialize=False, primary_key=True, to='web.Site')),
                ('tumor33', models.DecimalField(null=True, decimal_places=2, max_digits=4)),
                ('normal33', models.DecimalField(null=True, decimal_places=2, max_digits=4)),
                ('radar', models.BooleanField(default=False)),
                ('darned', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='siteedintn',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='siteedintn',
            name='site',
        ),
        migrations.AddField(
            model_name='siteedincancer',
            name='edin',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='siteedincancer',
            name='mean',
            field=models.DecimalField(max_digits=5, decimal_places=4, default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SiteEdinTN',
        ),
    ]
