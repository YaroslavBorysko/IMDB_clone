from django import forms
from django.contrib.auth.hashers import make_password


class ConfirmPasswordMixinForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and not password_confirm and password != password_confirm:
            self.add_error('password_confirm', "confirm password before changing it!")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Password and Confirm Password do not match")
        cleaned_data['password'] = make_password(password)

        return cleaned_data
