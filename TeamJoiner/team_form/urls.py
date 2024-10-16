from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('form/', views.form, name='form'),
    path('admin/', admin.site.urls)
]