from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$',  views.ResourceListView.as_view(), name='resource_list'),
    url(r'^organization/$', views.OrganizationListView.as_view(), name='organization_list'),
    url(r'^resourcepage/(?P<slug>\S+)/$', views.ResourcePageDetailView.as_view(), 
    	name='resourcepage_detail'),
    #url(r'^(?P<slug>\S+)/$', views.StoryDetailView.as_view(), name='story_detail'),
]
