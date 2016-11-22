from django.shortcuts import render, get_object_or_404
from .models import Menu
from news.models import NewsItem

def home_page(request):

    # get the various menu objects
    object = get_object_or_404(Menu, slug='home')
    projects_menu = get_object_or_404(Menu, slug='projects')
    resources_menu = get_object_or_404(Menu, slug='resources')
    stories_menu = get_object_or_404(Menu, slug='stories')
    news_menu = get_object_or_404(Menu, slug='news')
    newsitem_list = NewsItem.objects.filter(on_homepage=True)

    return render(request, "index.html", 
        {'object': object, 'resources_menu': resources_menu, 'stories_menu': stories_menu, 
        'news_menu': news_menu, 'newsitem_list': newsitem_list, 'projects_menu': projects_menu}) 
