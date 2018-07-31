from .functions.download_csv import download_csv
from .functions.search import search
from .functions.embed_sites import embed_sites
from .functions.barcode import *
from .functions.sample import *
from .functions.mirna import *
from .functions.mirexp import mirexp
from .functions.km import km
from .functions.cox import cox
from .functions.sitesimg3 import sitesimg3
from .functions.sitesimg5 import sitesimg5
from .functions.sitesimg6 import sitesimg6
from .functions.cancersimg3 import cancersimg3
from .functions.mirnaimg1 import mirnaimg1
from .functions.editing_detail import editing_detail
from .functions.mi_rna_detail import mi_rna_detail
from django.shortcuts import render
from random import randint

# Create your views here.


def barcode_search(request):
    return render(request, "barcode_search.html")


def mirna_search(request):
    mi = []
    with open('var/www/rnaedit/static/csv/mirna_input_list.txt', 'r') as file:
        for line in file:
            mi.append(line.rstrip())
    return render(request, "mirna_search.html", {'miropt': mi})


def mirna_sites(request, mirna):
    from web.models import Mirna
    if mirna == 'POST':
        mirna = Mirna.objects.get(name=request.POST['mirna'])
    else:
        mirna = Mirna.objects.get(name=mirna)
    rd = [randint(2000, 4000), randint(5000, 7000)]
    return render(request, "mirna_sites.html", {'mir': mirna, 'rd': rd})


def help(request):
    return render(request, "help.html")


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def addSample(request):
    from .functions import add_Sample
    return render(request, "search_form.html", {"warning": 'Samples added succussfully!'})


def updateSample(request):
    from .functions import update_Sample
    return render(request, "search_form.html", {"warning": 'Samples updated succussfully!'})


def addSite(request):
    from .functions import add_Site
    return render(request, "search_form.html", {"warning": 'Sites added succussfully!'})


def updateSite(request):
    from .functions import update_Site
    return render(request, "search_form.html", {"warning": 'Sites updated succussfully!'})


def addLevel(request, cancer):
    from web.models import Level
    from web.models import Sample
    from web.models import Site
    from django.core.exceptions import ObjectDoesNotExist
    import os
    from .functions.add_Level import update
    update(cancer)
    return render(request, "search_form.html", {"warning": '%s Levels added succussfully!' % (cancer)})




