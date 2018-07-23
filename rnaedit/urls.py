"""rnaedit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web import views

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r"^overview/$", views.home),
    url(r"^search/$", views.search),
    url(r"^embed_table/$", views.embed_sites),
    url(r"^barcode/$", views.barcode),
    url(r"^mirna/$", views.mirna_search),
    url(r"^mirna_results/$", views.mirna),
    url(r"^mirna_sites/(?P<mirna>.+)/$", views.mirna_sites),
    url(r"^barcode/(?P<bar>.+)/$", views.barcode),
    url(r"^sample/(?P<cancer>.+)/$", views.sample),
    url(r"^help/$", views.help),
    url(r"^contact/$", views.contact),
    url(r"^editing_detail/$", views.editing_detail),
    url(r"^download_csv/$", views.download_csv),
    url(r"^mi_rna_detail/$", views.mi_rna_detail),
    url(r"^mirexp/(?P<site>.+)/(?P<mir>.+)/$", views.mirexp),
    url(r"^km/(?P<cancer>.+)/(?P<site>.+)/(?P<cut>.+)/$", views.km),
    url(r"^img/mirna/1/(?P<cancer>.+)/(?P<g>.+)/(?P<lt>.+)/$", views.mirnaimg1),
    url(r"^img/sites/1/(?P<cris>.+)/(?P<tar>.+)/(?P<rd>.+)/$", views.sitesimg1),
    url(r"^img/sites/2/(?P<cris>.+)/(?P<tar>.+)/(?P<rd>.+)/$", views.sitesimg2),
    url(r"^img/sites/3/(?P<cris>.+)/(?P<tar>.+)/(?P<rd>.+)/$", views.sitesimg3),
    url(r"^img/sites/4/(?P<cris>.+)/(?P<tar>.+)/(?P<rd>.+)/$", views.sitesimg4),
    url(r"^img/sites/5/(?P<cris>.+)/(?P<tar>.+)/(?P<rd>.+)/$", views.sitesimg5),
    url(r"^img/cancers/1/(?P<cancer>.+)/(?P<rd>.+)/$", views.cancersimg1),
    url(r"^img/cancers/2/(?P<cancer>.+)/(?P<rd>.+)/$", views.cancersimg2),
    url(r"^img/cancers/3/(?P<cancer>.+)/(?P<rd>.+)/(?P<lr>.+)/$", views.cancersimg3),
#    url(r"^addSample/$", views.addSample),
#    url(r"^updateSample/$", views.updateSample),
#    url(r"^addSite/$", views.addSite),
#    url(r"^updateSite/$", views.updateSite),
#    url(r"^addLevel/(?P<cancer>.+)/$", views.addLevel, name='addLevel'),
]
