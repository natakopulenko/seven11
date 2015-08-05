# coding=utf-8
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)


class ServiceType(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category)


class Service(models.Model):
    title = models.CharField(max_length=50)
    type = models.ForeignKey(ServiceType)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    information = models.TextField()
    site = models.URLField(max_length=200)
    mark = models.DecimalField(max_digits=3, decimal_places=2)


class Action(models.Model):
    title = models.CharField(max_length=50)
    place = models.ForeignKey(Service)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    phone_number = models.CharField(max_length=20)
    image = models.ImageField()
