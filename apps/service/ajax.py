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
                                     'image': post.main_image.url,
                                 } for post in posts]})

    def get(self, request):
        posts = Post.objects.all()
        return self.PostCodes.ok(posts)


class PostView(View):
    class PostCodes(object):
        @classmethod
        def invalid_parameter(cls, parameter_name):
            return HttpResponseBadRequest('parameter {0} is invalid'.format(parameter_name))

        @classmethod
        def ok(cls, post, items):
            return JsonResponse({'code': 0,
                                 'message': 'OK',
                                 'data': {
                                     'title': post.title,
                                     'category': post.category.title,
                                     'id': post.id,
                                     'main_image': post.main_image.url,
                                     'items': [{
                                         'image':  item['image'],
                                         'text': item['text'],
                                         'subtitle': item['subtitle'],
                                     } for item in items],

                                 }
                                 })

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post_text = PostText.objects.filter(post=post_id)
        post_images = PostImage.objects.filter(post=post_id)
        post_subtitles = PostSubtitle.objects.filter(post=post_id)
        items_time = []
        items = []
        for text in post_text:
            items_time.append(text.time_of_adding)
        for image in post_images:
            items_time.append(image.time_of_adding)
        for subtitle in post_subtitles:
            items_time.append(subtitle.time_of_adding)
        items_time.sort()
        for time in items_time:
            texts = post_text.filter(time_of_adding=time)
            text = None
            image = None
            subtitle = None
            if texts is not None:
                for text_item in texts:
                    text = text_item.text



class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': category.id,
                'title': category.title
            } for category in categories]
        }
        return JsonResponse(response, safe=False)


class ServiceTypeView(View):
    def get(self, request, id_category):
        servicetypes = ServiceType.objects.filter(category=id_category)
        response = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': servicetype.id,
                'title': servicetype.title
            }for servicetype in servicetypes]
        }
        return JsonResponse(response, safe=False)        return JsonResponse(response, safe=False)
