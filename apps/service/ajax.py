# coding=utf-8
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.views.generic import View
from core.utils import angular_post_parameters
from core.models import *


class BlogView(View):
    class PostCodes(object):
        @classmethod
        def invalid_parameter(cls, parameter_name):
            return HttpResponseBadRequest('parameter {0} is invalid'.format(parameter_name))

        @classmethod
        def ok(cls, posts):
            return JsonResponse({'code': 0,
                                 'message': 'OK',
                                 'data': [{
                                     'title': post.title,
                                     'category': post.category.title,
                                     'id': post.id,
                                 } for post in posts]})

    def get(self, request):
        posts = Post.objects.all()
        return self.PostCodes.ok(posts)


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        respponse = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': category.id,
                'name': category.title
            } for category in categories]
        }
        return JsonResponse(respponse, safe=False)