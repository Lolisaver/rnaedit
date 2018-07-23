from django.db import models


class Sample(models.Model):
    sample_barcode = models.CharField(primary_key=True, max_length=50, default="")
    cancer_type = models.CharField(max_length=10, default="")
    is_tumor = models.BooleanField(default=True)
    stage_event_clinical_stage = models.CharField(max_length=15, default="")
    stage_event_pathologic_stage = models.CharField(max_length=15, default="")
    tnm_categories_pathologic_M = models.CharField(max_length=10, default="")
    tnm_categories_pathologic_N = models.CharField(max_length=10, default="")
    tnm_categories_pathologic_T = models.CharField(max_length=10, default="")
    age_at_initial_pathologic_diagnosis = models.IntegerField(null=True, default=None)
    days_to_birth = models.IntegerField(null=True, default=None)
    days_to_death = models.IntegerField(null=True, default=None)
    days_to_last_followup = models.CharField(max_length=10, default="")
    is_male = models.BooleanField(default=False)
    histological_type = models.CharField(max_length=100, default="")
    history_of_neoadjuvant_treatment = models.CharField(max_length=50, default="")
    other_dx = models.CharField(max_length=50, default="")
    person_neoplasm_cancer_status = models.CharField(max_length=10, default="")
    postoperative_rx_tx = models.NullBooleanField(default=None)
    radiation_therapy = models.NullBooleanField(default=None)
    tissue_prospective_collection_indicator = models.NullBooleanField(default=None)
    tissue_retrospective_collection_indicator = models.NullBooleanField(default=None)
    tumor_tissue_site = models.CharField(max_length=100, default="")
    vital_status = models.NullBooleanField(default=None)
    year_of_initial_pathologic_diagnosis = models.IntegerField(null=True, default=None)
    valid_site = models.IntegerField(null=True, default=None)

    def __str__(self):
        return self.sample_barcode


class Gtexsample(models.Model):
    scan = models.CharField(primary_key=True, max_length=14, default="")
    tissue = models.CharField(max_length=35, default="")


class Mirna(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    accession = models.CharField(max_length=40)
    seq = models.CharField(max_length=40, default='')
    p5 = models.DecimalField(max_digits=10, decimal_places=4)
    p50 = models.DecimalField(max_digits=10, decimal_places=4)
    p95 = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name


class Site(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    chromo = models.CharField(max_length=30)
    loc = models.PositiveIntegerField()
    hg19chr = models.CharField(max_length=30)
    hg19loc = models.PositiveIntegerField()
    hg19str = models.NullBooleanField()
    aa = models.PositiveIntegerField(default=0)
    gene = models.CharField(max_length=180)
    strand = models.NullBooleanField()
    region = models.CharField(max_length=25)
    location = models.CharField(max_length=20)
    repetitive = models.CharField(max_length=20)
    conserve = models.CharField(max_length=30)
    num_of_edited_samples = models.PositiveIntegerField(default=0)
    ref = models.CharField(max_length=1)
    ed = models.CharField(max_length=1)
    edit_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.0)
    gain = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)
    snp_id = models.CharField(max_length=20, default=".")
    cosmic = models.CharField(max_length=15, default=".")
    exac = models.DecimalField(max_digits=8, decimal_places=8, null=True)
    gg = models.DecimalField(max_digits=8, decimal_places=8, null=True)
    intervar = models.CharField(max_length=20, default=".")
    clin = models.CharField(max_length=20, default=".")
    clin_sig = models.PositiveSmallIntegerField(default=0)
    clin_dbn = models.CharField(max_length=75)
    redi = models.NullBooleanField(default=False)
    hyper = models.NullBooleanField(default=False)
    gain_mir = models.ManyToManyField(Mirna, related_name='wild_sites')
    loss_mir = models.ManyToManyField(Mirna, related_name='edit_sites')
    def __str__(self):
        return self.key


