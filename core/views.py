from django.http import HttpResponse
from django.template.loader import get_template


def login(request):
    template = get_template('login.html')
    return HttpResponse(template.render({'user': request.user}))


def home(request):
    template = get_template('index.html')
    return HttpResponse(template.render())


def landing(request):
    template = get_template('pages/landing.html')
    return HttpResponse(template.render({'video': 'https://www.youtube.com/embed/UK6eZauLK9o'}))


def logged(request):
    template = get_template('pages/logged.html')
    return HttpResponse(template.render({'user': request.user}))


def blog(request):
    template = get_template('pages/blog.html')
    return HttpResponse(template.render())


def post(request):
    template = get_template('pages/post.html')
    return HttpResponse(template.render())


def vacation(request):
    template = get_template('pages/vacation.html')
    return HttpResponse(template.render())