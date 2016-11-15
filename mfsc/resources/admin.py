from django.contrib import admin
from .models import Organization, ResourcePage

class OrganizationAdmin(admin.ModelAdmin):
    """docstring for OrganizationAdmin"""
    #change_form_template = 'resources/admin/blurb_change_form.html'
    fields = ['slug', 'name', 'link_url', 'town', 'phone', 'description']
    list_display = ('slug', 'name', 'link_url', 'town', 'phone')
            
admin.site.register(Organization, OrganizationAdmin)


class ResourcePageAdmin(admin.ModelAdmin):
    """docstring for ResourcePageAdmin"""
    change_form_template = 'resources/admin/body_text_change_form.html'
    fields = ['slug', 'title', 'body_text', 'ordinal']
    list_display = ('slug', 'title', 'ordinal')
            
admin.site.register(ResourcePage, ResourcePageAdmin)
