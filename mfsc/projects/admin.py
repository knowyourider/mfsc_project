from django.contrib import admin
from .models import Project, Subproject, ProjectImage, ProjectPdf,\
    SubprojectImage, SubprojectPdf


class ImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class PdfInline(admin.TabularInline):
    model = ProjectPdf
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    change_form_template = 'projects/admin/project_change_form.html'
    fieldsets = [
        (None,  {'fields': ['slug', 'title', 'menu_blurb', 'body_text']}),
        ('Related',   {'fields': ['key_action_id', 'actions']}),
        ('Behind the scenes',   {'fields': ['status_num', 'ordinal']}), 
        # , 'classes': ['collapse']
    ]
    inlines = [ImageInline, PdfInline]
    filter_horizontal = ['actions']    
    list_display = ('title',  'slug', 'project_url', 'key_action_id', 'status_num')
    #list_filter     = ['rec__goal__sector'] 
    search_fields = ['title', 'slug']

    def project_url(self, obj):
        return "https://mafoodsystem.org/projects/" + obj.slug + "/"

admin.site.register(Project, ProjectAdmin)

class SubImageInline(admin.TabularInline):
    model = SubprojectImage
    extra = 1

class SubPdfInline(admin.TabularInline):
    model = SubprojectPdf
    extra = 1

class SubprojectAdmin(admin.ModelAdmin):
    change_form_template = 'projects/admin/project_change_form.html'
    fieldsets = [
        (None,  {'fields': ['project', 'slug', 'title', 'body_text']}),
        # ('Behind the scenes',   {'fields': ['status_num']}), 
        # , 'classes': ['collapse']
    ]
    inlines = [SubImageInline, SubPdfInline]
    list_display = ('title',  'slug', 'subproject_url')
    list_filter     = ['project'] 
    search_fields = ['title', 'slug']

    def subproject_url(self, obj):
        return "https://mafoodsystem.org/projects/sub/" + obj.slug + "/"

admin.site.register(Subproject, SubprojectAdmin)

