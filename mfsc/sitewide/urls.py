from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),    
    # url(r'^$', views.ProjectListView.as_view(), name='project_list'),
    # url(r'^(?P<slug>\S+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
]
