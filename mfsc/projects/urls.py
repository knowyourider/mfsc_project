from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='project_list'),
    url(r'^sub/(?P<slug>\S+)/$', views.SubprojectDetailView.as_view(), name='subproject_detail'),
    url(r'^(?P<slug>\S+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
]
