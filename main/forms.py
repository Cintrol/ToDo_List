from django import forms
from main.models import PurposeModel
from django.core.exceptions import NON_FIELD_ERRORS


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

    class Meta:
        model = PurposeModel
        fields = ['name']


class NewPurposeForm(forms.ModelForm):
    """
    Создание новой цели
    """
    name = forms.CharField(
        required=True,
        widget=forms.TextInput()
    )
    class Meta:
        model = PurposeModel
        fields = ['name', 'user']

        error_messages = {
            NON_FIELD_ERRORS:{
                'unique_together': "Такая цель уже существует...",
            }
        }
