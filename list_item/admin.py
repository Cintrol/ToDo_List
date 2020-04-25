from django.contrib import admin
from list_item.models import ListItemModel


class ListItemAdmin(admin.ModelAdmin):
    """
    Регистрируем модель по задачам в админке
    """
    list_display = ['id','name', 'created','modified','list', 'is_done','expare_date']
    list_filter = ['name', 'list']
    search_fields = ['name', 'is_done']

admin.site.register(ListItemModel, ListItemAdmin)