"""seven11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from apps.service.ajax import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^$', 'core.views.home'),
    url(r'^login/', 'core.views.login'),
    url(r'^ajax/templates/landing/', 'core.views.landing'),
    url(r'^accounts/profile/', 'core.views.logged'),
    url(r'^ajax/templates/blog/', 'core.views.blog'),
    url(r'^ajax/templates/post/', 'core.views.post'),
    url(r'^accounts/profile/', 'core.views.logged'),
    url(r'^api/v1/blog/$', BlogView.as_view()),
    url(r'^api/v1/category/$', CategoryView.as_view()),
    url(r'^api/v1/category/(\d+)/$', ServiceTypeView.as_view()),
    url(r'^api/v1/posts/(\d+)/$', PostView.as_view()),
]
