from django.shortcuts import render
from ..models import Site
from ..models import SiteEdinTumor as SET
import matplotlib.pyplot as plt
import pandas as pd
import json


def sitesimg1(request, cris, tar, rd):
    cri_dict = json.loads(cris.replace("'", '"'))
    q1 = Site.objects.filter(**cri_dict)
    t10 = list(SET.objects.filter(site=q1, cancer='ALLL').order_by('-edin5')[:10].values_list('site', flat=True))
    secs = pd.DataFrame(list(SET.objects.filter(site__in=t10).values_list('site', 'cancer', 'edin5')), columns=['site', 'cancer', 'edited'])
    if secs.empty:
        return render(request, "embedpic.html", {'pic': 'img/nodata.png', 'img_src': tar, 's10': []})
    p1 = secs.pivot_table(values='edited', index='site', columns='cancer', aggfunc='first')
    p1['ALLL'] = p1.sum(axis=1)
    p1 = p1.sort_values('ALLL')
    del p1['ALLL']
    img1 = plt.figure(figsize=(18, 9))
    ax = plt.subplot(111)
    p1.plot.barh(stacked=True, fontsize=18, legend=False, ax=ax)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    fig1 = ax.get_figure()
    p1_name = '/var/www/rnaedit/static/img/sites/img1/p%s.png' % (rd)
    fig1.savefig(p1_name)
    pic = p1_name.split('static/')[1]
    return render(request, "embedpic.html", {'pic': pic, 'img_src': tar, 's10': list(p1.index)})
