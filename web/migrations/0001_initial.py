# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bind',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('chromo', models.CharField(max_length=30)),
                ('gstart', models.PositiveIntegerField()),
                ('gend', models.PositiveIntegerField()),
                ('qstart', models.PositiveIntegerField()),
                ('qend', models.PositiveIntegerField()),
                ('ustart', models.PositiveIntegerField()),
                ('uend', models.PositiveIntegerField()),
                ('energy', models.IntegerField()),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('mismatches', models.CommaSeparatedIntegerField(max_length=20)),
                ('gubind', models.CommaSeparatedIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('level', models.DecimalField(null=True, decimal_places=19, max_digits=20)),
                ('redi_A', models.PositiveIntegerField(default=0)),
                ('redi_C', models.PositiveIntegerField(default=0)),
                ('redi_G', models.PositiveIntegerField(default=0)),
                ('redi_T', models.PositiveIntegerField(default=0)),
                ('hyper_A', models.PositiveIntegerField(default=0)),
                ('hyper_C', models.PositiveIntegerField(default=0)),
                ('hyper_G', models.PositiveIntegerField(default=0)),
                ('hyper_T', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LevelLite',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('level', models.DecimalField(null=True, decimal_places=3, max_digits=4)),
                ('redi_A', models.PositiveIntegerField(default=0)),
                ('redi_G', models.PositiveIntegerField(default=0)),
                ('hyper_A', models.PositiveIntegerField(default=0)),
                ('hyper_G', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mirna',
            fields=[
                ('name', models.CharField(serialize=False, max_length=30, primary_key=True)),
                ('seq', models.CharField(max_length=40, default='')),
                ('accession', models.CharField(max_length=20, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('sample_barcode', models.CharField(serialize=False, primary_key=True, max_length=50, default='')),
                ('cancer_type', models.CharField(max_length=10, default='')),
                ('is_tumor', models.BooleanField(default=True)),
                ('stage_event_clinical_stage', models.CharField(max_length=15, default='')),
                ('stage_event_pathologic_stage', models.CharField(max_length=15, default='')),
                ('tnm_categories_pathologic_M', models.CharField(max_length=10, default='')),
                ('tnm_categories_pathologic_N', models.CharField(max_length=10, default='')),
                ('tnm_categories_pathologic_T', models.CharField(max_length=10, default='')),
                ('age_at_initial_pathologic_diagnosis', models.IntegerField(null=True, default=None)),
                ('days_to_birth', models.IntegerField(null=True, default=None)),
                ('days_to_death', models.IntegerField(null=True, default=None)),
                ('days_to_last_followup', models.CharField(max_length=10, default='')),
                ('is_male', models.BooleanField(default=False)),
                ('histological_type', models.CharField(max_length=100, default='')),
                ('history_of_neoadjuvant_treatment', models.CharField(max_length=50, default='')),
                ('other_dx', models.CharField(max_length=50, default='')),
                ('person_neoplasm_cancer_status', models.CharField(max_length=10, default='')),
                ('postoperative_rx_tx', models.NullBooleanField(default=None)),
                ('radiation_therapy', models.NullBooleanField(default=None)),
                ('tissue_prospective_collection_indicator', models.NullBooleanField(default=None)),
                ('tissue_retrospective_collection_indicator', models.NullBooleanField(default=None)),
                ('tumor_tissue_site', models.CharField(max_length=100, default='')),
                ('vital_status', models.NullBooleanField(default=None)),
                ('year_of_initial_pathologic_diagnosis', models.IntegerField(null=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('key', models.CharField(serialize=False, max_length=100, primary_key=True)),
                ('chromo', models.CharField(max_length=30)),
                ('loc', models.PositiveIntegerField()),
                ('utr', models.CharField(max_length=100)),
                ('gene', models.CharField(max_length=50)),
                ('strand', models.NullBooleanField()),
                ('repetitive', models.CharField(max_length=30)),
                ('conserve', models.CharField(max_length=20)),
                ('num_of_edited_samples', models.PositiveIntegerField(default=0)),
                ('ref', models.CharField(max_length=1)),
                ('ed', models.CharField(max_length=1)),
                ('edit_percent', models.DecimalField(null=True, decimal_places=2, default=0.0, max_digits=5)),
                ('gain', models.PositiveIntegerField(default=0)),
                ('loss', models.PositiveIntegerField(default=0)),
                ('snp_id', models.CharField(max_length=20, default='NA')),
                ('redi', models.NullBooleanField(default=False)),
                ('hyper', models.NullBooleanField(default=False)),
                ('gain_mir', models.ManyToManyField(to='web.Mirna', related_name='wild_sites')),
                ('loss_mir', models.ManyToManyField(to='web.Mirna', related_name='edit_sites')),
            ],
        ),
        migrations.AddField(
            model_name='levellite',
            name='sample',
            field=models.ForeignKey(to='web.Sample'),
        ),
        migrations.AddField(
            model_name='levellite',
            name='site',
            field=models.ForeignKey(to='web.Site'),
        ),
        migrations.AddField(
            model_name='level',
            name='sample',
            field=models.ForeignKey(to='web.Sample'),
        ),
        migrations.AddField(
            model_name='level',
            name='site',
            field=models.ForeignKey(to='web.Site'),
        ),
        migrations.AddField(
            model_name='bind',
            name='site',
            field=models.ForeignKey(to='web.Site'),
        ),
    ]
