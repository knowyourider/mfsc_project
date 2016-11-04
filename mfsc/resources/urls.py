from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="resources/index.html")),
    url(r'^organization/$', views.OrganizationListView.as_view(), name='organization_list'),
    #url(r'^(?P<slug>\S+)/$', views.StoryDetailView.as_view(), name='story_detail'),
    #url(r'^table/(?P<slug>\S+)/$', views.StoryView.as_view(), name='sector_table'),
]
