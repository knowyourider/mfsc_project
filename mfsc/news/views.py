from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsItem

class NewsItemListView(ListView):
    model = NewsItem
    # context_object_name = 'object_list'
    # template_name = 'news/newsitem_list.html' 

