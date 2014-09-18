from django.contrib.gis.db import models

class Trail(models.Model):
    name = models.CharField(max_length=50)
    cumulative_rating = models.IntegerField()
    num_ratings = models.IntegerField()

    # GeoDjango-specific: a geometry field, and
    # overriding the default manager with a GeoManager instance.
    line = models.LineStringField()
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name

