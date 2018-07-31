from django.shortcuts import render
from ..models import Site
from django.core.paginator import Paginator, EmptyPage
from copy import deepcopy
from django.db.models import Avg


def embed_sites(request):
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
    elif 'mirna' in request.GET:  # if search from mirna
        mir = request.GET['mirna']
        gl = request.GET['gl']
        criterias = {gl: mir}
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
    #看使用者選取要多少筆資料為一頁，預設為50
    if 'datas_per_page' in request.GET:
        datas_per_page = int(request.GET["datas_per_page"])
    else:
        datas_per_page = 10
    paginator = Paginator(editing_site_module_set[:100000], datas_per_page)
    try:
        editing_site_modules = paginator.page(page)
        print('check 1')
    except EmptyPage:
        editing_site_modules = paginator.page(paginator.num_pages)
    rediLevels = [x.redilevel_set.aggregate(Avg('level'))['level__avg'] for x in editing_site_modules]
    rediLevels = [2 if x == None else x for x in rediLevels]
    page_record = []
    search_record = []
    for key in search_request_dict:
        if key != "page" and key != "click_sort":
            page_record.append(key + "=" + search_request_dict[key])
            if key != "current_sort" and key != "sorted_direction":
                search_record.append(key + "=" + search_request_dict[key])
    page_record = "&".join(page_record)
    search_record = "&".join(search_record)
    return render(request, "embedtable.html", {"editing_modules": editing_site_modules,\
         "page_record": page_record, "search_record": search_record, "search_request_dict": search_request_dict,\
         "datas_per_page": datas_per_page, "sorted_direction": search_request_dict["sorted_direction"],\
         "current_sort": search_request_dict["current_sort"], 'rl': rediLevels,
         'cri': criterias, 'target_frame': request.GET['frame']})
