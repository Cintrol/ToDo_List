from django.contrib import admin
from django.urls import path, include
from list_item.views import list_item_view, edit_list_view

app_name = 'list_item'

urlpatterns = [
    path('', list_item_view, name='list_item'),
    path('edit/<int:pk>', edit_list_view, name='list_edit')
]