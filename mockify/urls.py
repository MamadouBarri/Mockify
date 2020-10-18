from django.contrib import admin
from django.urls import path
from api.views import Mockify, main_page_view
urlpatterns = [
    path('', main_page_view),
    path('api/', Mockify.as_view()),
]
