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
    tags = models.ManyToManyField('Tag')
    schedule = models.TextField()


class ServicePhotos(models.Model):
    photo = models.ImageField(upload_to='images/')
    service = models.ForeignKey(Service)


class ServiceVideos(models.Model):
    video = models.URLField(max_length=200)


class Tag(models.Model):
    title = models.CharField(max_length=100)


class ActionType(models.Model):
    title = models.CharField(max_length=40)


class Action(models.Model):
    type = models.ForeignKey(ActionType)
    title = models.CharField(max_length=50)
    place = models.ForeignKey(Service)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    phone_number = models.CharField(max_length=20)
    image = models.ImageField()


class EventType(models.Model):
    title = models.CharField(max_length=100)


class Event(models.Model):
    title = models.CharField(max_length=50)
    place = models.ForeignKey(Service)
    date = models.DateTimeField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=40)
    announcement = models.TextField()
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(EventType, blank=True, null=True)


class Goods(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    service_type = models.ManyToManyField(ServiceType)
    number = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)


class BlogCategory(models.Model):
    title = models.CharField(max_length=100)
    number_of_posts = models.IntegerField()


class Post(models.Model):
    category = models.ForeignKey(BlogCategory)
    title = models.CharField(max_length=200)
    publication_time = models.DateTimeField(auto_now_add=True)
    number_of_comments = models.IntegerField()
    main_image = models.ImageField(upload_to='images/')
    description = models.TextField()


class PostImage(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to='images/')
    time_of_adding = models.DateTimeField(auto_now_add=True)


class PostText(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField()
    time_of_adding = models.DateTimeField(auto_now_add=True)


class PostSubtitle(models.Model):
    post = models.ForeignKey(Post)
    subtitle = models.CharField(max_length=500)
    time_of_adding = models.DateTimeField(auto_now_add=True)    time_of_adding = models.DateTimeField()


class Album(models.Model):
    title = models.CharField(max_length=50)
    number_of_views = models.IntegerField()
    number_of_photos = models.IntegerField()
    dote_of_event = models.DateTimeField()
    service_of_photos = models.ForeignKey()


class AlbumPhoto(models.Model):
    images = models.ImageField(upload_to='images/')
    album = models.ForeignKey(Album)