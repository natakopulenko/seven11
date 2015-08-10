# -*- coding: utf-8 -*-
from core.models import Category, ServiceType, Service, ServicePhotos, ServiceVideos, Tag, ActionType, EventType, \
    PostText, PostImage, Post, BlogCategory, Goods, Action, Event
from django.contrib import admin
from django.contrib.admin.sites import AdminSite

AdminSite.index_title = "Вітаємо"
AdminSite.site_header = "Адмін"
admin.site.register(Category)
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(ServicePhotos)
admin.site.register(ServiceVideos)
admin.site.register(Tag)
admin.site.register(ActionType)
admin.site.register(Action)
admin.site.register(EventType)
admin.site.register(Event)
admin.site.register(Goods)
admin.site.register(BlogCategory)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostText )