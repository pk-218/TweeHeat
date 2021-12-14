from django.contrib.gis.db import models


# Create your models here.
class Tweets(models.Model):
    text = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.PointField(null=True)

    def __str__(self):
        return self.text
