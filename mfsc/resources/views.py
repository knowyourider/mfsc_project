from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Organization, ResourcePage
from sitewide.models import Menu


class ResourceListView(ListView):
    """
    Explicitly call template resource_list.html -
    actually a hand-made resource page
    """
    model = ResourcePage
    # context_object_name = 'resource_page_list' ?
    template_name = 'resources/resource_list.html' 


class ResourcePageDetailView(DetailView):
    model = ResourcePage
    # context_object_name = 'object'
    # template_name = 'resources/resourcepage_detail.html'


class OrganizationListView(ListView):
    model = Organization
    # context_object_name = 'object_list'
    # template_name = 'resources/organization_list.html' 

def about_page(request, slug):
    # special case since there is no "about" app
    object = get_object_or_404(ResourcePage, slug='about')
    about_ = get_object_or_404(Menu, slug='plan')
    about_menu = get_object_or_404(Menu, slug='about')

    return render(request, "resources/about_detail.html", 
        {'object': object, 'about_menu': about_menu}) 
