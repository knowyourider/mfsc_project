from django.views.generic import ListView
# from django.shortcuts import render
from .models import NewsItem


class NewsItemListView(ListView):
    # model = NewsItem
    queryset = NewsItem.objects.filter(status_num__lte=2)
    # context_object_name = 'object_list'
    #template_name = 'news/newsitem_list.html' 

class NewsArchiveListView(ListView):
    queryset = NewsItem.objects.filter(status_num=3)
    # context_object_name = 'object_list'
    template_name = 'news/news_archive_list.html' 
