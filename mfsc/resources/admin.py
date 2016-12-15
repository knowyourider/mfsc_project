from django.contrib import admin
from .models import Organization, ResourcePage, ResourcePdf

class OrganizationAdmin(admin.ModelAdmin):
    """docstring for OrganizationAdmin"""
    #change_form_template = 'resources/admin/blurb_change_form.html'
    fields = ['slug', 'name', 'link_url', 'town', 'phone', 'description', 'ordinal']
    list_display = ('slug', 'name', 'link_url', 'town', 'phone', 'ordinal')
            
admin.site.register(Organization, OrganizationAdmin)


class ResourcePageAdmin(admin.ModelAdmin):
    """
	A couple of special resource pages
	- about - this has menu set to id=5 so that it will trigger About highlight
	- resources - the hand-made menu pages that call the other resource pages
    """
    change_form_template = 'resources/admin/body_text_change_form.html'
    fields = ['slug', 'title', 'body_text', 'ordinal', 'menu']
    list_display = ('slug', 'title', 'ordinal')
            
admin.site.register(ResourcePage, ResourcePageAdmin)

class ResourcePdfAdmin(admin.ModelAdmin):
    """docstring for ResourcePdf"""
    fields = ['handy_label', 'pdf_file', 'category']
    list_display = ('handy_label', 'pdf_file', 'category')
    list_filter     = ['category'] 
            
admin.site.register(ResourcePdf, ResourcePdfAdmin)
