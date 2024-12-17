from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone


def get_filtered_queryset(mod):
    return mod.objects.select_related(
        'category',
        'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )

def get_paginator(request, news_list):
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def get_sort_and_comment(queryset):
    return queryset.annotate(
        comment_count=Count('comments', distinct=True)
    ).order_by('-pub_date')
