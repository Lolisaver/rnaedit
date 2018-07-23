# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_auto_20180705_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteEdinCancer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('edin', models.PositiveIntegerField(default=0)),
                ('edin5', models.PositiveIntegerField(default=0)),
                ('p0', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p25', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p50', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p75', models.DecimalField(decimal_places=4, max_digits=5)),
                ('p100', models.DecimalField(decimal_places=4, max_digits=5)),
                ('mean', models.DecimalField(decimal_places=4, max_digits=5)),
                ('sd', models.DecimalField(decimal_places=4, max_digits=5)),
                ('tumor', models.NullBooleanField(default=None)),
                ('cancer', models.ForeignKey(to='web.Cancer')),
                ('site', models.ForeignKey(to='web.Site')),
            ],
        ),
        migrations.RemoveField(
            model_name='siteeditcancer',
            name='cancer',
        ),
        migrations.RemoveField(
            model_name='siteeditcancer',
            name='site',
        ),
        migrations.DeleteModel(
            name='SiteEditCancer',
        ),
    ]
