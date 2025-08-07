from django.contrib import admin
from django.urls import path, include
import app.views as views

urlpatterns = [
    path('main/<int:number>', views.main, name='app.main')
]