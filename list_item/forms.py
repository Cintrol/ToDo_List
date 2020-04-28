from django import forms
from list_item.models import TaskModel

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