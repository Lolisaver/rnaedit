from django.shortcuts import render
from ..models import Sample, LevelLite
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from copy import deepcopy
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from random import randint


def barcode(request, bar=0):
    if bar == 0:
        if 'sample_barcode_field' in request.GET:
            has_sample_barcode = True
            sample_barcode = request.GET['sample_barcode_field']
        else:
            return render(request, "barcode_search.html")
    else:
        has_sample_barcode = True
        sample_barcode = bar
    search_request_dict = deepcopy(request.GET)
# 如果沒輸入page，預設值=1
    if request.method == 'GET' and 'page' in request.GET:
        page = int(request.GET["page"])
    else:
        page = 1
# 看看使用者在一開始的搜尋欄中有輸入哪些值
    try:
        sample_module = Sample.objects.get(sample_barcode=sample_barcode)
    except ObjectDoesNotExist:
        return render(request, "bar_result_table.html",\
     {"has_sample_barcode":has_sample_barcode,"sample_module": sample_barcode,\
     "editing_modules": [], "page_record": 0, "search_record": '',\
     "search_request_dict": '', "sorted_direction": '', "current_sort": ''})
    # 從資料庫中抓取這個Sample的LevelLite資料
    criterias = {'sample': sample_barcode, 'level__gt': 0.01}
    q1 = LevelLite.objects.filter(**criterias)
    editing_level_module_set = q1.annotate(g_sum=F('redi_G') + F('hyper_G')).filter(g_sum__gt=1)
    try:
        current_sort = request.GET["current_sort"]
    except:
        current_sort = "site"
    try:
        sorted_direction = request.GET["sorted_direction"]
    except:
        sorted_direction = "up"
    rd = randint(1, 1000)
    p1_name = '/var/www/rnaedit/static/img/sites/img1/p%s.png' % (rd)
    p2_name = p1_name.replace('img1', 'img2')
    pic = [p1_name.split('static/')[1], p2_name.split('static/')[1]]
    if "click_sort" in request.GET:
        if current_sort == request.GET["click_sort"]:
            if sorted_direction == "down":
                if request.GET["click_sort"] == "site":
                    editing_level_module_set = sorted(editing_level_module_set, key=lambda n: (n.site.chromo[3:], n.site.loc))
                elif request.GET["click_sort"] == "level":
                    editing_level_module_set = editing_level_module_set.order_by(request.GET["click_sort"])
                else:
                    editing_level_module_set = editing_level_module_set.order_by("site__" + request.GET["click_sort"])
                search_request_dict["sorted_direction"] = "up"
            else:
                if request.GET["click_sort"] == "site":
                    editing_level_module_set = sorted(editing_level_module_set, key=lambda n: (n.site.chromo[3:], n.site.loc), reverse=True)
                elif request.GET["click_sort"] == "level":
                    editing_level_module_set = editing_level_module_set.order_by("-" + request.GET["click_sort"])
                else:
                    editing_level_module_set = editing_level_module_set.order_by("-site__" + request.GET["click_sort"])
                search_request_dict["sorted_direction"] = "down"
        else:
            if request.GET["click_sort"] == "site":
                editing_level_module_set = sorted(editing_level_module_set, key=lambda n: (n.site.chromo[3:], n.site.loc))
            elif request.GET["click_sort"] == "level":
                editing_level_module_set = editing_level_module_set.order_by(request.GET["click_sort"])
            else:
                editing_level_module_set = editing_level_module_set.order_by("site__" + request.GET["click_sort"])
            search_request_dict["sorted_direction"] = "up"
        search_request_dict["current_sort"] = request.GET["click_sort"]
    else:
        if current_sort == "site":
            print('current_sort = site')
            editing_level_module_set = editing_level_module_set.order_by("site__chromo", "site__loc")
            print('finished sorting by site')
        elif current_sort == "level":
            editing_level_module_set = editing_level_module_set.order_by(current_sort)
        else:
            editing_level_module_set = editing_level_module_set.order_by("site__" + current_sort)
        search_request_dict["sorted_direction"] = "up"
        search_request_dict["current_sort"] = current_sort
    try:
        datas_per_page = int(request.GET["datas_per_page"])
    except:
        datas_per_page = 50
    paginator = Paginator(editing_level_module_set, datas_per_page)
    try:
        editing_level_modules = paginator.page(page)
    except PageNotAnInteger:
        editing_level_modules = paginator.page(1)
    except EmptyPage:
        editing_level_modules = paginator.page(paginator.num_pages)
    #將使用者搜尋的紀錄儲存下來以利之後選其他頁時知道使用者是搜尋什麼，然後第幾頁這樣
    page_record = list()
    search_record = list()
    for key in search_request_dict:
        if key != "page" and key != "click_sort":
            page_record.append(key + "=" + search_request_dict[key])
            if key != "current_sort" and key != "sorted_direction":
                search_record.append(key + "=" + search_request_dict[key])
    page_record = "&".join(page_record)
    search_record = "&".join(search_record)
    return render(request, "bar_result_table.html",\
     {"has_sample_barcode":has_sample_barcode,"sample_module": sample_module,\
     "editing_modules": editing_level_modules, "page_record": page_record, "search_record": search_record,\
     "search_request_dict": search_request_dict, "sorted_direction": search_request_dict["sorted_direction"],
     "current_sort": search_request_dict["current_sort"], 'pic': pic,
         'cri': criterias, 'rd': rd})

