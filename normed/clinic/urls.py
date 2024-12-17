from django.urls import path

from . import views


app_name = 'clinic'

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/<int:pk>', views.doctors_detail, name='doctors_detail'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path ('doctors/', views.doctors, name='doctors')
]
