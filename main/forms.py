from django import forms
from django.http import request
from main.models import PurposeModel
from django.core.exceptions import NON_FIELD_ERRORS


class PurposeForm(forms.ModelForm):
    """
    Редактирование существующей цели
    """
    class Meta:
        model = PurposeModel
        fields = ['name']
        name = forms.CharField(
            label='Укажите новое наименование',
            required=True,
            max_length=120,
            widget=forms.TextInput()
            )

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
        fields = ['name']

        error_messages = {
            NON_FIELD_ERRORS:{
                'unique_together': "Такая цель уже существует...",
            }
        }
