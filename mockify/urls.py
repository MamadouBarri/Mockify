from django.contrib import admin
from django.urls import path
from api.views import Mockify
urlpatterns = [
    path('api/', Mockify.as_view()),
]
