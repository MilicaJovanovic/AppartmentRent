import datetime

from django.db import models
from django.utils import timezone

class Location(models.Model):
    country = models.CharField(max_length=256, default="")
    place = models.CharField(max_length=256, default="")
    description = models.CharField(max_length=1024, default="")
    photo = models.CharField(max_length=1024, default="")
    distanceBg = models.CharField(max_length=256, default="")
    distanceNis = models.CharField(max_length=256, default="")
    distanceNs = models.CharField(max_length=256, default="")
    def __str__(self):
        return self.place

class Appartment(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    price = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    availableRooms = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def checkFreeRooms(self, availableRooms):
        if availableRooms <= self.availableRooms:
            self.availableRooms -= availableRooms
            return True
        else:
            return False


class User(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    def __str__(self):
        return self.name 

class Reservation(models.Model):
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)
    nameAndSurname = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    personNumber = models.IntegerField(default=0)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    def __str__(self):
        return self.nameAndSurname 
    def starting_soon(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def starting_soon(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    starting_soon.admin_order_field = 'start_date'
    starting_soon.boolean = True
    starting_soon.short_description = 'Starting soon?'
        
class Contact(models.Model):
    name = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    title = models.CharField(max_length=256, default="")
    content = models.CharField(max_length=1024, default="")
    def __str__(self):
        return self.title 

        