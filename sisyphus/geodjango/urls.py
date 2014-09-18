from django.conf.urls import patterns, include, url
from django.conf import settings
from djgeojson.views import GeoJSONLayerView
from sisyphus.models import Trail

# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^geodjango/', include('geodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/trails.json', GeoJSONLayerView.as_view(model=Trail, properties=('name'), geometry_field='line'), name='data')
)

# static files (images, css, javascript, etc.)
# (serving from django)
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
