from web.models import Sample

data_path = '/var/www/rnaedit/data/Sample_data.tsv'


def yesno(s):
    if s == 'YES':
        return 1
    elif s == 'NO':
        return 0
    else:
        return 2


def dedash(s):
    if s == '--':
        return -1
    else:
        return int(s)


with open(data_path, 'r') as f:
    headers = f.readline()
    for line in f:
        d = line.rstrip().split('\t')
        if Sample.objects.filter(sample_barcode=d[1]).exists():
            todel = Sample.objects.get(sample_barcode=d[1])
            todel.delete()
        if d[6] == 'MALE':
            ismale = 1
        elif d[6] == 'FEMALE':
            ismale = 0
        else:
            ismale = 2
        if d[16] == 'ALIVE':
            alive = 1
        elif d[16] == 'DEAD':
            alive = 0
        else:
            alive = 2
        Sample.objects.create(cancer_type=d[0],
            sample_barcode=d[1],
            age_at_initial_pathologic_diagnosis=dedash(d[2]),
            days_to_birth=dedash(d[3]),
            days_to_death=dedash(d[4]),
            days_to_last_followup=d[5],
            is_male=ismale,
            histological_type=d[7],
            history_of_neoadjuvant_treatment=d[8],
            other_dx=d[9],
            person_neoplasm_cancer_status=d[10],
            postoperative_rx_tx=yesno(d[11]),
            radiation_therapy=yesno(d[12]),
            tissue_prospective_collection_indicator=yesno(d[13]),
            tissue_retrospective_collection_indicator=yesno(d[14]),
            tumor_tissue_site=d[15],
            vital_status=alive,
            year_of_initial_pathologic_diagnosis=dedash(d[17]),
            stage_event_clinical_stage=d[18],
            stage_event_pathologic_stage=d[19],
            tnm_categories_pathologic_M=d[20],
            tnm_categories_pathologic_N=d[21],
            tnm_categories_pathologic_T=d[22],)
print('Sample data update successfully!')
