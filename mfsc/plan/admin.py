from django.contrib import admin
from .models import Sector, Goal, Rec, Action

class SectorAdmin(admin.ModelAdmin):
    """docstring for ContentTypeAdmin"""
    change_form_template = 'plan/admin/sector_change_form.html'
    fields = ['slug', 'title', 'body_text']
    list_display = ('slug', 'id', 'title')
            
admin.site.register(Sector, SectorAdmin)

class GoalAdmin(admin.ModelAdmin):
    change_form_template = 'plan/admin/goal_change_form.html'
    fieldsets = [
        (None,  {'fields': ['sector', 'goal_num', 'description', 'term',
            'body_text']}),
        #('Tags',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Notes',   {'fields': ['responsible', 'stakeholder']}),
    ]
    list_display = ('description',  'goal_num', 'id', 'sector')
    list_filter     = ['sector'] # , 'edit_date'
    search_fields = ['description']
    #filter_horizontal = ['people', 'evidence', 'contexts']    

admin.site.register(Goal, GoalAdmin)

class ActionInline(admin.TabularInline):
    model = Action
    extra = 2

class RecAdmin(admin.ModelAdmin):
    #change_form_template = 'plan/admin/rec_change_form.html'
    fieldsets = [
        (None,  {'fields': ['goal', 'rec_num', 'description', 'term']}),
        #('Tags',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Notes',   {'fields': ['related', 'responsible', 'stakeholder']}),
    ]
    inlines = [ActionInline]
    list_display = ('truncated_description',  'full_rec_num', 'sector_goal')
    list_filter     = ['goal__sector'] 
    search_fields = ['description']
    #filter_horizontal = ['people', 'evidence', 'contexts']    

    def truncated_description(self, obj):
        return obj.description[:40]

    def sector_goal(self, obj):
        return obj.goal.sector.slug + ": " + str(obj.goal.goal_num) + ". " + obj.goal.description[:30]

    def full_rec_num(self, obj):
        return str(obj.goal.sector.id) + "." + str(obj.goal.goal_num) + "." + str(obj.rec_num)

    def sector(self, obj):
        return obj.goal.sector

admin.site.register(Rec, RecAdmin)
