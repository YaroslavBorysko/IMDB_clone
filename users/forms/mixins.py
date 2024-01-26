from django import forms


class ConfirmPasswordMixinForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and not password_confirm and password != password_confirm:
            self.add_error('password_confirm', "confirm password before changing it!")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Password and Confirm Password do not match")

        return cleaned_data
