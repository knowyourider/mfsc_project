"""mfsc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [

    #url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^', include('sitewide.urls', namespace='sitewide')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^plan/', include('plan.urls', namespace='plan')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^stories/', include('stories.urls', namespace='stories')),
    url(r'^admin/', admin.site.urls),
]
