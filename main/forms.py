from django import forms
from main.models import PurposeModel

class PurposeForm(forms.ModelForm):
    """
    Редактирование существующей цели
    """
    pass


class NewPurposeForm(forms.ModelForm):
    """
    Создание новой цели
    """
    class Meta:
        model = PurposeModel
        fields = ['name']
        name = forms.CharField(
            label='Укажите новую цель',
            required=True,
            max_length=120,
            widget=forms.TextInput()
            )
 #      user = forms.CharField()