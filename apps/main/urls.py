from django.contrib import admin
from django.urls import path, include
from apps.main import views as main_views

urlpatterns = [
    path('', main_views.HomeView.as_view()),
]
