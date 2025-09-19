from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Trip(models.Model):
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    companion = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=100)
    transportation = models.CharField(max_length=100)
    lodging = models.CharField(max_length=100)
    attractions = models.TextField(max_length=250)
    notes = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('trip-detail', kwargs={'trip_id': self.id})
    


# class Transportation_stretch(models.Model):
#     type = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     departure_location = models.CharField(max_length=100)
#     destination_location = models.CharField(max_length=100)
#     ticket_number = models.CharField(max_length=100)
#     notes = models.TextField(max_length=250)
#     trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.type
#         #not sure if this is enough info, but place to start