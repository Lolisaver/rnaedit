from django.shortcuts import render
from web.models import Sample
from django.core.paginator import Paginator, EmptyPage
from random import randint
from django.db.models.functions import Length


def sample(request, cancer):
    criterias = {}
    if cancer != 'ALL':
        criterias['cancer_type'] = cancer
    if 'tissue' in request.GET and request.GET['tissue'] != '':
        criterias['tumor_tissue_site'] = request.GET['tissue']
    if 'gender' in request.GET and request.GET['gender'] != '':
        criterias['is_male'] = request.GET['gender']
    if 'tumor' in request.GET and request.GET['tumor'] != '':
        criterias['is_tumor'] = request.GET['tumor']
    if 'age_from' in request.GET and request.GET['age_from'] != '':
        criterias['days_to_birth__lte'] = int(request.GET['age_from']) * -365 + 180
    if 'age_to' in request.GET and request.GET['age_to'] != '':
        criterias['days_to_birth__gte'] = int(request.GET['age_to']) * -365 - 180

    samples = Sample.objects.filter(**criterias).annotate(bc_len=Length('sample_barcode')).filter(bc_len__gt=13)
    if 'click_sort' in request.GET:
        samples = samples.order_by(request.GET['click_sort'])
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET["page"])
    else:
        page = 1
    if 'datas_per_page' in request.GET:
        perpage = request.GET['datas_per_page']
    else:
        perpage = 10
    paginator = Paginator(samples, perpage)
    try:
        samples_paged = paginator.page(page)
    except EmptyPage:
        samples_paged = paginator.page(paginator.num_pages)
    search_rec = []
    cri_human = {}
    for k in request.GET:
        if request.GET[k] != '' and k != 'page':
            search_rec.append('%s=%s' % (k, request.GET[k]))
            if k == 'gender':
                if request.GET[k] == '0':
                    cri_human[k] = 'male'
                else:
                    cri_human[k] = 'female'
            elif k == 'age_from':
                cri_human['older than'] = request.GET[k]
            elif k == 'age_to':
                cri_human['younger than'] = request.GET[k]
            else:
                cri_human[k] = request.GET[k]
    searched = '&'.join(search_rec)
    rd = (randint(0, 1000), randint(2000, 4000))
    #p1_name = 'img/cancers/img1/p%s.png' % (rd)
    #p2_name = p1_name.replace('img1', 'img2')
    #pics = [p1_name, p2_name]
    return render(request, "samples.html", {'samples': samples_paged, 
        'cancer': cancer, 'search_record': searched, 'cri': cri_human,
        'rd': rd})
