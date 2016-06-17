from django.contrib import admin
from .models import Sector, Goal

class SectorAdmin(admin.ModelAdmin):
    """docstring for ContentTypeAdmin"""
    fields = ['slug', 'title', 'body_text']
    list_display = ('slug', 'id', 'title')
            
admin.site.register(Sector, SectorAdmin)

class GoalAdmin(admin.ModelAdmin):
    #change_form_template = 'stories/admin/chapter_change_form.html'
    fieldsets = [
        (None,  {'fields': ['sector', 'goal_num', 'description', 'term',
            'body_text']}),
        #('Tags',   {'fields': ['people', 'evidence', 'contexts']}),
        ('Notes',   {'fields': ['responsible', 'stakeholder']}),
    ]
    #filter_horizontal = ['people', 'evidence', 'contexts']    
    #search_fields = ['title']
    list_display = ('description',  'goal_num', 'id', 'sector')
    list_filter     = ['sector'] # , 'edit_date'
    search_fields = ['description']

admin.site.register(Goal, GoalAdmin)
