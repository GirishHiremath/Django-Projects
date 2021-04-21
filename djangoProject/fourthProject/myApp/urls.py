from django.contrib import admin
from django.conf.urls import url
from myApp import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url('response1/',views.view1),
    url('response2/',views.view2)
]
