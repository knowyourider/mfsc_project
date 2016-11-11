from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    change_form_template = 'stories/admin/body_text_change_form.html'
    fieldsets = [
        (None,  {'fields': ['slug', 'title', 'credit', 'body_text', 'actions']}),
        ('Notes',   {'fields': ['related', 'second_image']}),
    ]
    #readonly_fields = ('slug', 'title', 'body_text')
    filter_horizontal = ['actions']    
    list_display = ('title',  'slug', 'credit')
    #list_filter     = ['rec__goal__sector'] 
    search_fields = ['title']


admin.site.register(Story, StoryAdmin)
