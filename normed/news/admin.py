from django.contrib import admin

from .models import Category, Comment, New
# Register your models here.
admin.site.empty_value_display = 'Не задано'


class NewInline(admin.StackedInline):
    model = New
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        NewInline,
    )


class NewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'is_published',
        'author',
        'category',
    )
    list_editable = (
        'category',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = ('is_published', 'pub_date',)
    list_display_links = ('title',)


admin.site.register(New, NewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
