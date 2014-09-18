from django.contrib.gis import admin
from models import Trail

admin.site.register(Trail, admin.GeoModelAdmin)
