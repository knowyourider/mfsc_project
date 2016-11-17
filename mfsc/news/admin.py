from django.contrib import admin
from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['slug', 'title', 'posted', 'body_text', 
            'is_active', 'on_homepage']}),
    ]
    change_form_template = 'news/admin/body_text_change_form.html'
    list_display = ('title', 'slug', 'posted', 'is_active', 'on_homepage')

admin.site.register(NewsItem, NewsItemAdmin)
