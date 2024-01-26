from django import forms

from users.forms.mixins import ConfirmPasswordMixinForm
from users.models import BaseUser


class UserRegisterForm(ConfirmPasswordMixinForm):
    confirm_password = forms.CharField()

    class Meta:
        model = BaseUser
        fields = ['email', 'password', 'confirm_password']


class UserUpdateForm(ConfirmPasswordMixinForm):

    class Meta:
        model = BaseUser
        fields = ['email', 'first_name', 'last_name']
