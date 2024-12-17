from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import DateTimeInput

from .models import Comment, New


class NewsForm(forms.ModelForm):

    class Meta:
        model = New
        exclude = ('author',)
        widgets = {
            'pub_date': DateTimeInput(
                format='%d-%m-%Y %H:%M:%S', attrs={'type': 'datetime-local'}
            ),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
