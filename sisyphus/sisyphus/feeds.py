from django.contrib.gis.feeds import Feed
from sisyphus.models import Photo
from django.contrib.sites.models import get_current_site

class PhotosFeed(Feed):
  title = "Latest Trail Photos"
  link = "/images/"
  description = "Latest Trail Photos."

  def items(self):
    return Photo.objects.all()

  def item_title(self, item):
    return item.name

  def item_description(self, item):
    request = None
    full_url = ''.join(['http://', get_current_site(request).domain, item.image.url])
    return "<img src='" + full_url + "' />"

  def item_link(self, item):
    return ""

  def item_geometry(self, item):
    return item.point

