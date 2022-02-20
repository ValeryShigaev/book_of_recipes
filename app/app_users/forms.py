from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """ Contains fields for registration """

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'reg_input'}), label='Введите логин')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'reg_input'}), label='Введите пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'reg_input'}), label='Подтвердите пароль')


class LoginForm(forms.Form):
    """ Contains fields for login """

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'reg_input'}), label='Ваш логин')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'reg_input'}), label='Ваш пароль')