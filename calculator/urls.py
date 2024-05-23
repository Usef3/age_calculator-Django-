from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.calculate_age_view, name='calculate_age'),
]
