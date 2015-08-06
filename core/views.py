from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required


def login(request):
    template = get_template('login.html')
    return HttpResponse(template.render({'user': request.user}))


def home(request):
    template = get_template('index.html')
    return HttpResponse(template.render())


def landing(request):
    template = get_template('pages/landing.html')
    return HttpResponse(template.render())


def logged(request):
    template = get_template('pages/logged.html')
    return HttpResponse(template.render({'user': request.user}))
