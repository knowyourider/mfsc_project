from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    """docstring for OrganizationAdmin"""
    fields = ['slug', 'name', 'link_url', 'town', 'phone']
    list_display = ('slug', 'name', 'link_url', 'town', 'phone')
            
admin.site.register(Organization, OrganizationAdmin)
