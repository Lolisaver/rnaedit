from web.models import Site

data_path = '/var/www/rnaedit/data/redi_hg38.txt'

with open(data_path, 'r') as f:
    headers = f.readline()
    for line in f:
        d = line.rstrip().split('\t')
        tg = Site()
        if d[3] == '+':
            tg.strand = True
            tg.ref = 'A'
            tg.ed = 'G'
        else:
            tg.strand = False
            tg.ref = 'T'
            tg.ed = 'C'
        tg.key = d[1] + '_' + str(d[2]) + d[3]
        tg.chromo = d[1]
        tg.loc = d[2]
        tg.redi = True
        tg.hyper = False
        tg.save()
