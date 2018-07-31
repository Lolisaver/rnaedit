from django.shortcuts import render
from web.models import Site
from web.models import SiteEdinCancer as SEC
from web.models import Cancer
import pandas as pd
import json


def sitesimg5(request, cris, tar, rd):
    c2n = {'ACC': 1, 'BLCA': 2, 'BRCA': 3, 'CESC': 4, 'CHOL': 5, 'COAD': 6, 'DLBC': 7,
 'ESCA': 8, 'GBM': 9, 'HNSC': 10, 'KICH': 11, 'KIRC': 12, 'KIRP': 13, 'LAML': 14, 'LGG': 15, 
 'LIHC': 16, 'LUAD': 17, 'LUSC': 18, 'MESO': 19, 'OV': 20, 'PAAD': 21, 'PCPG': 22,
 'PRAD': 23, 'READ': 24, 'SARC': 25, 'SKCM': 26, 'STAD': 27, 'TGCT': 28, 'THCA': 29,
 'THYM': 30, 'UCEC': 31, 'UCS': 32, 'UVM': 33}
    cancers = pd.DataFrame(list(Cancer.objects.all().values_list('abbr', 'tumorSample', 'normalSample')))
    tumc = cancers.set_index(0)[1].to_dict()
    norc = cancers.set_index(0)[2].to_dict()
    cri_dict = json.loads(cris.replace("'", '"'))
    q1 = Site.objects.filter(**cri_dict)

    # sites from tumors top5
    t5 = list(q1.order_by('-siteanno__tumor33')[:5].values_list('key', flat=True))
    secs = pd.DataFrame(list(SEC.objects.filter(site__in=t5).values_list('site', 'cancer', 'edin5', 'p50', 'tumor')), columns=['site', 'cancer', 'edited', 'p50', 'tn'])
    secs = secs[secs['cancer'] != 'ALLL']
    secs['site'] += '_' + secs['tn'].astype(str).str[0]

    # sites from normals top5
    n5 = list(q1.order_by('-siteanno__normal33')[:5].values_list('key', flat=True))
    secs_n = pd.DataFrame(list(SEC.objects.filter(site__in=n5).values_list('site', 'cancer', 'edin5', 'p50', 'tumor')), columns=['site', 'cancer', 'edited', 'p50', 'tn'])
    secs_n = secs_n[secs_n['cancer'] != 'ALLL']
    secs_n['site'] += '_' + secs_n['tn'].astype(str).str[0]

    if secs.empty:
        return render(request, "embedpic.html", {'pic': 'img/nodata.png', 'img_src': tar, 's10': []})
    t2n = {}
    for i in range(len(t5)):
        t2n[t5[i] + '_T'] = 2 * i + 1  # odd for tumors
        t2n[t5[i] + '_F'] = 2 * i + 2  # even for normals
    secs['site'] = secs['site'].map(t2n)
    t2n = {}
    for i in range(len(n5)):
        t2n[n5[i] + '_T'] = 2 * i + 11  # odd for tumors
        t2n[n5[i] + '_F'] = 2 * i + 12  # even for normals
    secs_n['site'] = secs_n['site'].map(t2n)
    secs = secs.append(secs_n)

    secs.loc[(secs['tn'] == True), 'edited'] /= secs.loc[(secs['tn'] == True), 'cancer'].map(tumc)
    secs.loc[(secs['tn'] == False), 'edited'] /= secs.loc[(secs['tn'] == False), 'cancer'].map(norc)
    secs['cancer'] = secs['cancer'].map(c2n)
    

    p1_name = '/var/www/rnaedit/static/csv/sites/img4/d%s.csv' % (rd)
    secs.to_csv(p1_name, index=False)
    pic = p1_name.split('static/')[1]
    return render(request, "embedcircle2.html", {'pic': pic, 'img_src': tar, 't5': t5 + n5})
