"""CBVProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from myApp import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url('response1/',views.view1.as_view(),name='response1'),
    url('update/(?P<pk>\d+)',views.view4.as_view()),
    url('delete/(?P<pk>\d+)',views.view5.as_view()),
    url('create/',views.view3.as_view()),
    url('(?P<pk>\d+)',views.view2.as_view(),name='detail')
]
