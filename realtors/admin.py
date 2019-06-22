from django.contrib import admin
from .models import RealtorInformation


class RealtorInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp',)
    list_editable = ('is_mvp',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'phone',)
    list_per_page = 25
    ordering = ('id',)


admin.site.register(RealtorInformation, RealtorInformationAdmin)

