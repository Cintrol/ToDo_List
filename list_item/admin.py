from django.contrib import admin
from list_item.models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    """
    Регистрируем модель по задачам в админке
    """
    task_display = ['id', 'name', 'created', 'modified', 'purpose', 'is_done',
                    'expare_date']
    task_filter = ['name', 'purpose', 'user']
    search_fields = ['name', 'purpose', 'user', 'is_done']


admin.site.register(TaskModel, TaskAdmin)
