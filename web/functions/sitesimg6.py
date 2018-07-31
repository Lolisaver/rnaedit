from django.shortcuts import render
from web.models import Site
from web.models import SiteEdinTumor as SET
from web.models import SiteEdinNormal as SEN
from web.models import SiteEdinCancer as SEC
from web.models import Cancer, Sample
from web.models import LevelLite as ll
import pandas as pd


def sitesimg6(request, bar, tar, rd):
    c2n = {True: 2, False: 3}
    cancer = Sample.objects.get(sample_barcode=bar).cancer_type
    tumc = Cancer.objects.get(abbr=cancer).tumorSample
    norc = Cancer.objects.get(abbr=cancer).normalSample
    # sites from tumors top5
    t5 = list(SET.objects.filter(cancer=cancer).order_by('-edin5', '-p50')[:10].values_list('site', flat=True))
    secs = pd.DataFrame(list(SEC.objects.filter(cancer=cancer, site__in=t5).values_list('site', 'cancer', 'edin5', 'p50', 'tumor')), columns=['site', 'cancer', 'edited', 'p50', 'tn'])

    # sites from normals top5
    n5 = list(SEN.objects.filter(cancer=cancer).order_by('-edin5', '-p50')[:10].values_list('site', flat=True))
    secs_n = pd.DataFrame(list(SEC.objects.filter(cancer=cancer, site__in=n5).values_list('site', 'cancer', 'edin5', 'p50', 'tumor')), columns=['site', 'cancer', 'edited', 'p50', 'tn'])

    secs_s = pd.DataFrame(list(ll.objects.filter(site__in=t5 + n5, sample=bar).values_list('site', 'level')), columns=['site', 'p50'])
    secs_s['edited'] = 1
    secs_s['cancer'] = 1
    secs_s['tn'] = bool(1 - int(bar[-3]))

    t2n = {}
    rep = []
    for i in range(len(t5)):
        t2n[t5[i]] = i + 1
    secs['site'] = secs['site'].map(t2n)
    for i in range(len(n5)):
        if n5[i] in t2n:
            rep.append((i + 11, t2n[n5[i]]))
        t2n[n5[i]] = i + 11
    secs_n['site'] = secs_n['site'].map(t2n)
    secs_s['site'] = secs_s['site'].map(t2n)
    for i in rep:
        nc = secs_s[secs_s['site'] == i[0]]
        nc.loc[:, 'site'] = i[1]
        secs_s = secs_s.append(nc)
    secs = secs.append(secs_n)
    if secs.empty:
        return render(request, "embedpic.html", {'pic': 'img/nodata.png', 'img_src': tar, 's10': []})
    secs.loc[(secs['tn'] == True), 'edited'] /= tumc
    secs.loc[(secs['tn'] == False), 'edited'] /= norc
    secs['cancer'] = secs['tn'].map(c2n)

    secs = secs.append(secs_s)

    p1_name = '/var/www/rnaedit/static/csv/sites/img4/d%s.csv' % (rd)
    secs.to_csv(p1_name, index=False)
    pic = p1_name.split('static/')[1]
    return render(request, "embedcircle3.html", {'pic': pic, 'img_src': tar, 't5': t5 + n5})
