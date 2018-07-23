from django.shortcuts import render
from ..models import MiexpCancer as MC
import pandas as pd
from random import randint
import matplotlib.pyplot as plt


def mirnaimg1(request, cancer, g, lt):
    lt = float(lt)
    if lt == 0:
        exps = MC.objects.filter(cancer=cancer).values_list('p50', flat=True)
    else:
        exps = MC.objects.filter(cancer=cancer, p50__lt=lt).values_list('p50', flat=True)
    df = pd.DataFrame([exps]).T
    df = df.astype(float)
    fig, ax = plt.subplots()
    ax = df[0].plot.hist(int(g), figsize=(10, 5))
    fig1 = ax.get_figure()
    p1_name = '/var/www/rnaedit/static/img/mirnas/img1/p%s.png' % (randint(1, 10000))
    fig1.savefig(p1_name)
    pic = p1_name.split('static/')[1]
    return render(request, "embedpic.html", {'pic': pic, 'img_src': ''})
