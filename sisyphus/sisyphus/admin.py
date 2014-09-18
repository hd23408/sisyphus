from django.contrib.gis import admin
from models import Trail, Photo

admin.site.register(Trail, admin.GeoModelAdmin)
admin.site.register(Photo, admin.GeoModelAdmin)
