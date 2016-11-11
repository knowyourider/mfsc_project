from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Organization, ResourcePage

class ResourceListView(ListView):
    """
    Explicitly call template resource_list.html - actually contains three lists
    of which ResourcePage is only one
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
