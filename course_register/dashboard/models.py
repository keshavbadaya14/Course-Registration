from django.db import models
from django.contrib.auth.models import User

class TimeTable(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)  # Monday, Tuesday, etc.
    subject = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

class MessSchedule(models.Model):
    meal = models.CharField(max_length=50)  # Breakfast, Lunch, Dinner
    time = models.TimeField()
    menu = models.TextField()

class ExamSchedule(models.Model):
    course = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.CharField(max_length=100)

class BusSchedule(models.Model):
    route = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    bus_number = models.CharField(max_length=20)
