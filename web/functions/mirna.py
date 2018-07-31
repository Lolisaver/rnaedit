from django.shortcuts import render
from web.models import MiexpTumor as MT
from web.models import Site
from django.core.paginator import Paginator, EmptyPage


def mirna(request):
    criterias = {}
    if 'mirna' in request.POST and request.POST['mirna'] != '':
        criterias['mirna'] = request.POST['mirna']
        criterias['cancer'] = 'ALLL'
    else:
        if 'cancer_field' in request.POST and request.POST['cancer_field'] != '':
            criterias['cancer'] = request.POST['cancer_field']
        if 'exp_from' in request.POST and request.POST['exp_from'] != '':
            criterias['p50__gt'] = float(request.POST['exp_from'])
        if 'exp_to' in request.POST and request.POST['exp_to'] != '':
            criterias['p50__lt'] = float(request.POST['exp_to'])
    mirnas = MT.objects.filter(**criterias)
    if 'click_sort' in request.GET:
        mirnas = mirnas.order_by(request.GET['click_sort'])
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET["page"])
    else:
        page = 1
    if 'datas_per_page' in request.GET:
        perpage = request.GET['datas_per_page']
    else:
        perpage = 10
    paginator = Paginator(mirnas, perpage)
    try:
        mirnas_paged = paginator.page(page)
    except EmptyPage:
        mirnas_paged = paginator.page(paginator.num_pages)
    search_rec = []
    cri_human = {}
    for k in request.GET:
        if request.GET[k] != '' and k != 'page':
            search_rec.append('%s=%s' % (k, request.GET[k]))
            if k == 'gender':
                pass
            elif k == 'exp_from':
                cri_human['miRNA expression higher than'] = request.GET[k]
            elif k == 'exp_to':
                cri_human['miRNA expression lower than'] = request.GET[k]
            else:
                cri_human[k] = request.GET[k]
    searched = '&'.join(search_rec)
    return render(request, "mirna.html", {'mirnas': mirnas_paged, 
                  'search_record': searched, 'cri': cri_human, 'cancer': criterias['cancer']})


def mirna_by_site(request, sitekey, gl):
    s1 = Site.objects.get(key=sitekey)
    if 'g' in gl.lower():
        mirnas = s1.gain_mir.all()
    if 'l' in gl.lower():
        mirnas = s1.loss_mir.all()
    if 'click_sort' in request.GET:
        mirnas = mirnas.order_by(request.GET['click_sort'])
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET["page"])
    else:
        page = 1
    if 'datas_per_page' in request.GET:
        perpage = request.GET['datas_per_page']
    else:
        perpage = 10
    paginator = Paginator(mirnas, perpage)
    try:
        mirnas_paged = paginator.page(page)
    except EmptyPage:
        mirnas_paged = paginator.page(paginator.num_pages)
    search_rec = []
    cri_human = {}
    for k in request.GET:
        if request.GET[k] != '' and k != 'page':
            search_rec.append('%s=%s' % (k, request.GET[k]))
            if k == 'gender':
                pass
            elif k == 'exp_from':
                cri_human['miRNA expression higher than'] = request.GET[k]
            elif k == 'exp_to':
                cri_human['miRNA expression lower than'] = request.GET[k]
            else:
                cri_human[k] = request.GET[k]
    searched = '&'.join(search_rec)
    return render(request, "mirna_by_site.html", {'mirnas': mirnas_paged, 
                  'search_record': searched, 'cri': cri_human})
