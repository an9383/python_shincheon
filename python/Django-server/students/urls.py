from django.contrib import admin
from django.urls import path, include
import students.views as views

urlpatterns = [
    path('main/', views.main, name='students.main')
]