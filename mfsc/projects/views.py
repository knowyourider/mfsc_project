from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, Subproject

class ProjectListView(ListView):
    # model = Project
    queryset = Project.objects.filter(status_num__gte=1)
    # context_object_name = 'object_list'
    # template_name = 'projects/project_list.html' 

class ProjectDetailView(DetailView):
    model = Project
    # context_object_name = 'object'
    # template_name = 'projects/project_detail.html'

class SubprojectDetailView(DetailView):
    model = Subproject
    # context_object_name = 'object'
    # template_name = 'projects/subproject_detail.html'

