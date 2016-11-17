from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NewsItemListView.as_view(), name='newsitem_list'),
    #url(r'^(?P<slug>\S+)/$', views.ProjectDetailView.as_view(), name='project_detail'),
]
