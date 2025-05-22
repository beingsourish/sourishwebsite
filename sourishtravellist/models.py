from django.utils import timezone

from django.db import models

# Create your models here.
class Places(models.Model):
    place_state = models.CharField(max_length=255)

    def __str__(self):
        return self.place_state


class PlacesVisited(models.Model):
    place_name = models.CharField(max_length=255)
    place_city = models.CharField(max_length=255)
    place_zip = models.CharField(max_length=255)
    visited_year = models.IntegerField()
    visited_though = models.CharField(max_length=255)
    place_state = models.ForeignKey(Places, on_delete=models.CASCADE)
    record_create= models.DateTimeField(default=timezone.now)
    record_update= models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

class Userdetails(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)