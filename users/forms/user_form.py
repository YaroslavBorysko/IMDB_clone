from django import forms
from users.forms.mixins import ConfirmPasswordMixinForm
from users.models import BaseUser


class UserRegisterForm(ConfirmPasswordMixinForm):
    password_confirm = forms.CharField()

    class Meta:
        model = BaseUser
        fields = ['email', 'password', 'password_confirm']


class UserUpdateForm(ConfirmPasswordMixinForm):

    class Meta:
        model = BaseUser
        fields = ['email', 'first_name', 'last_name']
