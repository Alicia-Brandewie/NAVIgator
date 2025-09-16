from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Trip(models.Model):
    location = models.CharField
    start_date = models.DateField
    end_date = models.DateField
    companion = models.CharField
    emergency_contact = models.CharField
    transportation = models.CharField
    lodging = models.CharField
    attractions = models.TextField
    notes = models.TextField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name