class rediLevel(models.Model):
    nas = models.PositiveIntegerField(default=0)
    ngs = models.PositiveIntegerField(default=0)
    level = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    gcover = models.PositiveIntegerField(default=0)
    gfreq = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    sample = models.ForeignKey(Gtexsample, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.level)


class LevelLite(models.Model):
    level = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    redi_A = models.PositiveIntegerField(default=0)
    redi_G = models.PositiveIntegerField(default=0)
    hyper_A = models.PositiveIntegerField(default=0)
    hyper_G = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.level)


class Level(models.Model):
    level = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    redi_A = models.PositiveIntegerField(default=0)
    redi_G = models.PositiveIntegerField(default=0)
    hyper_A = models.PositiveIntegerField(default=0)
    hyper_G = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.level)


class Bind(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    mir = models.ForeignKey(Mirna, on_delete=models.CASCADE)
    chromo = models.CharField(max_length=30)
    utr = models.CharField(max_length=20)
    gstart = models.PositiveIntegerField()
    gend = models.PositiveIntegerField()
    qstart = models.PositiveIntegerField()
    qend = models.PositiveIntegerField()
    ustart = models.PositiveIntegerField()
    uend = models.PositiveIntegerField()
    energy = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    score = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    seed_type = models.CharField(max_length=10)
    mseq = models.CharField(max_length=40)
    binder = models.CharField(max_length=40)
    miseq = models.CharField(max_length=40)


class Miexp(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    mir = models.ForeignKey(Mirna, on_delete=models.CASCADE)
    exp = models.DecimalField(max_digits=10, decimal_places=3)


class Cancer(models.Model):
    abbr = models.CharField(max_length=4, primary_key=True)
    full = models.CharField(max_length=70, default="")
    tumorSample = models.PositiveSmallIntegerField(default=0)
    normalSample = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.abbr


class SiteEdinCancer(models.Model):  # in tumor tissues
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin5 = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=5, decimal_places=4)
    tumor = models.NullBooleanField(default=None)


class SiteEdinTN(models.Model):  # in tumor tissues
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin5 = models.PositiveIntegerField(default=0)
    edin5p = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=5, decimal_places=4)
    p50p = models.PositiveIntegerField(default=0)
    tumor = models.NullBooleanField(default=None)



class SiteEdin(models.Model):  # in tumor tissues
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin = models.PositiveIntegerField(default=0)
    edin5 = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=5, decimal_places=4)
    mean = models.DecimalField(max_digits=5, decimal_places=4)


class SiteEdinTumor(models.Model):  # in tumor tissues
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin5 = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=5, decimal_places=4)


class SiteEdinNormal(models.Model):  # in tumor tissues
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin5 = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=5, decimal_places=4)


class MiexpCancer(models.Model):  # in both tissues
    mirna = models.ForeignKey(Mirna, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin = models.PositiveIntegerField(default=0)
    p0 = models.DecimalField(max_digits=10, decimal_places=4)
    p25 = models.DecimalField(max_digits=10, decimal_places=4)
    p50 = models.DecimalField(max_digits=10, decimal_places=4)
    p75 = models.DecimalField(max_digits=10, decimal_places=4)
    p100 = models.DecimalField(max_digits=10, decimal_places=4)
    mean = models.DecimalField(max_digits=10, decimal_places=4)
    sd = models.DecimalField(max_digits=10, decimal_places=4)
    is_tumor = models.PositiveSmallIntegerField()


class MiexpTumor(models.Model):  # in tumor tissues
    mirna = models.ForeignKey(Mirna, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=10, decimal_places=4)


class MiexpNormal(models.Model):  # in tumor tissues
    mirna = models.ForeignKey(Mirna, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    edin = models.PositiveIntegerField(default=0)
    p50 = models.DecimalField(max_digits=10, decimal_places=4)


class cox(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    cancer = models.ForeignKey(Cancer, on_delete=models.CASCADE)
    p = models.DecimalField(max_digits=10, decimal_places=9)
    fdr = models.DecimalField(max_digits=10, decimal_places=9)
