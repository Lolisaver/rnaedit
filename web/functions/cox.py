from django.shortcuts import render
from web.models import cox
from web.models import Site


def cox(request, sitekey):
    s1 = Site.objects.get(key=sitekey)
    coxes = s1.cox_set.all().order_by('cancer_id')
    return render(request, "cox.html", {'coxes': coxes, 'site': s1})

'''
def cox(request, sitekey):
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
'''
