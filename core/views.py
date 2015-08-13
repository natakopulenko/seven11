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


def albums(request):
    template = get_template('pages/albums.html')
    return HttpResponse(template.render())


def album(request):
    template = get_template('pages/album.html')
    return HttpResponse(template.render())


def vacation(request):
    template = get_template('pages/vacation.html')
    return HttpResponse(template.render())


def category(request):
    template = get_template('pages/category.html')
    return HttpResponse(template.render())


def service_type(request):
    template = get_template('pages/service_type.html')
    return HttpResponse(template.render())


def service(request):
    template = get_template('pages/service.html')
    return HttpResponse(template.render())


def actions(request):
    template = get_template('pages/actions.html')
    return HttpResponse(template.render())


def action(request):
    template = get_template('pages/action.html')
    return HttpResponse(template.render())