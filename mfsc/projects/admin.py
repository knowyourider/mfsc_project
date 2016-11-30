from django.contrib import admin
from .models import Project, ProjectImage


class ImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    change_form_template = 'projects/admin/project_change_form.html'
    fieldsets = [
        (None,  {'fields': ['slug', 'title', 'menu_blurb', 'body_text']}),
        ('Related',   {'fields': ['key_action_id', 'actions']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal']}), 
        # , 'classes': ['collapse']
    ]
    inlines = [ImageInline]
    filter_horizontal = ['actions']    
    list_display = ('title',  'slug', 'key_action_id')
    #list_filter     = ['rec__goal__sector'] 
    search_fields = ['title', 'slug']

admin.site.register(Project, ProjectAdmin)
