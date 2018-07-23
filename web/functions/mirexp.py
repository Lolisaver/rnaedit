from django.shortcuts import render
from web.models import LevelLite as ll
from web.models import Miexp, Mirna
from django.core.paginator import Paginator, EmptyPage
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


def mirexp(request, site, mir):
    timeit()
    samples = ll.objects.filter(site=site).values('sample')
    timeit('check1')
    miexps = Miexp.objects.filter(mir=mir, sample=samples)
    timeit('check2')
    if 'click_sort' in request.GET:
        if request.GET['click_sort'] != 'exp':
            miexps = miexps.order_by('sample__' + request.GET['click_sort'])
        else:
            miexps = miexps.order_by(request.GET['click_sort'])
    mirget = Mirna.objects.get(name=mir)

    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET["page"])
    else:
        page = 1
    if 'datas_per_page' in request.GET:
        perpage = request.GET['datas_per_page']
    else:
        perpage = 50
    paginator = Paginator(miexps, perpage)
    try:
        miexps_paged = paginator.page(page)
    except EmptyPage:
        miexps_paged = paginator.page(paginator.num_pages)

    return render(request, "miexps.html", {'miexps': miexps_paged, 'mir': mirget})
