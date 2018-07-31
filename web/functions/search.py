from django.shortcuts import render
from web.models import Site
from copy import deepcopy
from random import randint


def search(request):
    search_request_dict = deepcopy(request.GET)
# 如果沒輸入page，預設值=1
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET["page"])
    else:
        page = 1
# 看看使用者在一開始的搜尋欄中有輸入哪些值
    if "chromosome_field" in request.GET:
        has_chromosome = (request.GET["chromosome_field"] != "0")
        has_gene_name = (len(request.GET["gene_name_field"]) != 0)
        has_genomic_region = (request.GET["genomic_region_field"] != "any")
        has_aa_change = (request.GET["aa_change_field"] != "any")
        has_rep = (request.GET["repeat_field"] != "any")
        criterias = {'redi': 1}
        if has_chromosome:
            chromosome = "chr" + request.GET["chromosome_field"]
            criterias['chromo'] = chromosome
        for f in ['gain__gte', 'gain__lte', 'loss__gte', 'loss__lte', 'loc__gte', 'loc__lte', 
        'siteanno__has_cox__gte', 'siteanno__has_cox__lte']:
            if request.GET[f] != '':
            	criterias[f] = int(request.GET[f])
        if has_gene_name:
            gene_name = request.GET["gene_name_field"]
            criterias['gene'] = gene_name
        if has_genomic_region:
            criterias['region'] = request.GET["genomic_region_field"]
        if has_aa_change:
            criterias['aa'] = request.GET["aa_change_field"]
        if has_rep:
            criterias['location'] = request.GET["repeat_field"]
        if any(criterias):
            editing_site_module_set = Site.objects.filter(**criterias)
    else:
        return render(request, "search_form.html")
    # 如果使用者沒有輸入barcode的話則執行以下指令，資料抓取的方式和有輸入barcode大同小異
    if 'current_sort' in request.GET:
        current_sort = request.GET["current_sort"]
    else:
        current_sort = "site"
    if 'sorted_direction' in request.GET:
        sorted_direction = request.GET["sorted_direction"]
    else:
        sorted_direction = "up"
    rd = randint(1, 1000)
    p1_name = '/var/www/rnaedit/static/img/sites/img1/p%s.png' % (rd)
    p2_name = p1_name.replace('img1', 'img2')
    pic = [p1_name.split('static/')[1], p2_name.split('static/')[1]]
    if "click_sort" in request.GET:
        if current_sort == request.GET["click_sort"]:
            if sorted_direction == "up":
                if request.GET["click_sort"] == "site":
                    editing_site_module_set = editing_site_module_set.order_by("-chromo", "-loc")
                else:
                    editing_site_module_set = editing_site_module_set.order_by("-" + request.GET["click_sort"])
                search_request_dict["sorted_direction"] = "down"
            else:
                if request.GET["click_sort"] != "site":
                    editing_site_module_set = editing_site_module_set.order_by(request.GET["click_sort"])
                search_request_dict["sorted_direction"] = "up"
        else:
            if request.GET["click_sort"] != "site":
                editing_site_module_set = editing_site_module_set.order_by(request.GET["click_sort"])
            search_request_dict["sorted_direction"] = "up"
        search_request_dict["current_sort"] = request.GET["click_sort"]
    else:
        if current_sort != "site":
            editing_site_module_set = editing_site_module_set.order_by(current_sort)
        search_request_dict["sorted_direction"] = "up"
        search_request_dict["current_sort"] = current_sort
    return render(request, "editing_level_result_table.html", {'pic': pic,
         'cri': criterias, 'rd': rd})
