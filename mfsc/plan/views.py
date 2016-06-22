from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sector, Goal, Rec, Action, Tag

class SectorListView(ListView):
    model = Sector
    # context_object_name = 'object_list'
    # template_name = 'plan/sector_list.html' 


class SectorDetailView(DetailView):
    model = Sector
    # context_object_name = 'object'
    # template_name = 'plan/sector_detail.html'
    # goal_list defined in model

class SectorTableView(DetailView):
    model = Sector
    # context_object_name = 'object'
    template_name = 'plan/sector_table.html'
    # goal_list defined in model


class GoalDetailView(DetailView):
    model = Goal
    # context_object_name = 'object'
    # template_name = 'plan/goal_detail.html'
    # rec_list defined in model


class RecDetailView(DetailView):
    model = Rec
    # context_object_name = 'object'
    # template_name = 'plan/rec_detail.html'
    # action_list defined in model

class ActionDetailView(DetailView):
    model = Action
    # context_object_name = 'object'
    # template_name = 'plan/action_detail.html'


class TagListView(ListView):
    model = Tag
    # context_object_name = 'object_list'
    # template_name = 'plan/tag_list.html' 


class TagDetailView(DetailView):
    model = Tag
    # context_object_name = 'object'
    # template_name = 'plan/tag_detail.html'
    # action_list defined in model
