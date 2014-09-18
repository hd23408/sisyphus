from django.conf.urls import patterns, include, url
from django.conf import settings
from djgeojson.views import GeoJSONLayerView
from sisyphus.models import Trail

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/trails.json', GeoJSONLayerView.as_view(model=Trail, properties=('name'), geometry_field='line'), name='data'),
    url(r'^images/$', 'sisyphus.views.images', name='images'),
)

# static files (images, css, javascript, etc.)
# (serving from django)
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
