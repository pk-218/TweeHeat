from django.contrib.gis.db import models


# Create your models here.
class Tweets(models.Model):
    text = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    state_name = models.CharField(null=True, max_length=20)
    location = models.PointField(null=True)

    def __str__(self):
        return self.text


# States
class States(models.Model):
    fid = models.IntegerField()
    program = models.CharField(max_length=15, null=True)
    state_code = models.CharField(max_length=2)
    state_name = models.CharField(max_length=20)
    flowing_st = models.CharField(max_length=1)
    fid_1 = models.IntegerField()
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.state_name


# Clusters
class ClusterBox(models.Model):
    cluster_id = models.IntegerField(null=True)
    box = models.GeometryField()

    def __str__(self):
        return self.cluster_id
