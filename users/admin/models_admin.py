from django.contrib import admin

from users.models import Actor, Director, BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'biography')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'biography')


