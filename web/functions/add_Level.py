from web.models import LevelLite
from web.models import Sample
from web.models import Site
from django.core.exceptions import ObjectDoesNotExist
import os


def update(cancer):
    data_dir = '/var/www/rnaedit/data/%s/' % (cancer)
    datalist = sorted(os.listdir(data_dir))
    for data_name in datalist:
        data_path = data_dir + data_name
        bar = data_name.split('.')[0]
        if bar[-3] == '0':
            tumor = True
        else:
            tumor = False
        try:
            sam = Sample.objects.get(sample_barcode=bar)
        except ObjectDoesNotExist:
            sam = Sample.objects.get(sample_barcode=bar[:12])
            sam.sample_barcode = bar
            if tumor:
                sam.save()
            else:
                sam.is_tumor = False
                sam.stage_event_clinical_stage = ""
                sam.stage_event_pathologic_stage = ""
                sam.tnm_categories_pathologic_M = ""
                sam.tnm_categories_pathologic_N = ""
                sam.tnm_categories_pathologic_T = ""
                sam.history_of_neoadjuvant_treatment = ""
                sam.other_dx = ""
                sam.person_neoplasm_cancer_status = ""
                sam.save()
        with open(data_path, 'r') as f:
            headers = f.readline()
            for line in f:
                d = line.rstrip().split(',')
                sitekey = d[1] + '_' + d[2] + d[3]
                level = (int(d[6]) + int(d[8])) / (int(d[8]) + int(d[5]) + int(d[6]) + int(d[7]))
                try:
                    LevelLite.objects.create(site=Site.objects.get(key=sitekey), sample=sam,
                                             redi_A=int(d[5]),
                                             redi_G=int(d[6]),
                                             hyper_A=int(d[7]),
                                             hyper_G=int(d[8]),
                                             level=level)
                except:
                    f = open('/var/www/rnaedit/data/error_sites.txt', 'a')
                    f.writelines('%s\t%s\n' % (cancer, sitekey))
                    f.close()
                '''
                tg, newlevel = LevelLite.objects.get_or_create(site=Site.objects.get(key=sitekey), sample=sam, 
                    defaults={'site': Site.objects.get(key=sitekey),
                              'sample': sam,
                              'redi_A': int(d[4]),
                              'redi_G': int(d[5]),
                              'hyper_A': int(d[6]),
                              'hyper_G': int(d[7]),
                              'level': level})
                '''


