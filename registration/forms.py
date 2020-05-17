from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    """
    Форма регистрации нового пользователя
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            'username': {
                'unique_together': "Имя занято",
                'unique': "Имя занято"
            },
            'password2': {
                'password_mismatch': "Пароли не совпадают",
            }
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).first():
            raise forms.ValidationError(
                'E-mail используется: %(value)s',
                code='invalid',
                params={'value': email},
            )
        return email


class LoginForm(forms.Form):
    login = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.PasswordInput()
    )
