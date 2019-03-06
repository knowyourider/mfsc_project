from django.views.generic import ListView, DetailView
# from django.shortcuts import render
from .models import NewsItem


class NewsItemListView(ListView):
    # model = NewsItem
    queryset = NewsItem.objects.filter(status_num__lte=3)
    paginate_by = 10
    # context_object_name = 'object_list'
    #template_name = 'news/newsitem_list.html' 

class NewsItemDetailView(DetailView):
    model = NewsItem
    # context_object_name = 'object'
    # template_name = 'news/newsitem_detail.html'


class NewsArchiveListView(ListView):
    queryset = NewsItem.objects.filter(status_num=3)
    # context_object_name = 'object_list'
    template_name = 'news/news_archive_list.html' 
