from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutPage.as_view(), name='about'),
    path('services/', views.ServicesPage.as_view(), name='services')
]
