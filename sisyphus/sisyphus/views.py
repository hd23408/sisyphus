from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from sisyphus.models import Photo
from sisyphus.models import Trail
from sisyphus.forms import PhotoForm

from django.contrib.gis.geos import Point, GEOSGeometry

import datetime

def images(request):
    # Handle file upload
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            trail = Trail.objects.get(pk=request.POST['trail'])
            point = Point(954158.1, 4215137.1, srid=32140)
            new_photo = Photo(name = form.cleaned_data['name'], image = request.FILES['imgfile'], 
                        upvotes = 0, downvotes = 0, trail = trail, point = point)
            new_photo.save()

            # Redirect to the image list after POST
            return HttpResponseRedirect(reverse('sisyphus.views.images'))
    else:
        form = PhotoForm() # A empty, unbound form

    # Load documents for the list page
    photos = Photo.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'sisyphus/images.html',
        {'photos': photos, 'form': form},
        context_instance=RequestContext(request)
    )

