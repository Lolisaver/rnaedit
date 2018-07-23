from django.shortcuts import render
from web.models import SiteEdinTumor as SET
from web.models import SiteEdinNormal as SEN
from web.models import LevelLite as ll
from web.models import Cancer
import pandas as pd
import matplotlib.pyplot as plt
import time


def timeit(msg=''):
    if hasattr(timeit, 't0'):
        passed = time.time() - timeit.t0
        timeit.t0 = time.time()
        print(msg, round(passed, 4))
    else:
        timeit.t0 = time.time()
        print('Timer activated')
    return 0


def cancersimg1(request, cancer, rd):
    fig, ax = plt.subplots()
    fig.set_size_inches((16, 8))
    ax.set_ylim(-0.1, 1.1)
    if Cancer.objects.get(abbr=cancer).normalSample == 0:
        timeit()
        t5_details = SET.objects.filter(cancer=cancer).order_by('-edin5', '-p50')[:10]
        t5 = list(t5_details.values_list('site', flat=True))
        timeit('check1')
        t0 = time.time()
        tt1 = ll.objects.filter(site__in=t5, sample__cancer_type=cancer)
        ttl = tt1.values_list('site', 'level')
        secs = list(ttl)
        timeit('check2')
        dic = {}
        for i in secs:
            col = i[0]
            if col not in dic:
                dic[col] = []
            dic[col].append(float(i[1]))
        p1 = [dic[x] for x in t5]
        labels = [*map(str, range(1, 11))]
        box = ax.boxplot(p1,
                         vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         labels=labels, 
                         showfliers=False)
        for patch in box['boxes']:
            patch.set_facecolor('orange')
        edins = dict(SET.objects.filter(site__in=t5, cancer=cancer).values_list('site', 'edin5'))
        timeit('check5')
        sums = Cancer.objects.get(abbr=cancer).tumorSample
        timeit('check6')
        ss = [(edins[x] / sums * 4000) for x in t5]
        p3 = pd.DataFrame([[0, ] * 10, [*range(1, 11)]]).T
        timeit('check7')
        p3.columns = ['yy', 'xx']
        p3.plot.scatter(x='xx', y='yy', s=ss, c='orange', ax=ax)
        n5_details = []
    else:
        timeit()
        t5_details = SET.objects.filter(cancer=cancer).order_by('-edin5', '-p50')[:5]
        t5 = list(t5_details.values_list('site', flat=True))
        timeit('check1')
        tt = ll.objects.filter(site__in=t5, sample__cancer_type=cancer)
        tt = tt.values_list('site', 'level', 'sample__is_tumor')
        tt = list(tt)
        timeit('check2')
        t1 = {}
        for i in tt:
            col = i[0]
            if i[2]:
                if col not in t1:
                    t1[col] = []
                t1[col].append(float(i[1]))
        n5_details = SEN.objects.filter(cancer=cancer).order_by('-edin5', '-p50')[:5]
        n5 = list(n5_details.values_list('site', flat=True))
        timeit('check4')
        nn = ll.objects.filter(site__in=n5, sample__cancer_type=cancer)
        nn = nn.values_list('site', 'level', 'sample__is_tumor')
        nn = list(nn)
        timeit('check5')
        n1 = {}
        for i in nn:
            col = i[0] + 'N'
            if not i[2]:
                if col not in t1:
                    t1[col] = []
                t1[col].append(float(i[1]))
        p1 = [t1[x] for x in t5] + [t1[x + 'N'] for x in n5]
        labels = [*map(str, range(1, 6))] * 2
        box = ax.boxplot(p1,
                         vert=True,  # vertical box alignment
                         patch_artist=True,  # fill with color
                         labels=labels, 
                         showfliers=False)
        for i, patch in enumerate(box['boxes']):
            if i < 5:
                patch.set_facecolor('orange')
            else:
                patch.set_facecolor('blue')
        edins_T = dict(SET.objects.filter(site__in=t5, cancer=cancer).values_list('site', 'edin5'))
        timeit('check8')
        edins_N = dict(SEN.objects.filter(site__in=n5, cancer=cancer).values_list('site', 'edin5'))
        timeit('check9')
        sums_T = Cancer.objects.get(abbr=cancer).tumorSample
        sums_N = Cancer.objects.get(abbr=cancer).normalSample
        ss_T = [(edins_T[x] / sums_T * 4000) for x in t5]
        ss_N = [(edins_N[x] / sums_N * 4000) for x in n5]
        timeit('check10')
        p3 = pd.DataFrame([[0, ] * 5, [*range(1, 6)], [*range(6, 11)]]).T
        timeit('check11')
        p3.columns = ['yy', 'xx_T', 'xx_N']
        p3.plot.scatter(x='xx_T', y='yy', s=ss_T, c='orange', ax=ax)
        p3.plot.scatter(x='xx_N', y='yy', s=ss_N, c='blue', ax=ax)
        t5 = t5 + n5
        timeit('check12')
    for item in (ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(20)
    for patch in box['medians']:
        patch.set_color('red')
    fig1 = ax.get_figure()
    p1_name = '/var/www/rnaedit/static/img/cancers/img1/p%s.png' % (rd)
    fig1.savefig(p1_name)
    timeit('check save')
    pic = p1_name.split('static/')[1]
    return render(request, "embedpic.html", {'pic': pic, 'img_src': 'p1img', 't5': t5_details, 'n5': n5_details})
