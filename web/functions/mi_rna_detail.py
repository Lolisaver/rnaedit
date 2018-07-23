from django.shortcuts import render
from web.models import Bind, Site

def mi_rna_detail(request):
    target_site_key = request.GET["site"]
    if not request.GET["site"].endswith('-'):
        target_site_key = target_site_key[:-1] + '+'
    target_site = Site.objects.get(key=target_site_key)
    gain_mirs = target_site.gain_mir.all()
    loss_mirs = target_site.loss_mir.all()
    gain_binds = Bind.objects.filter(site=target_site, mir=gain_mirs)
    loss_binds = Bind.objects.filter(site=target_site, mir=loss_mirs)
    return render(request, "mi_rna_details.html", {'site': target_site,
                'gain_binds': gain_binds, 'loss_binds': loss_binds})
