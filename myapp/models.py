from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Student Model
class Student(models.Model):
    studentID = models.IntegerField()
    studentName = models.CharField(max_length=255)
    studentCourse = models.CharField(max_length=255)
    studentEmail = models.CharField(max_length=255)
    studentUsername = models.CharField(max_length=255)
    studentPassword = models.CharField(max_length=255)


# Bus Model
class Busses(models.Model):
    busID = models.IntegerField()
    busPlateNumber = models.CharField(max_length=255)
    busDriver = models.CharField(max_length=255)
    numberOfSeats = models.IntegerField()
    numberOfVacancies = models.IntegerField()

    def __str__(self):
        return self.numberOfVacancies


# Schedule Model
class Schedule(models.Model):
    scheduleID = models.IntegerField()
    busID = models.IntegerField()
    scheduleDeparture = models.TimeField()
    scheduleArrival = models.TimeField()
    scheduleSeatVacancies = models.IntegerField()


# Admin Model
class AdminHOD(models.Model):
    adminID = models.IntegerField()
    adminUsername = models.IntegerField()
    adminPassword = models.CharField(max_length=255)
    adminName = models.CharField(max_length=255)


# Chief Model
class Chief(models.Model):
    chiefID = models.IntegerField()
    chiefUsername = models.CharField(max_length=255)
    chiefPassword = models.CharField(max_length=255)
    chiefName = models.CharField(max_length=255)


# Reservation Model
class Reservation(models.Model):
    reservationID = models.IntegerField(default=900)
    studentID = models.IntegerField()
    studentName = models.CharField(max_length=255)
    busID = models.IntegerField()
    scheduleID = models.IntegerField()
    scheduleSeatVacancies = models.IntegerField(default=1)


