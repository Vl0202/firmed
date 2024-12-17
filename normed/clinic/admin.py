from django.contrib import admin

from .models import Doctor
# Register your models here.
admin.site.empty_value_display = 'Не задано'

class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'middle_name',
        'specialty',
        'education',
        'experience_years',
        'biography',
        'photo',
    )

    search_fields = ('first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name',)


admin.site.register(Doctor, DoctorAdmin)
