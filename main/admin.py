from django.contrib import admin
from main.models import PurposeModel


class PurposeAdmin(admin.ModelAdmin):
    """
    Регистрируем модель в админке
    """
    purpose_display = ['id', 'created', 'name', 'is_done', 'user']
    purpose_filter = ['id', 'created', 'name', 'is_done']
    search_fields = ['name', 'user']

admin.site.register(PurposeModel, PurposeAdmin)
