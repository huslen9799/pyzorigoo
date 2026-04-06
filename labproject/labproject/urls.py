
from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path('api/utils/time/' ,views.dt_gettime),
    path('api/one/' ,views.dt_one),
]
