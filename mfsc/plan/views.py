from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sector, Goal, Rec, Action

class SectorListView(ListView):
    model = Sector
    # context_object_name = 'object_list'
    # template_name = 'plan/sector_list.html' 


class SectorDetailView(DetailView):
    model = Sector
    # context_object_name = 'object'
    # template_name = 'stories/sector_detail.html'
    # goal_list defined in model


class GoalDetailView(DetailView):
    model = Goal
    # context_object_name = 'object'
    # template_name = 'stories/goal_detail.html'
    # rec_list defined in model


class RecDetailView(DetailView):
    model = Rec
    # context_object_name = 'object'
    # template_name = 'stories/rec_detail.html'
    # action_list defined in model

class ActionDetailView(DetailView):
    model = Action
    # context_object_name = 'object'
    # template_name = 'stories/action_detail.html'

