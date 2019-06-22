from django.contrib import admin
from .models import IndividualListInformation


class IndividualListItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'house_address', 'city',
                     'state', 'zip_code', 'country', 'price', 'bedrooms')
    list_per_page = 25


admin.site.register(IndividualListInformation, IndividualListItemAdmin)
