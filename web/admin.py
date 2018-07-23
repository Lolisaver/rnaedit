from django.contrib import admin

# Register your models here.

from web.models import Sample
from web.models import Site
from web.models import Level
from web.models import Mirna
from web.models import Bind

admin.site.register(Sample)
admin.site.register(Site)
admin.site.register(Level)
admin.site.register(Mirna)
admin.site.register(Bind)


