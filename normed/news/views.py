from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import CommentForm, EditProfileForm, NewsForm
from.models import Category, Comment, New
from .service import get_filtered_queryset, get_paginator, get_sort_and_comment

User = get_user_model()


def news_list(request):
    news_list = get_sort_and_comment(get_filtered_queryset(New))
    context = {
        'page_obj': get_paginator(request, news_list),
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, pk):
    new = get_object_or_404(
        New,
        pk=pk
    )
    if new.author != request.user:
        new = get_object_or_404(
            get_filtered_queryset(New),
            pk=pk
        )
    comments = (
        new.comments.all()
        .select_related('author'))
    form = CommentForm
    context = {'new': new,
               'form': form,
               'comments': comments,
               }
    return render(request, 'news/detail.html', context)


def category_news(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    news_list = (
        get_sort_and_comment(get_filtered_queryset(New))
        .filter(category=category))
    context = {
        'category': category,
        'page_obj': get_paginator(request, news_list),
    }
    return render(request, 'news/category.html', context)


class NewCreateView(LoginRequiredMixin, CreateView):
    model = New
    form_class = NewsForm
    template_name = 'news/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('news:news_list')


class NewUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = New
    form_class = NewsForm
    template_name = 'news/create.html'

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user

    def handle_no_permission(self):
        return redirect('news:news_detail', self.get_object().id)

    def get_success_url(self):
        return reverse('news:news_detail', kwargs={'pk': self.object.pk})


class NewDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = New
    template_name = 'news/create.html'
    success_url = reverse_lazy('news:news_list')

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user

    def handle_no_permission(self):
        return redirect('news:news_detail', self.get_object().id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new'] = self.object
        return context


@login_required
def add_comment(request, pk):
    new = get_object_or_404(New, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.news = new
        comment.save()
    return redirect('news:news_detail', pk=pk)


@login_required
def edit_comment(request, new_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, new_id=new_id)
    if comment.author != request.user:
        raise PermissionDenied
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form. save()
        return redirect('news:news_detail', pk=new_id)
    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'news/comment.html', context)


@login_required
def delete_comment(request, new_id, comment_id):
    comment = get_object_or_404(
        Comment, id=comment_id, author=request.user, new_id=new_id
    )
    if comment.author != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        comment.delete()
        return redirect('news:news_detail', pk=new_id)

    context = {'comment': comment}

    return render(request, 'news/comment.html', context)

