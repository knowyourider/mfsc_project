from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectListView(ListView):
    # model = Project
    queryset = Project.objects.filter(status_num__gte=1)
    # context_object_name = 'object_list'
    # template_name = 'stories/project_list.html' 

class ProjectDetailView(DetailView):
    model = Project
    # context_object_name = 'object'
    # template_name = 'stories/project_detail.html'

