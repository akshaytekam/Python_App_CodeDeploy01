# chat/urls.py
from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns = [
    url(r'^$', views.chatting, name='chat'),
    re_path(r'(?P<room_name>[^/]+)/$', views.room, name='room'),
]
