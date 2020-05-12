from django import forms
from list_item.models import TaskModel
from django.core.exceptions import NON_FIELD_ERRORS

class NewTaskForm(forms.ModelForm):
    """
    Создание новой задачи
    """
    class Meta:
        model = TaskModel
        fields = ['name', 'expare_date']
        name = forms.CharField(
            label='Укажите новую задачу',
            required=True,
            max_length=120,
            widget=forms.TextInput()
            )
        expare_date = forms.DateTimeField(
            required=False,
            widget=forms.DateInput(attrs={type: 'date'})
        )
        NON_FIELD_ERRORS: {
            'unique_together': 'Имя уже существует'
        }


class EditTaskForm(forms.ModelForm):
    """
    Редактирование существующей задачи
    """
    class Meta:
        model = TaskModel
        fields = ['name', 'expare_date']
        name = forms.CharField(
            label='Укажите новое наименование',
            required=True,
            max_length=120,
            widget=forms.TextInput()
        )
        expare_date = forms.DateTimeField(
            label = 'укажите новую дату завершения',
            required=False,
            widget=forms.DateInput(attrs={type: 'date'})
        )
