from django.views.generic.base import TemplateView
from django.shortcuts import render


def custom_404_error(request, exception):
    return render(request, 'pages/404.html', status=404)

def csrf_failure(request, reason=''):
    return render(request, 'pages/403csrf.html', status=403)

def custom_500_error(request):
    return render(request, 'pages/500.html', status=500)


class AboutPage(TemplateView):
    template_name = 'pages/about.html'


class ServicesPage(TemplateView):
    template_name = 'pages/services.html'
