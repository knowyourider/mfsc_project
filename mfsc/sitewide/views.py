from django.shortcuts import render, get_object_or_404
from .models import Menu
from news.models import NewsItem

def home_page(request):

    # get the various menu objects
    object = get_object_or_404(Menu, slug='home')
    plan_menu = get_object_or_404(Menu, slug='plan')
    projects_menu = get_object_or_404(Menu, slug='projects')
    resources_menu = get_object_or_404(Menu, slug='resources')
    stories_menu = get_object_or_404(Menu, slug='stories')
    news_menu = get_object_or_404(Menu, slug='news')
    about_menu = get_object_or_404(Menu, slug='about')
    newsitem_list = NewsItem.objects.filter(status_num=1)

    return render(request, "index.html", 
        {'object': object, 'plan_menu': plan_menu, 'resources_menu': resources_menu, 
        'stories_menu': stories_menu, 'news_menu': news_menu, 'newsitem_list': newsitem_list, 
        'projects_menu': projects_menu, 'about_menu': about_menu}) 
