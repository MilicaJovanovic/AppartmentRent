import datetime

from django.db import models
from django.utils import timezone

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
# 	    now = timezone.now()
# 	    return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
class Location(models.Model):
    country = models.CharField(max_length=256)
    place = models.CharField(max_length=256)
    def __str__(self):
        return self.place

class Appartment(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    price = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    def __str__(self):
        return self.name 

class Reservation(models.Model):
    appartment = models.ForeignKey(Appartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default="")
    personNumber = models.IntegerField(default=0)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    def __str__(self):
        return self.name 
    def starting_soon(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def starting_soon(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    starting_soon.admin_order_field = 'start_date'
    starting_soon.boolean = True
    starting_soon.short_description = 'Starting soon?'
        