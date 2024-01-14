from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailInput()
    birth_data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "age", "birth_data")

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age <= 0 or age > 130:
            raise ValidationError("Некорректный возраст")


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
