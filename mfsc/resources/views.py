from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Organization

class OrganizationListView(ListView):
    model = Organization
    # context_object_name = 'object_list'
    # template_name = 'resources/organization_list.html' 
