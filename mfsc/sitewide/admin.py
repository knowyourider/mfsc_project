from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    change_form_template = 'sitewide/admin/menu_blurb_change_form.html'
    fieldsets = [
        (None,  {'fields': ['slug', 'title', 'menu_blurb']}),
        #('Related',   {'fields': ['key_action_id', 'actions']}),
        #('Behind the scenes',   {'fields': ['status_num', 'ordinal']}), 
        # , 'classes': ['collapse']
    ]
    #filter_horizontal = ['actions']    
    list_display = ('title',  'slug', 'id')
    #list_filter     = ['rec__goal__sector'] 
    #search_fields = ['title', 'slug']

admin.site.register(Menu, MenuAdmin)
