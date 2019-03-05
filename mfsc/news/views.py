# from datetime import date
# import datetime
from django.views.generic import ListView
from django.shortcuts import render
from .models import NewsItem


def newsitem_list(request):
	"""
	Using def instead of class -- will make it easier to use a redirect.
	Will need to look up the short name (doubles as anchor tag).
	"""
	object_list = NewsItem.objects.filter(status_num__lte=2)
	context = {'object_list': object_list}
	return render(request, 'news/newsitem_list.html', context)

# class NewsItemListView(ListView):
#     # model = NewsItem
#     # queryset = NewsItem.objects.filter(posted__gt=date.today() - datetime.timedelta(days=20))
#     queryset = NewsItem.objects.filter(status_num__lte=2)
#     # context_object_name = 'object_list'
#     #template_name = 'news/newsitem_list.html' 

class NewsArchiveListView(ListView):
    queryset = NewsItem.objects.filter(status_num=3)
    # context_object_name = 'object_list'
    template_name = 'news/news_archive_list.html' 
