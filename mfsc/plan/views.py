from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q
from .models import Sector, Goal, Rec, Action, Tag
from .forms import ActionSearchForm

class SearchListView(FormMixin, ListView):
    model = Action
    paginate_by=20
    # context_object_name = 'object_list'
    template_name = 'plan/search_list.html' 
    form_class = ActionSearchForm
    init_data = {'q': ''}

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(), # won't be using this
            'prefix': self.get_prefix(),  # don't know what this is
            'data': self.request.GET or self.init_data # None  # will add my data here
        }
    
    def get(self, request, *args, **kwargs):
        # get starting query set -- hopefully won't need this
        self.object_list = self.get_queryset()
        # get the form
        form = self.get_form(self.get_form_class())

        if form.is_valid():
            q = form.cleaned_data['q']

            # get lists of sectors and ... checked
            sec_list = form.cleaned_data['secs']
            tag_list = form.cleaned_data['tags']
            org_list = form.cleaned_data['orgs']

            if q:
                self.object_list = self.object_list.filter(Q(description__icontains=q) | 
                    Q(background__icontains=q) )

            # sectors -- skip filter if they're all checked
            if len(sec_list) > 0 : # < len(self.init_data['gls'])
                # per undocumented .add method for Q objects
                # https://bradmontgomery.net/blog/adding-q-objects-in-django/
                qquery = Q(rec__goal__sector__slug=sec_list[0])

                for gradelevel in sec_list[1:]:
                    qquery.add((Q(rec__goal__sector__slug=gradelevel)), 'OR' ) # , qquery.connector

                self.object_list = self.object_list.filter(qquery)

            """
                # alt, cryptic method
                # q_list = [Q(gradelevels__short_name='9_12'), 
                #    Q(gradelevels__short_name='6_8')]
                #self.object_list = self.object_list.filter(functools.reduce(OR, q_list))

                # either ends up creating something like:
                #self.object_list = self.object_list.filter(Q(gradelevels__short_name='3_5') | 
                #    Q(gradelevels__short_name='6_8'))
            """
            
            # tags - these narrow (and)
            # so we don't go the Q route which seems more suited for OR
            if len(tag_list) > 0 : 

                for idx, val in enumerate(tag_list):
                    self.object_list = self.object_list.filter(tags__slug=tag_list[idx])

            # Organizations - widen (or)
            if len(org_list) > 0 : 
                qquery = Q(organizations__slug=org_list[0])

                for org in org_list[1:]:
                    qquery.add((Q(organizations__slug=org)), 'OR' ) 

                self.object_list = self.object_list.filter(qquery)

        # test for null result
        print("--- object_list length: " + str(len(self.object_list)))


        # remove any duplicates
        self.object_list = self.object_list.distinct()

        context = self.get_context_data(form=form)
        context['result_count'] = len(self.object_list)
        return self.render_to_response(context)

class SectorListView(ListView):
    model = Sector
    # context_object_name = 'object_list'
    # template_name = 'plan/sector_list.html' 

class InternalSectorListView(ListView):
    model = Sector
    # context_object_name = 'object_list'
    template_name = 'plan/internal_sector_list.html' 


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
