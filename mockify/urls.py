from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api.views import Mockify, main_page_view


urlpatterns = [
    path('api/', Mockify.as_view()),
    re_path('', main_page_view),
]

urlpatterns += staticfiles_urlpatterns()
