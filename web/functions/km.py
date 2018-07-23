from django.shortcuts import render
from web.models import LevelLite as ll
from lifelines import KaplanMeierFitter


def km(request, cancer, site, cut):
    levels = ll.objects.filter(sample__cancer_type=cancer, sample__is_tumor=True, site=site)
    ingroup = int(round(float(cut) * levels.count()))
    hgq = levels.order_by('-level')[:ingroup]
    lgq = levels.order_by('level')[:ingroup]
    days = []
    death = []
    group = []
    for dead, alive in hgq.values_list('sample__days_to_death', 'sample__days_to_last_followup'):
        if dead == -1:
            if alive != '--':
                days.append(int(alive))
                death.append(False)
                group.append('h')
        else:
            days.append(dead)
            death.append(True)
            group.append('h')

    for dead, alive in lgq.values_list('sample__days_to_death', 'sample__days_to_last_followup'):
        if dead == -1:
            if alive != '--':
                days.append(int(alive))
                death.append(False)
                group.append('l')
        else:
            days.append(dead)
            death.append(True)
            group.append('l')
    from pandas import DataFrame as Df
    qq = Df([days, death, group]).T
    days = qq[0]
    death = qq[1]
    groups = qq[2]
    ix = (groups == 'l')
    kmf = KaplanMeierFitter()
    kmf.fit(days[~ix], death[~ix], label='high group')
    ax = kmf.plot()
    kmf.fit(days[ix], death[ix], label='low group')
    pic_path = '/var/www/rnaedit/static/img/km/p1.png'
    fig = kmf.plot(ax=ax).get_figure()
    fig.savefig(pic_path)

    mt = {'cut': cut, 'site': site, 'ig': ingroup, 'cancer': cancer}

    return render(request, "km.html", {'pic': pic_path.split('static/')[1], 'meta': mt})
