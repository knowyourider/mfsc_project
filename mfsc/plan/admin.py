from django.contrib import admin
from .models import Sector, Goal, Rec, Action

class SectorAdmin(admin.ModelAdmin):
    """docstring for ContentTypeAdmin"""
    change_form_template = 'plan/admin/sector_change_form.html'
    fields = ['slug', 'title', 'body_text']
    readonly_fields = ('slug', 'title', 'body_text')
    list_display = ('slug', 'id', 'title')
            
admin.site.register(Sector, SectorAdmin)

class GoalAdmin(admin.ModelAdmin):
    change_form_template = 'plan/admin/goal_change_form.html'
    fieldsets = [
        (None,  {'fields': ['sector', 'goal_num', 'description', 
            'body_text', 'term']}),
        ('Notes',   {'fields': ['responsible', 'stakeholder']}),
    ]
    readonly_fields = ('sector', 'goal_num', 'description')
    list_display = ('description',  'goal_num', 'id', 'sector')
    list_filter     = ['sector'] # , 'edit_date'
    search_fields = ['description']
    #filter_horizontal = ['people', 'evidence', 'contexts']    

admin.site.register(Goal, GoalAdmin)


class RecAdmin(admin.ModelAdmin):
    #change_form_template = 'plan/admin/rec_change_form.html'
    fieldsets = [
        (None,  {'fields': ['goal', 'rec_num', 'description', 'term']}),
        #('Meta info',   {'fields': ['term']}),
        ('Notes',   {'fields': ['related', 'responsible', 'stakeholder']}),
    ]
    readonly_fields = ('goal', 'rec_num', 'description')
    list_display = ('truncated_description',  'full_rec_num', 'sector_goal')
    list_filter     = ['goal__sector'] 
    search_fields = ['description']

    def truncated_description(self, obj):
        return obj.description[:40]

    def sector_goal(self, obj):
        return obj.goal.sector.slug + ": " + str(obj.goal.goal_num) + ". " + \
        obj.goal.description[:30]

    def full_rec_num(self, obj):
        return str(obj.goal.sector.id) + "." + str(obj.goal.goal_num) + "." + \
        str(obj.rec_num)

    def sector(self, obj):
        return obj.goal.sector

admin.site.register(Rec, RecAdmin)


class ActionAdmin(admin.ModelAdmin):
    change_form_template = 'plan/admin/action_change_form.html'
    fieldsets = [
        (None,  {'fields': ['rec', 'action_num', 'description']}),
        ('Meta info',   {'fields': ['background', 'progress', 'metrics',
            'organizations', 'tags', 'actions', 'term']}),
        ('Notes',   {'fields': ['related', 'responsible', 'stakeholder']}),
    ]
    readonly_fields = ('rec', 'action_num', 'description')
    filter_horizontal = ['organizations', 'tags', 'actions']    
    list_display = ('truncated_description',  'act_num', 'goal_rec')
    list_filter     = ['rec__goal__sector'] 
    search_fields = ['description']

    def truncated_description(self, obj):
        return obj.description[:40]

    def goal_rec(self, obj):
        return str(obj.rec.goal.goal_num) + ". " + obj.rec.goal.description[:20] + \
        " - " + str(obj.rec.rec_num) + ". " + obj.rec.description[:20]

    def act_num(self, obj):
        return str(obj.rec.goal.sector.slug) + " " + str(obj.rec.goal.goal_num) + \
        "." + str(obj.rec.rec_num) + "." + str(obj.action_num)

    def sector(self, obj):
        return obj.rec.goal.sector

admin.site.register(Action, ActionAdmin)


