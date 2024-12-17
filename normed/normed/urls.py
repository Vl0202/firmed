from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView


handler404 = 'pages.views.custom_404_error'
handler500 = 'pages.views.custom_500_error'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('clinic:index'),
        ),
        name='registration',
    ),
    path('news/', include('news.urls', namespace='news')),
    path ('', include('clinic.urls', namespace='clinic'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
