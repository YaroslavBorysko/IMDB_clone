from django import forms
from users.models import BaseUser
from django.forms import ModelForm


class UserRegisterForm(ModelForm):
    confirm_password = forms.CharField()

    class Meta:
        model = BaseUser
        fields = ['email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Password and Confirm Password do not match")

        return cleaned_data

