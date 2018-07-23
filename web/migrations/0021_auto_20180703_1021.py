# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20180620_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEditCancer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('edited_in', models.PositiveIntegerField(default=0)),
                ('lev_mean', models.DecimalField(decimal_places=4, max_digits=5)),
                ('lev_med', models.DecimalField(decimal_places=4, max_digits=5)),
                ('is_tumor', models.BooleanField(default=True)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('site', models.ForeignKey(to='web.Site')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='hyper_A',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='level',
            name='hyper_G',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='level',
            name='redi_A',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='level',
            name='redi_G',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
    ]
