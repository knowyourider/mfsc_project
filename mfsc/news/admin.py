from django.contrib import admin
from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['slug', 'title', 'posted', 'body_text', 'news_image',
            'credit', 'status_num']}),
    ]
    change_form_template = 'news/admin/body_text_change_form.html'
    list_display = ('title', 'slug', 'posted', 'status_num')

admin.site.register(NewsItem, NewsItemAdmin)
