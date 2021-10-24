from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
     path('', views.post_list, name='post_list'),
     url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail')
]