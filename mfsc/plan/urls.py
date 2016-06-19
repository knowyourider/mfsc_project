from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.SectorListView.as_view(), name='sector_list'),
    url(r'^goal/rec/action/(?P<pk>\d+)/$', views.ActionDetailView.as_view(), name='action_detail'),
    url(r'^goal/rec/(?P<pk>\d+)/$', views.RecDetailView.as_view(), name='rec_detail'),
    url(r'^goal/(?P<pk>\d+)/$', views.GoalDetailView.as_view(), name='goal_detail'),
    url(r'^(?P<slug>\S+)/$', views.SectorDetailView.as_view(), name='sector_detail'),
]
