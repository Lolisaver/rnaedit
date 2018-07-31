from django.shortcuts import render
from web.models import SiteEdinTumor as SET
from web.models import SiteEdinNormal as SEN
from web.models import LevelLite as ll
from web.models import Cancer
import numpy as np
import pandas as pd


def cancersimg3(request, cancer, rd, lr):
    if lr == 'r':
        order = ('-p50', '-edin5')
        img_src = 'p2'
    else:  # lr == 'r'
        order = ('-edin5', '-p50')
        img_src = 'p1'
    thiscancer = Cancer.objects.get(abbr=cancer)
    norc = thiscancer.normalSample
    tumc = thiscancer.tumorSample
    if norc == 0:
        t5_details = SET.objects.filter(cancer=cancer).order_by(*order)[:10]
        t5 = list(t5_details.values_list('site', flat=True))
        tt1 = ll.objects.filter(site__in=t5, sample__cancer_type=cancer)
        ttl = tt1.values_list('site', 'level')
        secs = list(ttl)
        p1 = pd.DataFrame(secs)
        p1.columns = ['cancer', 'edin']
        n5_details = []
        v_type = 'combine'
    else:
        t5_details = SET.objects.filter(cancer=cancer).order_by(*order)[:5]
        t5 = list(t5_details.values_list('site', flat=True))
        tt = ll.objects.filter(site__in=t5, sample__cancer_type=cancer)
        tt = tt.values_list('site', 'level', 'sample__is_tumor')
        tt = list(tt)
        pt = pd.DataFrame(tt)
        pt[0] += '_T'
        n5_details = SEN.objects.filter(cancer=cancer).order_by(*order)[:5]
        n5 = list(n5_details.values_list('site', flat=True))
        nn = ll.objects.filter(site__in=n5, sample__cancer_type=cancer)
        nn = nn.values_list('site', 'level', 'sample__is_tumor')
        nn = list(nn)
        pn = pd.DataFrame(nn)
        pn[0] += '_N'
        p1 = pt.append(pn)
        p1.columns = ['cancer', 'p50', 'is_tumor']
        #v_type = 'combine'
        v_type = 'split'
    p1_name = '/var/www/rnaedit/static/csv/cancers/img3/d%s.csv' % (rd)
    p1['p50'] = p1['p50'].astype(float)
    # p1['edin'] -= np.random.rand(p1.shape[0]) / 1000
    p1.to_csv(p1_name, index=False)
    pic = p1_name.split('static/')[1]
    return render(request, "embedboxcancer.html", {'pic': pic, 'img_src': img_src, 
                    't5': t5_details, 'n5': n5_details, 'c_count': 10,
                    'norc': norc, 'tumc': tumc})
