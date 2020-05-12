from django import forms
from list_item.models import TaskModel
from django.core.exceptions import NON_FIELD_ERRORS

class NewTaskForm(forms.ModelForm):
    """
    Создание новой цели
    """
    class Meta:
        model = TaskModel
        fields = ['name', 'purpose']
        name = forms.CharField(
            label='Укажите новую задачу',
            required=True,
            max_length=120,
            widget=forms.TextInput()
            )

class PurposeForm(forms.ModelForm):
    """
    Редактирование существующей цели
    """
    name = forms.CharField(
        label='Укажите новое наименование',
        required=True,
        max_length=120,
        widget=forms.TextInput()
    )
    expiere_date = forms.DateTimeField()
    class Meta:
        model = TaskModel
        fields = ['name', 'expiere_date']
