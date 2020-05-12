from django.contrib import admin
from django.urls import path, include
from main.views import (main_view, edit_view, create_view, delete_view)

app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('delete/<int:pk>', delete_view, name='delete'),
    path('create/', create_view, name='create')
]