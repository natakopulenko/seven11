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

            images = post_images.filter(time_of_adding=time)
            if images is not None:
                for image_item in images:
                    image = image_item.image.url
            subtitles = post_subtitles.filter(time_of_adding=time)
            if subtitles is not None:
                for subtitle_item in subtitles:
                    subtitle = subtitle_item.subtitle
            items.append({
                'image': image,
                'text': text,
                'subtitle': subtitle,
            })
        return self.PostCodes.ok(post, items)


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': category.id,
                'title': category.title,
                'slug': category.slug,
            } for category in categories]
        }
        return JsonResponse(response, safe=False)


class ServiceTypeView(View):
    def get(self, request, id_category):
        service_types = ServiceType.objects.filter(category=id_category)
        response = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': service_type.id,
                'title': service_type.title
            }for service_type in service_types]
        }
        return JsonResponse(response, safe=False)


class AlbumsView(View):
    def get(self, request):
        albums = Album.objects.all()
        response = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': album.id,
                'title': album.title,
                'number_of_views': album.number_of_views,
                'number_of_photos': album.number_of_photos,
                'date_of_event': album.date_of_event,
                'service': album.service.title,
                'photos': [{'photo': photo.image.url
                            } for photo in AlbumPhoto.objects.filter(album=album.id)[0:2]]
            }for album in albums]
        }
        return JsonResponse(response, safe=False)


class AlbumView(View):
     def get(self, request, id_album):
        album = Album.objects.get(id=id_album)
        response = {
            'code': 0,
            'message': 'OK',
            'data': {
                'id': album.id,
                'title': album.title,
                'service': album.service.title,
                'photos': [{'photo': photo.image.url
                            } for photo in AlbumPhoto.objects.filter(album=album.id)]
            }
        }
        return JsonResponse(response, safe=False)


class CategoryView(View):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        service_types = ServiceType.objects.filter(category=category.id)
        response = {
            'code': 0,
            'message': 'OK',
            'data': [{
                'id': service_type.id,
                'title': service_type.title,
                'services': [{
                    'id': service.id,
                    'title': service.title,
                    'address': service.address,
                    'mark': service.mark,
                }for service in Service.objects.filter(type=service_type.id)[0:10]]
            }for service_type in service_types]
        }
        return JsonResponse(response, safe=False)


class ServicesByTypeView(View):
    class PostCodes(object):
        @classmethod
        def invalid_parameter(cls, parameter_name):
            return HttpResponseBadRequest('parameter {0} is invalid'.format(parameter_name))

        @classmethod
        def ok(cls, type, services):
            return JsonResponse({'code': 0,
                                 'message': 'OK',
                                 'type': type.title,
                                 'data': [{
                                     'id': service.id,
                                     'title': service.title,
                                     'address': service.address,
                                     'mark': service.mark,
                                 } for service in services]})

    def get(self, request, service_type_id):
        services = Service.objects.filter(type=service_type_id)
        service_type = ServiceType.objects.get(id=service_type_id)
        return self.PostCodes.ok(service_type, services)


class ServiceView(View):
    class PostCodes(object):
        @classmethod
        def invalid_parameter(cls, parameter_name):
            return HttpResponseBadRequest('parameter {0} is invalid'.format(parameter_name))

        @classmethod
        def ok(cls, service):
            return JsonResponse({'code': 0,
                                 'message': 'OK',
                                 'data': {
                                     'title': service.title,
                                     'type': service.type.title,
                                     'id': service.id,
                                     'address': service.address,
                                     'phone_number': service.phone_number,
                                     'description': service.description,
                                     'information': service.information,
                                     'site': service.site,
                                     'mark': service.mark,
                                     'schedule': service.schedule,
                                     'tags': [{
                                         'title': tag.title,
                                     }for tag in service.tags.all()]
                                 },
                                 })

    def get(self, request, service_id):
        service = Service.objects.get(id=service_id)
        return self.PostCodes.ok(service)