from django.shortcuts import render
from web.models import Site, Cancer
from web.models import SiteEdinCancer as SEC
import pandas as pd
import json


def sitesimg2(request, cris, tar, rd):
    cri_dict = json.loads(cris.replace("'", '"'))
    q1 = Site.objects.filter(**cri_dict)
    secs = pd.DataFrame(list(SEC.objects.filter(site=q1).values_list('cancer', 'edin', 'tumor')), columns=['cancer', 'edin', 'is_tumor'])
    if secs.empty:
        return render(request, "embedpic.html", {'pic': 'img/nodata.png', 'img_src': tar})
    cancers = pd.DataFrame(list(Cancer.objects.all().values_list('abbr', 'normalSample', 'tumorSample')))
    norc = cancers.set_index(0)[1].to_dict()
    tumc = cancers.set_index(0)[2].to_dict()
    p2 = secs.pivot_table(values='edin', index='cancer', columns='is_tumor', aggfunc=sum)[[1, 0]]
    p2[True] = p2[True] / p2.index.map(tumc)
    p2[False] = p2[False] / p2.index.map(norc)
    p2.drop(['ALLL'], inplace=True)
    img2 = p2.plot.bar(stacked=True, figsize=(18, 9), fontsize=20, legend=False)
    patches, labels = img2.get_legend_handles_labels()
    img2.legend(('Normal', 'Tumor'), labels, loc='best')
    fig2 = img2.get_figure()
    p2_name = '/var/www/rnaedit/static/img/sites/img2/p%s.png' % (rd)
    fig2.savefig(p2_name)
    pic = p2_name.split('static/')[1]
    return render(request, "embedpic.html", {'pic': pic, 'img_src': tar})
