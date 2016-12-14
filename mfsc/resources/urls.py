from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$',  views.ResourceListView.as_view(), name='resource_list'),
    url(r'^organization/$', views.OrganizationListView.as_view(), 
    	name='organization_list'),
    # resource home is a special case of a resource page
    url(r'^resourcehome/(?P<slug>\S+)/$', 
        views.ResourcePageDetailView.as_view(template_name="resources/resource_list.html"), 
        name='resourcehome_detail'),
    url(r'^resourcepage/(?P<slug>\S+)/$', views.ResourcePageDetailView.as_view(), 
    	name='resourcepage_detail'),
    # special case of resourcepage for about
    # url(r'^about/(?P<slug>\S+)/$', 
    #     views.ResourcePageDetailView.as_view(template_name="resources/about_detail.html"), 
    #     name='about_detail'),
    url(r'^about/(?P<slug>\S+)/$', 
    	views.about_page, name='about_detail'),
]
