from __future__ import unicode_literals
from djgeojson.fields import PointField
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible 
class Photo(models.Model):
    title = models.CharField(max_length=200)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    longitude = models.FloatField(default = 0)
    latitude = models.FloatField(default= 0)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

    geom = PointField()
    description = models.TextField()
    picture = models.ImageField()

    @property
    def popupContent(self):
      return '<img src="C:\Users\HsiaoWenHui\Documents\GitHub\NTUST_FinalProject\FinalProject\map\ templates\map\NTUST.jpg" /><p><NTUST</p>'
    class Meta:
        ordering = ["-timestamp"]



