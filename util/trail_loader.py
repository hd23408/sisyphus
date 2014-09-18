#!/usr/bin/python

import osgeo.ogr
import sys, os
sys.path.append("sisyphus/sisyphus")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geodjango.settings")
from sisyphus.models import Trail

shapePath = '../data/trails_public_4326.shp'
shapeData = osgeo.ogr.Open(shapePath)
layer = shapeData.GetLayer()

for index in xrange(layer.GetFeatureCount()):
  feature = layer.GetFeature(index)
  trail_name = feature.GetFieldAsString(3)
  trail_geom = feature.GetGeometryRef()

  try: #TODO: deal with multilinestring
    trail = Trail.objects.get_or_create(
                name=trail_name,
                line=str(trail_geom),
                cumulative_rating=0,
                num_ratings=0
                )
  except:
    continue
