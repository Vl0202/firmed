from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from news.forms import EditProfileForm
from news.models import New
from .models import Doctor


User = get_user_model()


def index(request):
    text = ''
    short_news = New.objects.order_by('-pub_date')[:5]
    context = {
        'text':text,
        'short_news': short_news,
    }
    return render(request, 'clinic/index.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'profile': user,
    }

    return render(request, 'clinic/profile.html', context)


@login_required
def edit_profile(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('clinic:profile', username=request.user.username)
    context = {
        'form': form,
    }
    return render(request, 'clinic/edit_profile.html', context)


def doctors(request):
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'clinic/doctors.html', context)

def doctors_detail(request, pk):
    doctor = get_object_or_404(
        Doctor,
        pk=pk
    )
    context = {
        'doctor': doctor,
    }
    return render(request, 'clinic/doctors_detail.html', context)
