from django.contrib import admin
from users.models import BaseUser, Director, Actor


class BaseUserInline(admin.TabularInline):
    model = BaseUser
    extra = 0
    fields = ("email", "first_name", "last_name")
    show_change_link = True

#
# class ActorInline(admin.TabularInline):
#     model = Actor
#     extra = 0
#     fields = ("name", "birthdate")
#     show_change_link = True
#
#
# class DirectorInline(admin.TabularInline):
#     model = Director
#     extra = 0
#     fields = ("name", "birthdate")
#     show_change_link = True
