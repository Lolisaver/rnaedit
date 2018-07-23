from django.shortcuts import render
from web.models import Site, Cancer
from web.models import SiteEdinCancer as SEC
import pandas as pd
import json


def sitesimg3(request, cris, tar, rd):
    cri_dict = json.loads(cris.replace("'", '"'))
    q1 = Site.objects.filter(**cri_dict)
    secs = pd.DataFrame(list(SEC.objects.filter(site=q1).values_list('cancer', 'edin5', 'p50', 'tumor')), columns=['cancer', 'edin', 'p50', 'is_tumor'])
    if secs.empty:
        return render(request, "embedpic.html", {'pic': 'img/nodata.png', 'img_src': tar})
    cancers = pd.DataFrame(list(Cancer.objects.all().values_list('abbr', 'normalSample', 'tumorSample')))
    norc = cancers.set_index(0)[1].to_dict()
    tumc = cancers.set_index(0)[2].to_dict()
    secs = secs[secs.cancer != 'ALLL']
    cancer_count = len(set(secs.cancer))
    secs.loc[secs['is_tumor'], 'edin'] /= secs['cancer'].map(tumc)
    secs.loc[~secs['is_tumor'], 'edin'] /= secs['cancer'].map(norc)
    secs['edin'] = secs['edin'].round(2)
    p2_name = '/var/www/rnaedit/static/csv/sites/img3/d%s.csv' % (rd)
    secs.to_csv(p2_name, index=False)
    pic = p2_name.split('static/')[1]
    return render(request, "embedbox.html", {'pic': pic, 'img_src': tar, 
        'c_count': cancer_count})
